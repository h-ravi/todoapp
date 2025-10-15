from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import datetime, timedelta
from calendar import monthcalendar, month_name
from .models import Todo, Budget, IndianHoliday
import json

# Authentication Views
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


# Home View
@login_required
def home(request):
    # Get all todos first for counting
    all_todos = Todo.objects.filter(user=request.user)
    total_todos = all_todos.count()
    completed_todos = all_todos.filter(status='completed').count()
    pending_todos = all_todos.filter(status='pending').count()
    
    # Get recent todos for display (slice at the end)
    todos = all_todos[:5]
    
    # Budget summary
    today = timezone.now().date()
    month_start = today.replace(day=1)
    budgets_this_month = Budget.objects.filter(user=request.user, date__gte=month_start)
    total_income = budgets_this_month.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = budgets_this_month.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'todos': todos,
        'total_todos': total_todos,
        'completed_todos': completed_todos,
        'pending_todos': pending_todos,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': total_income - total_expense,
    }
    return render(request, 'home.html', context)


# Todo Views
@login_required
def todo_list(request):
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    
    todos = Todo.objects.filter(user=request.user)
    
    if status_filter:
        todos = todos.filter(status=status_filter)
    if priority_filter:
        todos = todos.filter(priority=priority_filter)
    
    context = {
        'todos': todos,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    }
    return render(request, 'todo_list.html', context)


@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        
        todo = Todo.objects.create(
            user=request.user,
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date if due_date else None
        )
        messages.success(request, 'Todo created successfully!')
        return redirect('todo_list')
    
    return render(request, 'todo_form.html', {'action': 'Create'})


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')
        todo.priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        todo.due_date = due_date if due_date else None
        todo.save()
        messages.success(request, 'Todo updated successfully!')
        return redirect('todo_list')
    
    context = {'todo': todo, 'action': 'Update'}
    return render(request, 'todo_form.html', context)


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')


# Calendar Views
@login_required
def calendar_view(request):
    year = int(request.GET.get('year', timezone.now().year))
    month = int(request.GET.get('month', timezone.now().month))
    
    # Get calendar data
    cal = monthcalendar(year, month)
    month_name_str = month_name[month]
    
    # Get holidays for this month
    holidays = IndianHoliday.objects.filter(year=year, date__month=month)
    holidays_dict = {holiday.date.day: holiday for holiday in holidays}
    
    # Navigation
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    
    context = {
        'calendar': cal,
        'year': year,
        'month': month,
        'month_name': month_name_str,
        'holidays': holidays_dict,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    }
    return render(request, 'calendar.html', context)


# Calculator View
@login_required
def calculator_view(request):
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Safe evaluation of mathematical expressions
            result = eval(expression, {"__builtins__": {}}, {})
        except:
            result = 'Error'
    
    return render(request, 'calculator.html', {'result': result})


# Budget Views
@login_required
def budget_list(request):
    view_type = request.GET.get('view', 'day')
    
    today = timezone.now().date()
    budgets = Budget.objects.filter(user=request.user)
    
    if view_type == 'day':
        budgets = budgets.filter(date=today)
        period = f"Today ({today})"
    elif view_type == 'week':
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        budgets = budgets.filter(date__gte=week_start, date__lte=week_end)
        period = f"This Week ({week_start} to {week_end})"
    elif view_type == 'month':
        budgets = budgets.filter(date__year=today.year, date__month=today.month)
        period = f"{month_name[today.month]} {today.year}"
    elif view_type == 'year':
        budgets = budgets.filter(date__year=today.year)
        period = f"Year {today.year}"
    else:
        period = "All Time"
    
    total_income = budgets.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = budgets.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense
    
    # Category-wise breakdown
    category_data = {}
    for budget in budgets:
        if budget.category not in category_data:
            category_data[budget.category] = {'income': 0, 'expense': 0}
        if budget.type == 'income':
            category_data[budget.category]['income'] += float(budget.amount)
        else:
            category_data[budget.category]['expense'] += float(budget.amount)
    
    context = {
        'budgets': budgets,
        'view_type': view_type,
        'period': period,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'category_data': category_data,
    }
    return render(request, 'budget_list.html', context)


@login_required
def budget_create(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        
        Budget.objects.create(
            user=request.user,
            type=type,
            category=category,
            amount=amount,
            description=description,
            date=date
        )
        messages.success(request, 'Budget entry created successfully!')
        return redirect('budget_list')
    
    return render(request, 'budget_form.html', {'action': 'Create'})


@login_required
def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    
    if request.method == 'POST':
        budget.type = request.POST.get('type')
        budget.category = request.POST.get('category')
        budget.amount = request.POST.get('amount')
        budget.description = request.POST.get('description')
        budget.date = request.POST.get('date')
        budget.save()
        messages.success(request, 'Budget entry updated successfully!')
        return redirect('budget_list')
    
    context = {'budget': budget, 'action': 'Update'}
    return render(request, 'budget_form.html', context)


@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    budget.delete()
    messages.success(request, 'Budget entry deleted successfully!')
    return redirect('budget_list')
