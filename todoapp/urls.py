from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Home
    path('', views.home, name='home'),
    
    # Todo
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.todo_create, name='todo_create'),
    path('todos/<int:pk>/update/', views.todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    
    # Calendar
    path('calendar/', views.calendar_view, name='calendar'),
    
    # Calculator
    path('calculator/', views.calculator_view, name='calculator'),
    
    # Budget
    path('budget/', views.budget_list, name='budget_list'),
    path('budget/create/', views.budget_create, name='budget_create'),
    path('budget/<int:pk>/update/', views.budget_update, name='budget_update'),
    path('budget/<int:pk>/delete/', views.budget_delete, name='budget_delete'),
]
