# 🔐 Admin & User Management Guide

## User Roles & Permissions

### Role Hierarchy

1. **Super Admin** (superadmin)
   - ✅ Full system control
   - ✅ Can create/edit/delete ANY user
   - ✅ Can change user roles
   - ✅ Access to Django admin panel
   - ✅ All permissions across the system
   - ✅ Can manage holidays, budgets, todos for all users

2. **Admin** (admin)
   - ✅ Can manage all users and data
   - ✅ Access to Django admin panel
   - ✅ Can create/edit/delete todos and budgets
   - ✅ Can view all user activities
   - ❌ Cannot delete Super Admins

3. **Manager** (manager)
   - ✅ Can view user reports
   - ✅ Can manage assigned users
   - ✅ Limited admin access
   - ❌ Cannot access Django admin panel (by default)
   - ❌ Cannot modify other users' data

4. **User** (user)
   - ✅ Regular user access
   - ✅ Can manage own todos and budgets
   - ✅ Can use calculator and calendar
   - ❌ No admin panel access
   - ❌ Cannot view other users' data

---

## 🚀 How to Create New Admin Users

### Method 1: Interactive Command (Recommended)

Run this command in terminal:

```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user
```

**You'll be prompted to enter:**
- Username
- Email
- Password
- Role (choose from: user, manager, admin, superadmin)

**Example Session:**
```
Enter username: john_admin
Enter email: john@example.com
Enter password: securepass123

Available roles:
1. user - Regular user (no admin access)
2. manager - Can manage users and view reports
3. admin - Full admin access (can manage all data)
4. superadmin - Super Admin (full system control)

Select role (1-4) or type role name [default: admin]: 4

============================================================
User created successfully!
============================================================
Username: john_admin
Email: john@example.com
Password: securepass123
Role: SUPERADMIN
Staff Status: True
Superuser Status: True
============================================================

Role Permissions:
✓ Full system control
✓ Can create/edit/delete any user
✓ Access to admin panel
✓ All admin features

Login at: http://127.0.0.1:8000/login/
Admin panel: http://127.0.0.1:8000/admin/
```

### Method 2: Command Line Arguments

```bash
# Create Super Admin
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username superadmin \
  --email super@admin.com \
  --password admin123 \
  --role superadmin

# Create Admin
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username admin2 \
  --email admin2@example.com \
  --password admin123 \
  --role admin

# Create Manager
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username manager1 \
  --email manager@example.com \
  --password manager123 \
  --role manager

# Create Regular User
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username user1 \
  --email user1@example.com \
  --password user123 \
  --role user
```

---

## 👥 How to Add Users via Admin Panel

### Step 1: Login to Admin Panel

1. Go to: `http://127.0.0.1:8000/admin/`
2. Login with Super Admin credentials:
   - Username: `admin`
   - Password: `admin`

### Step 2: Add New User

1. Click on **"Users"** in the left sidebar
2. Click **"ADD USER +"** button (top right)
3. Fill in the form:
   - **Username**: Enter unique username
   - **Email**: Enter valid email address
   - **First name**: Optional
   - **Last name**: Optional
   - **Password1**: Enter secure password
   - **Password2**: Confirm password
   - **Role**: Select from dropdown:
     - User
     - Manager
     - Admin
     - Super Admin
4. Click **"SAVE"** button

### Step 3: View User Details

After creating, you'll see:
- User's basic information
- Profile information (role, phone, address)
- Permissions (staff status, superuser status)
- Groups and permissions

---

## 🔧 Managing Existing Users

### View All Users

1. Login to admin panel: `http://127.0.0.1:8000/admin/`
2. Click **"Users"** in sidebar
3. You'll see list of all users with:
   - Username
   - Email
   - Role
   - Name
   - Staff status
   - Superuser status
   - Active status
   - Join date

### Edit User Role

**Method 1: Via User List**
1. Go to Users list
2. Find the user
3. Click on username to edit
4. Scroll to **"Profile"** section
5. Change **"Role"** dropdown
6. Click **"SAVE"**

**Method 2: Via Command Line**
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username existing_user \
  --role admin
```
When prompted, type `yes` to update the role.

### Delete User

1. Go to Users list
2. Check the checkbox next to user(s) to delete
3. Select **"Delete selected users"** from action dropdown
4. Click **"Go"** button
5. Confirm deletion

⚠️ **Warning**: Deleting a user will also delete all their todos and budgets!

---

## 📊 Admin Panel Features

### Dashboard Overview

Access: `http://127.0.0.1:8000/admin/`

**Available Sections:**
- **Users**: Manage all user accounts
- **User Profiles**: Manage roles and contact info
- **Todos**: View and manage all todos
- **Budgets**: View and manage all budget entries
- **Indian Holidays**: Add/edit/delete holidays
- **Groups**: Create user groups (optional)
- **Permissions**: Fine-grained permission control

### Managing Todos (Admin View)

1. Click **"Todos"** in admin panel
2. You can:
   - View all todos from all users
   - Filter by user, status, priority, date
   - Search by title, description, username
   - Edit status and priority inline
   - Click on todo to edit details
   - Delete todos
   - See user's role alongside todo

**Quick Edit:**
- Change **Status** or **Priority** directly in list
- Click **"SAVE"** button at bottom

### Managing Budgets (Admin View)

1. Click **"Budgets"** in admin panel
2. You can:
   - View all budget entries from all users
   - Filter by type, category, date, user
   - Search by description, username
   - Edit type, category, amount inline
   - See user's role alongside budget
   - Export data

### Managing Holidays

1. Click **"Indian Holidays"** in admin panel
2. You can:
   - Add new holidays
   - Edit existing holidays
   - Mark as national holiday
   - Filter by year
   - Delete holidays

**Add New Holiday:**
1. Click **"ADD INDIAN HOLIDAY +"**
2. Fill in:
   - Name (e.g., "Diwali")
   - Date
   - Description
   - Is National (checkbox)
   - Year
3. Click **"SAVE"**

---

## 🔐 Permission Matrix

| Feature | User | Manager | Admin | Super Admin |
|---------|------|---------|-------|-------------|
| Login/Signup | ✅ | ✅ | ✅ | ✅ |
| Own Todos | ✅ | ✅ | ✅ | ✅ |
| Own Budget | ✅ | ✅ | ✅ | ✅ |
| Calendar | ✅ | ✅ | ✅ | ✅ |
| Calculator | ✅ | ✅ | ✅ | ✅ |
| View Other Users | ❌ | ⚠️ Limited | ✅ | ✅ |
| Admin Panel | ❌ | ❌ | ✅ | ✅ |
| Manage All Todos | ❌ | ❌ | ✅ | ✅ |
| Manage All Budgets | ❌ | ❌ | ✅ | ✅ |
| Add/Delete Users | ❌ | ❌ | ⚠️ Limited | ✅ |
| Change User Roles | ❌ | ❌ | ❌ | ✅ |
| Manage Holidays | ❌ | ❌ | ✅ | ✅ |
| System Settings | ❌ | ❌ | ❌ | ✅ |

---

## 📱 Testing Different Roles

### Test Super Admin
```bash
# Create a test super admin
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username testsuperadmin \
  --email test@superadmin.com \
  --password test123 \
  --role superadmin
```
Login at: `http://127.0.0.1:8000/login/`
- Can access everything
- Can create/edit/delete all users
- Full admin panel access

### Test Admin
```bash
# Create a test admin
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username testadmin \
  --email test@admin.com \
  --password test123 \
  --role admin
```
Login at: `http://127.0.0.1:8000/login/`
- Can access admin panel
- Can manage todos and budgets
- Cannot change super admin roles

### Test Manager
```bash
# Create a test manager
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username testmanager \
  --email test@manager.com \
  --password test123 \
  --role manager
```
Login at: `http://127.0.0.1:8000/login/`
- Regular user interface
- Future: Custom manager dashboard

### Test Regular User
```bash
# Create a test user
/home/r/Python/django/.venv/bin/python manage.py create_admin_user \
  --username testuser \
  --email test@user.com \
  --password test123 \
  --role user
```
Login at: `http://127.0.0.1:8000/login/`
- Standard features only
- Own todos and budgets
- No admin access

---

## 🔄 Updating Existing Admin

The default admin account was created with:
- Username: `admin`
- Email: `admin@admin.com`
- Password: `admin`

To update this to Super Admin role:
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user
```
Enter username: `admin`
When prompted, type `yes` to update the role to `superadmin`

---

## 📝 Best Practices

### For Super Admins
1. ✅ Use strong passwords
2. ✅ Limit number of super admins (1-2 max)
3. ✅ Regularly audit user accounts
4. ✅ Remove inactive users
5. ✅ Monitor admin panel logs

### For Admins
1. ✅ Don't share admin credentials
2. ✅ Log out after admin tasks
3. ✅ Be careful when deleting data
4. ✅ Verify user emails before creating
5. ✅ Document changes in admin notes

### Security Tips
1. 🔒 Change default admin password
2. 🔒 Use unique passwords for each admin
3. 🔒 Enable two-factor auth (future feature)
4. 🔒 Regular backups of database
5. 🔒 Monitor login attempts

---

## 🆘 Troubleshooting

### "User already exists"
If you try to create a user that exists:
- Command will ask if you want to update the role
- Type `yes` to update, `no` to cancel

### "Cannot access admin panel"
Check:
1. User has `admin` or `superadmin` role
2. User has `is_staff = True`
3. Clear browser cache
4. Try incognito/private window

### "Profile does not exist"
Run this command to create missing profiles:
```bash
/home/r/Python/django/.venv/bin/python manage.py create_profiles
```

### Reset Admin Password
```bash
/home/r/Python/django/.venv/bin/python manage.py changepassword admin
```

---

## 📚 Quick Reference Commands

```bash
# Create new admin user (interactive)
python manage.py create_admin_user

# Create specific role user
python manage.py create_admin_user --username USER --email EMAIL --password PASS --role ROLE

# Create profiles for existing users
python manage.py create_profiles

# Change password
python manage.py changepassword USERNAME

# Run server
python manage.py runserver

# Access admin panel
http://127.0.0.1:8000/admin/
```

---

## 🎯 Summary

✅ **Super Admin**: Full control, use sparingly  
✅ **Admin**: Day-to-day management, trusted users  
✅ **Manager**: Limited oversight (future enhancements)  
✅ **User**: Regular application users  

**Remember**: With great power comes great responsibility! 🦸‍♂️

---

**Need Help?** Check README.md for more documentation.
