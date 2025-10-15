<div align="center">

# 📝 Django Todo App

### A Feature-Rich Task Management System with Multi-Role Support

[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)

**A comprehensive, full-stack web application built with Django, featuring authentication, role-based access control, todo management, budget tracking, Indian holidays calendar, and an integrated calculator.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Admin Guide](#-admin-panel) • [API](#-project-structure) • [Contributing](#-contributing)

---

</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Database Schema](#-database-schema)
- [User Roles & Permissions](#-user-roles--permissions)
- [Admin Panel](#-admin-panel)
- [API Endpoints](#-api-endpoints)
- [Usage Guide](#-usage-guide)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**Django Todo App** is a modern, full-featured task management system designed for individuals and teams. Built with Django 5.2, it combines essential productivity tools into a single, intuitive platform. Whether you're managing personal tasks, tracking expenses, or planning around Indian holidays, this application has you covered.

### Why This Project?

- **🔐 Secure Authentication**: Industry-standard user authentication with session management
- **👥 Multi-Role Support**: Super Admin, Admin, Manager, and User roles with granular permissions
- **📊 Budget Tracking**: Comprehensive income/expense tracking with multiple time-period views
- **📅 Cultural Awareness**: Pre-loaded Indian holidays calendar (2025-2026)
- **🧮 Integrated Tools**: Built-in calculator for quick computations
- **📱 Responsive Design**: Beautiful UI that works on all devices
- **🚀 Production Ready**: Clean code, well-documented, and easily deployable

---

## ✨ Features

### 🔐 1. **Authentication & User Management**

#### Core Authentication
- ✅ **User Registration**: Secure signup with email validation
- ✅ **Login/Logout**: Session-based authentication
- ✅ **Password Security**: Hashed passwords using Django's built-in security
- ✅ **Form Validation**: Client and server-side validation
- ✅ **Session Management**: Secure user sessions with timeout
- ✅ **User Profiles**: Extended user model with roles and contact information

#### Role-Based Access Control
- **Super Admin**: Full system control, can manage all users and data
- **Admin**: Admin panel access, can manage users and application data
- **Manager**: Limited oversight, can view reports and manage assigned users
- **User**: Standard access to personal todos and budgets

### 👥 2. **Admin Panel & User Management**

#### Django Admin Panel
- **URL**: `http://127.0.0.1:8000/admin/`
- **Customized Interface**: Enhanced with role-based filtering and bulk operations
- **User Management**:
  - Create, read, update, delete users
  - Assign roles (User, Manager, Admin, Super Admin)
  - Manage permissions and groups
  - View user activity and statistics
  - Bulk actions (activate, deactivate, delete)
- **Data Management**:
  - Manage all todos across users
  - Control budget entries
  - Add/edit Indian holidays
  - Export data for reports
- **Advanced Features**:
  - Search and filter by multiple criteria
  - Inline editing for quick updates
  - Auto-complete fields for relationships
  - Date hierarchy navigation
  - Custom actions and bulk operations

#### User Role Management
- Create new admins with specific roles using CLI
- Update user roles on-the-fly
- View role-based statistics
- Audit user permissions

### ✅ 3. **Todo Management System**

#### Todo Features
- **CRUD Operations**: Create, Read, Update, Delete todos
- **Todo Properties**:
  - Title and detailed description
  - Status tracking (Pending → In Progress → Completed)
  - Priority levels (Low, Medium, High)
  - Due date with datetime picker
  - Automatic timestamps (created_at, updated_at)
- **Filtering & Search**:
  - Filter by status (pending/in_progress/completed)
  - Filter by priority (low/medium/high)
  - Search by title and description
  - Sort by date, priority, or status
- **Dashboard Statistics**:
  - Total todos count
  - Completed tasks percentage
  - Pending tasks overview
  - Recent todos display (last 5)
- **Visual Indicators**:
  - Color-coded priority badges
  - Status icons (pending, in-progress, completed)
  - Due date warnings
  - Progress tracking

### 📅 4. **Calendar with Indian Holidays**

#### Calendar Features
- **Interactive Calendar View**:
  - Monthly grid layout
  - Navigate between months and years
  - Previous/Next month navigation
  - Current month highlighting
- **Indian National Holidays** (Pre-loaded):
  - Republic Day (January 26)
  - Independence Day (August 15)
  - Gandhi Jayanti (October 2)
- **Religious & Cultural Festivals** (40+ holidays):
  - Hindu: Diwali, Holi, Ganesh Chaturthi, Navratri, Dussehra, etc.
  - Islamic: Eid ul-Fitr, Eid ul-Adha, Muharram
  - Christian: Christmas, Good Friday
  - Sikh: Guru Nanak Jayanti
  - Buddhist: Buddha Purnima
  - Jain: Mahavir Jayanti
  - Regional: Pongal, Onam, Baisakhi
- **Holiday Details**:
  - Holiday name and description
  - National holiday badge
  - Date and year information
  - Visual highlighting (yellow for national, red for others)
- **Holiday List View**:
  - Comprehensive list of holidays for selected month
  - Filter by year
  - Search holidays by name
- **Pre-loaded Data**: 2025-2026 holidays included

### 🧮 5. **Built-in Calculator**

#### Calculator Features
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **User Interface**:
  - Clean, intuitive button layout
  - Large display screen
  - Responsive design
  - Color-coded buttons (numbers, operators, functions)
- **Input Methods**:
  - Click buttons with mouse
  - Full keyboard support
  - Number keys (0-9)
  - Operator keys (+, -, *, /)
  - Enter/= for calculation
  - Escape/C for clear
  - Backspace for delete
- **Features**:
  - Real-time display updates
  - Error handling
  - Decimal point support
  - Clear and delete functions
  - Instant calculations


### 💰 6. **Budget Tracker**

#### Budget Management
- **Track Income & Expenses**: Comprehensive financial tracking
- **Time-Period Views**:
  - **Day-wise**: Today's transactions
  - **Week-wise**: Current week summary (Monday-Sunday)
  - **Monthly**: Current month overview
  - **Yearly**: Annual budget tracking
  - **All Time**: Complete financial history
- **Category Management** (8 categories):
  - Food & Dining
  - Transportation
  - Entertainment & Recreation
  - Utilities (Electricity, Water, Internet)
  - Healthcare & Medical
  - Education & Learning
  - Shopping & Personal
  - Other Expenses
- **Financial Analytics**:
  - Total income calculation
  - Total expense calculation
  - Net balance (Income - Expense)
  - Category-wise breakdown
  - Visual summary with color-coded amounts
- **Budget Features**:
  - Add, edit, delete entries
  - Date selection for each transaction
  - Description field for notes
  - Amount with decimal support (₹)
  - Type selection (Income/Expense)
- **Reports & Insights**:
  - Category-wise income/expense table
  - Net amount per category
  - Period-wise summaries
  - Quick view of financial health

### 🗄️ 7. **SQLite Database**

#### Database Features
- **Lightweight**: SQLite3 - no separate database server required
- **File-based**: Single `db.sqlite3` file contains all data
- **ACID Compliant**: Reliable and consistent data storage
- **Zero Configuration**: Works out of the box
- **Data Persistence**:
  - User accounts and profiles
  - Todo items with all attributes
  - Budget entries with transactions
  - Indian holidays (2025-2026)
  - Session data
  - Admin logs and history

### 🎨 8. **User Interface**

#### Design Features
- **Bootstrap 5.3**: Modern, responsive framework
- **Font Awesome 6.4**: 1000+ icons for visual clarity
- **Custom Styling**:
  - Gradient backgrounds
  - Card-based layouts
  - Smooth animations and transitions
  - Hover effects
  - Color-coded elements
- **Responsive Design**:
  - Mobile-first approach
  - Works on phones, tablets, desktops
  - Adaptive navigation
  - Flexible layouts
- **User Experience**:
  - Intuitive navigation
  - Clear visual hierarchy
  - Success/error messages
  - Loading indicators
  - Confirmation dialogs

---

## 📸 Screenshots

### Dashboard
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)
*Main dashboard showing todo statistics, budget summary, and quick access buttons*

### Todo Management
![Todo List](https://via.placeholder.com/800x400?text=Todo+Management)
*Todo list with filtering options and priority badges*

### Calendar View
![Calendar](https://via.placeholder.com/800x400?text=Calendar+with+Holidays)
*Interactive calendar displaying Indian holidays*

### Budget Tracker
![Budget](https://via.placeholder.com/800x400?text=Budget+Tracker)
*Budget tracker with income/expense breakdown*

### Admin Panel
![Admin](https://via.placeholder.com/800x400?text=Admin+Panel)
*Django admin panel with user management*

---

## 🛠️ Tech Stack

### Backend
- **Django 5.2.7** - High-level Python web framework
- **Python 3.12.3** - Programming language
- **SQLite3** - Embedded database engine

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling with custom properties
- **JavaScript (ES6+)** - Client-side interactivity
- **Bootstrap 5.3.0** - CSS framework
- **Font Awesome 6.4.0** - Icon library

### Tools & Libraries
- **Django Admin** - Built-in admin interface
- **Django ORM** - Object-Relational Mapping
- **Django Forms** - Form handling and validation
- **Django Auth** - Authentication system
- **Django Messages** - Flash messages
- **Django Signals** - Event-driven programming

---

## 📥 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.12 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer)
- **Git** (optional, for cloning)

### Step 1: Clone the Repository

```bash
# Using Git
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app

# Or download and extract ZIP file
```

### Step 2: Create Virtual Environment

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required Packages:**
- Django==5.2.7
- Pillow==10.4.0 (for image handling)

### Step 4: Database Setup

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Load Initial Data

```bash
# Populate Indian holidays (2025-2026)
python manage.py populate_holidays

# Create super admin user
python manage.py create_admin_user --username admin --email admin@admin.com --password admin --role superadmin
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

### Step 7: Access the Application

Open your browser and navigate to:
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

**Default Credentials:**
- Username: `admin`
- Password: `admin`

---

## 🚀 Quick Start

### For First-Time Users

1. **Sign Up**
   ```
   Navigate to: http://127.0.0.1:8000/signup/
   Create your account
   ```

2. **Login**
   ```
   Go to: http://127.0.0.1:8000/login/
   Enter your credentials
   ```

3. **Explore Features**
   - Create your first todo
   - Add a budget entry
   - Check the calendar
   - Try the calculator

### For Administrators

1. **Access Admin Panel**
   ```
   URL: http://127.0.0.1:8000/admin/
   Username: admin
   Password: admin
   ```

2. **Manage Users**
   - Create new users with roles
   - Edit user permissions
   - View user activity

3. **Manage Data**
   - View all todos and budgets
   - Add/edit holidays
   - Export reports

---

## 📁 Project Structure

```
django-todo-app/
│
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database file
├── requirements.txt                   # Python dependencies
├── README.md                         # Project documentation
├── LICENSE                           # License file
│
├── todoproject/                      # Project configuration
│   ├── __init__.py
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # Main URL configuration
│   ├── wsgi.py                      # WSGI configuration
│   └── asgi.py                      # ASGI configuration
│
├── todoapp/                          # Main application
│   ├── __init__.py
│   ├── admin.py                     # Admin panel configuration
│   ├── apps.py                      # App configuration
│   ├── models.py                    # Database models
│   ├── views.py                     # View functions
│   ├── urls.py                      # App URL patterns
│   ├── tests.py                     # Unit tests
│   │
│   ├── migrations/                  # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_userprofile.py
│   │
│   ├── management/                  # Custom management commands
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       ├── create_admin.py      # Create default admin
│   │       ├── create_admin_user.py # Create admin with roles
│   │       ├── create_profiles.py   # Create user profiles
│   │       ├── populate_holidays.py # Load holidays
│   │       └── verify_admins.py     # Verify admin users
│   │
│   └── templatetags/                # Custom template filters
│       ├── __init__.py
│       └── custom_filters.py        # Dictionary access filters
│
├── templates/                        # HTML templates
│   ├── base.html                    # Base template
│   ├── home.html                    # Dashboard
│   ├── login.html                   # Login page
│   ├── signup.html                  # Sign up page
│   ├── todo_list.html               # Todo list
│   ├── todo_form.html               # Todo create/edit
│   ├── calendar.html                # Calendar view
│   ├── calculator.html              # Calculator
│   ├── budget_list.html             # Budget list
│   └── budget_form.html             # Budget create/edit
│
└── static/                          # Static files
    ├── css/                         # Custom stylesheets
    ├── js/                          # JavaScript files
    └── images/                      # Image assets
```

---

## 🗄️ Database Schema

### User Model (Extended)
```python
User (Django built-in)
├── id (PK)
├── username
├── email
├── password (hashed)
├── first_name
├── last_name
├── is_staff
├── is_superuser
├── is_active
├── date_joined
└── last_login

UserProfile (Extended)
├── id (PK)
├── user_id (FK → User)
├── role (user/manager/admin/superadmin)
├── phone
├── address
├── created_at
└── updated_at
```

### Todo Model
```python
Todo
├── id (PK)
├── user_id (FK → User)
├── title
├── description
├── status (pending/in_progress/completed)
├── priority (low/medium/high)
├── due_date
├── created_at
└── updated_at
```

### Budget Model
```python
Budget
├── id (PK)
├── user_id (FK → User)
├── type (income/expense)
├── category (food/transport/etc.)
├── amount (Decimal)
├── description
├── date
└── created_at
```

### IndianHoliday Model
```python
IndianHoliday
├── id (PK)
├── name
├── date
├── description
├── is_national (Boolean)
└── year
```

---

## 👥 User Roles & Permissions

| Feature | User | Manager | Admin | Super Admin |
|---------|------|---------|-------|-------------|
| **Login/Signup** | ✅ | ✅ | ✅ | ✅ |
| **Own Todos** | ✅ | ✅ | ✅ | ✅ |
| **Own Budget** | ✅ | ✅ | ✅ | ✅ |
| **Calendar** | ✅ | ✅ | ✅ | ✅ |
| **Calculator** | ✅ | ✅ | ✅ | ✅ |
| **View Other Users** | ❌ | ⚠️ Limited | ✅ | ✅ |
| **Admin Panel** | ❌ | ❌ | ✅ | ✅ |
| **Manage All Todos** | ❌ | ❌ | ✅ | ✅ |
| **Manage All Budgets** | ❌ | ❌ | ✅ | ✅ |
| **Add/Delete Users** | ❌ | ❌ | ⚠️ Limited | ✅ |
| **Change User Roles** | ❌ | ❌ | ❌ | ✅ |
| **Manage Holidays** | ❌ | ❌ | ✅ | ✅ |
| **System Settings** | ❌ | ❌ | ❌ | ✅ |

### Role Descriptions

#### 🟢 User (Default)
- Regular application access
- Manage personal todos and budgets
- View calendar and use calculator
- No admin privileges

#### 🔵 Manager
- All user features
- View reports (future feature)
- Manage assigned team members
- Limited oversight capabilities

#### 🟡 Admin
- Access to admin panel
- Manage all users (except super admins)
- Control all todos and budgets
- Manage holidays
- Export data and reports

#### 🔴 Super Admin
- Full system control
- Create/edit/delete any user
- Change user roles
- Access all features
- System-level permissions

---

## 🎛️ Admin Panel

### Accessing Admin Panel

```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: admin
```

### Admin Features

#### 1. User Management
- **List Users**: View all registered users
  - Filter by: Role, Staff Status, Active Status, Join Date
  - Search by: Username, Email, Name
  - Bulk actions: Activate, Deactivate, Delete
  
- **Add User**: Create new users with role selection
  - Assign role during creation
  - Set permissions automatically
  - Configure staff/superuser status

- **Edit User**: Modify user details
  - Change role
  - Update permissions
  - Edit profile information
  - Reset password

#### 2. User Profile Management
- View/edit user profiles
- Update roles inline
- Add contact information
- Track profile creation dates

#### 3. Todo Management
- View all todos from all users
- See user role alongside each todo
- Filter by: User, Status, Priority, Date
- Bulk edit status and priority
- Search todos by content

#### 4. Budget Management
- Monitor all financial entries
- Filter by: Type, Category, Date, User
- View user role with each entry
- Edit entries inline
- Export for reports

#### 5. Holiday Management
- Add custom holidays
- Edit existing holidays
- Mark national holidays
- Delete holidays
- Import/export holiday data

### Creating New Admins

#### Via Command Line (Recommended)
```bash
# Interactive mode
python manage.py create_admin_user

# With parameters
python manage.py create_admin_user \
  --username newadmin \
  --email admin@example.com \
  --password securepass123 \
  --role superadmin
```

#### Via Admin Panel
1. Login to admin panel
2. Click "Users" → "ADD USER +"
3. Fill in details
4. Select role from dropdown
5. Click "SAVE"

---

## 🔌 API Endpoints

### Authentication URLs
```
/signup/                 - User registration
/login/                  - User login
/logout/                 - User logout
```

### Application URLs
```
/                        - Home dashboard
/todos/                  - Todo list
/todos/create/           - Create todo
/todos/<id>/update/      - Update todo
/todos/<id>/delete/      - Delete todo
/calendar/               - Calendar view
/calculator/             - Calculator
/budget/                 - Budget list
/budget/create/          - Create budget entry
/budget/<id>/update/     - Update budget entry
/budget/<id>/delete/     - Delete budget entry
```

### Admin URLs
```
/admin/                  - Admin panel
/admin/auth/user/        - User management
/admin/todoapp/todo/     - Todo management
/admin/todoapp/budget/   - Budget management
/admin/todoapp/indianholiday/ - Holiday management
```

---

## 📖 Usage Guide

### 1. Getting Started

#### Create Your Account
1. Navigate to http://127.0.0.1:8000/signup/
2. Fill in registration form:
   - Username (unique)
   - Email address
   - Password
   - Confirm password
3. Click "Sign Up"
4. Automatically logged in and redirected to dashboard

#### Login to Existing Account
1. Go to http://127.0.0.1:8000/login/
2. Enter username and password
3. Click "Login"
4. Access main dashboard

### 2. Managing Todos

#### Creating Todos
1. Click "Todos" in navbar
2. Click "New Todo" button
3. Fill in todo details:
   - **Title**: Task name (required)
   - **Description**: Detailed information
   - **Status**: Pending/In Progress/Completed
   - **Priority**: Low/Medium/High
   - **Due Date**: Optional deadline
4. Click "Save"

#### Viewing & Filtering Todos
- **View All**: See complete todo list
- **Filter by Status**: Pending, In Progress, or Completed
- **Filter by Priority**: Low, Medium, or High
- **Sort**: By creation date (newest first)

#### Editing Todos
1. Click "Edit" button on todo card
2. Update any field
3. Click "Save"

#### Deleting Todos
1. Click "Delete" button
2. Confirm deletion
3. Todo permanently removed

### 3. Budget Tracking

#### Adding Budget Entry
1. Click "Budget" in navbar
2. Click "New Entry" button
3. Fill in details:
   - **Type**: Income or Expense
   - **Category**: Select from 8 categories
   - **Amount**: Enter amount in ₹
   - **Date**: Transaction date
   - **Description**: Optional notes
4. Click "Save"

#### Viewing Budget Reports
- **Day View**: Today's transactions
- **Week View**: Current week (Mon-Sun)
- **Month View**: Current month
- **Year View**: Current year
- **All View**: Complete history

Each view shows:
- Total income
- Total expense
- Net balance
- Category-wise breakdown

#### Managing Budget Entries
- **Edit**: Update any entry
- **Delete**: Remove transactions
- **Filter**: By date range, category, type

### 4. Using the Calendar

#### Viewing Calendar
1. Click "Calendar" in navbar
2. See current month with holidays
3. Navigate months:
   - **Previous**: Go to previous month
   - **Next**: Go to next month

#### Understanding Holiday Markers
- **Yellow Background**: National holidays
- **Red Background**: Other holidays
- **Holiday Badge**: "National" tag for national holidays

#### Viewing Holiday Details
- Scroll below calendar
- See complete list of holidays for the month
- View holiday descriptions

### 5. Using the Calculator

#### Methods of Input
**Mouse Input:**
- Click number buttons (0-9)
- Click operator buttons (+, -, ×, /)
- Click "=" for result
- Click "C" to clear

**Keyboard Input:**
- Press number keys (0-9)
- Press operator keys (+, -, *, /)
- Press Enter or = for result
- Press Escape or C to clear
- Press Backspace to delete last digit

#### Performing Calculations
1. Enter first number
2. Click/press operator
3. Enter second number
4. Click/press equals
5. View result

### 6. Admin Dashboard

#### Accessing as Admin
1. Login with admin credentials
2. Click "Admin" link in navbar
3. OR go directly to /admin/

#### Managing Users
**View Users:**
- Click "Users" in admin panel
- See all registered users
- View roles, email, join date

**Add New User:**
1. Click "ADD USER +"
2. Enter username, email, password
3. Select role (User/Manager/Admin/Super Admin)
4. Click "SAVE"

**Edit User:**
1. Click on username
2. Update details
3. Change role if needed
4. Save changes

**Bulk Actions:**
- Select multiple users (checkboxes)
- Choose action from dropdown
- Click "Go"

#### Managing Application Data
**Todos:**
- View todos from all users
- Filter by user, status, priority
- Edit or delete any todo

**Budgets:**
- Monitor all financial entries
- Filter by type, category, user
- Edit or delete entries

**Holidays:**
- Add new holidays
- Edit existing holidays
- Mark as national holiday
- Delete holidays

---

## ⚙️ Configuration

### Django Settings

#### Key Settings (todoproject/settings.py)

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Templates
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]

# Login URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

# Security (Development)
DEBUG = True
SECRET_KEY = 'your-secret-key-here'
ALLOWED_HOSTS = []
```

### Environment Variables (Recommended for Production)

Create a `.env` file:
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Custom Management Commands

```bash
# Create admin user
python manage.py create_admin_user

# Verify admins
python manage.py verify_admins

# Create profiles for existing users
python manage.py create_profiles

# Populate holidays
python manage.py populate_holidays

# Change password
python manage.py changepassword username
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test todoapp

# Run with verbosity
python manage.py test --verbosity=2

# Keep test database
python manage.py test --keepdb
```

### Test Coverage

```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run --source='.' manage.py test

# Generate report
coverage report

# HTML report
coverage html
```

### Manual Testing Checklist

- [ ] User registration works
- [ ] User login/logout works
- [ ] Todo CRUD operations work
- [ ] Budget CRUD operations work
- [ ] Calendar displays holidays
- [ ] Calculator functions correctly
- [ ] Admin panel accessible
- [ ] User roles enforced
- [ ] Filters and search work
- [ ] Responsive design works

---

## 🚀 Deployment

### Preparation for Production

#### 1. Security Settings

```python
# settings.py
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

#### 2. Static Files

```bash
# Collect static files
python manage.py collectstatic
```

#### 3. Database Migration

```bash
# For production database
python manage.py migrate --database=production
```

### Deployment Options

#### Option 1: Heroku

```bash
# Install Heroku CLI
# Create Procfile
web: gunicorn todoproject.wsgi

# Create runtime.txt
python-3.12.3

# Deploy
heroku create yourapp
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py create_admin_user
```

#### Option 2: DigitalOcean

1. Create a droplet
2. Install Python, pip, virtualenv
3. Clone repository
4. Set up Gunicorn and Nginx
5. Configure domain and SSL

#### Option 3: PythonAnywhere

1. Upload code
2. Create virtual environment
3. Configure WSGI file
4. Set up static files
5. Run migrations

### Production Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY from environment
- [ ] ALLOWED_HOSTS configured
- [ ] Database backed up
- [ ] Static files collected
- [ ] HTTPS enabled
- [ ] Admin password changed
- [ ] Error logging configured
- [ ] Email backend configured
- [ ] Regular backups scheduled

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Admin Login Not Working

**Problem:** Can't login to admin panel

**Solutions:**
```bash
# Create new admin user
python manage.py create_admin_user

# Verify existing admins
python manage.py verify_admins

# Reset password
python manage.py changepassword admin
```

#### 2. Calendar Not Showing Holidays

**Problem:** Calendar page is empty or holidays missing

**Solutions:**
```bash
# Populate holidays
python manage.py populate_holidays

# Check if holidays exist
python manage.py shell
>>> from todoapp.models import IndianHoliday
>>> IndianHoliday.objects.count()
```

#### 3. Static Files Not Loading

**Problem:** CSS/JS not working, no styling

**Solutions:**
```bash
# Collect static files
python manage.py collectstatic

# Check static file configuration in settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

#### 4. Database Errors

**Problem:** No such table / IntegrityError

**Solutions:**
```bash
# Delete database and start fresh
rm db.sqlite3

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Recreate admin
python manage.py create_admin_user
```

#### 5. Import Errors

**Problem:** ModuleNotFoundError

**Solutions:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt
```

#### 6. Permission Denied Errors

**Problem:** Can't access certain features

**Solutions:**
- Check user role in admin panel
- Ensure UserProfile exists for user
- Run `python manage.py create_profiles`

#### 7. Template Does Not Exist

**Problem:** TemplateDoesNotExist error

**Solutions:**
- Check `TEMPLATES` setting in settings.py
- Ensure templates directory exists
- Verify template path in views

#### 8. Calculator Not Working

**Problem:** Calculator buttons not responding

**Solutions:**
- Check browser console for JavaScript errors
- Ensure Bootstrap JS is loaded
- Clear browser cache

### Getting Help

If you encounter other issues:

1. **Check Django logs**: Terminal where server is running
2. **Enable debug mode**: Set `DEBUG = True` in settings.py
3. **Check documentation**: See other .md files in project
4. **Review code**: Check models.py, views.py for logic
5. **GitHub Issues**: Report bugs and request features

---

## ⚙️ Configuration

### Django Settings

#### Key Settings (todoproject/settings.py)

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Templates
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]

# Login URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

# Security (Development)
DEBUG = True
SECRET_KEY = 'your-secret-key-here'
ALLOWED_HOSTS = []
```

### Environment Variables (Recommended for Production)

Create a `.env` file:
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Custom Management Commands

```bash
# Create admin user
python manage.py create_admin_user

# Verify admins
python manage.py verify_admins

# Create profiles for existing users
python manage.py create_profiles

# Populate holidays
python manage.py populate_holidays

# Change password
python manage.py changepassword username
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/django-todo-app.git
   cd django-todo-app
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clean, readable code
   - Follow Django best practices
   - Add comments where needed
   - Update documentation

4. **Test Your Changes**
   ```bash
   python manage.py test
   python manage.py runserver
   # Manual testing
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   # Create Pull Request on GitHub
   ```

### Contribution Guidelines

#### Code Style

- Follow **PEP 8** for Python code
- Use **4 spaces** for indentation
- Keep lines under **79 characters** where possible
- Use **meaningful variable names**
- Add **docstrings** to functions and classes

#### Commit Message Format

```
Type: Brief description (50 chars or less)

More detailed explanation if needed.
```

**Types:** Add, Fix, Update, Remove, Docs, Style, Refactor, Test

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Use privately

---

## 📞 Contact & Support

### Project Links

- 📦 **Repository**: GitHub repository URL
- 🐛 **Issue Tracker**: Report bugs
- 📖 **Documentation**: See .md files in project root

### Support

If you need help:

1. **Read the Documentation**
   - README.md (this file)
   - QUICKSTART.md
   - ADMIN_GUIDE.md
   - LOGIN_TROUBLESHOOTING.md

2. **Check Existing Issues** on GitHub

3. **Create New Issue** with detailed information

---

## 🙏 Acknowledgments

### Built With

- [Django](https://www.djangoproject.com/) - The web framework
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Font Awesome](https://fontawesome.com/) - Icon library
- [SQLite](https://www.sqlite.org/) - Database engine

### Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python Documentation](https://docs.python.org/)

---

## 📚 Related Documentation

- [QUICKSTART.md](QUICKSTART.md) - Fast setup guide
- [ADMIN_GUIDE.md](ADMIN_GUIDE.md) - Complete admin documentation
- [ADMIN_CHEATSHEET.md](ADMIN_CHEATSHEET.md) - Quick admin reference
- [LOGIN_TROUBLESHOOTING.md](LOGIN_TROUBLESHOOTING.md) - Login issues help

---

## 📝 Changelog

### Version 1.0.0 (2025)

**Initial Release**

✨ **Features:**
- User authentication (login, signup, logout)
- Todo management with status and priority
- Budget tracker with 8 categories
- Calendar with 40+ Indian holidays
- Calculator with keyboard support
- Role-based admin system (4 roles)
- Responsive Bootstrap UI
- SQLite database

🐛 **Bug Fixes:**
- Fixed QuerySet slicing error in home view
- Fixed calendar template filter issue

📖 **Documentation:**
- Comprehensive README
- Admin guides
- Quick start guide
- Troubleshooting guide

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a star! ⭐

Made with ❤️ and Django

**Happy Todo Managing! 🎯**

</div>
