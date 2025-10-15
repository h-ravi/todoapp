# 🚀 Quick Admin Creation Cheat Sheet

## Create New Admins - Copy & Paste Commands

### 1. Interactive Mode (Easiest)
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user
```
Then follow the prompts!

---

## 2. One-Line Commands

### Create Super Admin
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username myadmin --email admin@example.com --password mypassword --role superadmin
```

### Create Regular Admin
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username johndoe --email john@example.com --password john123 --role admin
```

### Create Manager
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username manager1 --email manager@example.com --password manager123 --role manager
```

### Create User
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username user1 --email user@example.com --password user123 --role user
```

---

## 3. Via Django Admin Panel

1. **Go to**: http://127.0.0.1:8000/admin/
2. **Login** with admin credentials
3. Click **"Users"** → **"ADD USER +"**
4. Fill form and select **Role**
5. Click **"SAVE"**

---

## Role Quick Reference

| Role | Code | Access Level |
|------|------|--------------|
| Super Admin | `superadmin` | Full system control |
| Admin | `admin` | Admin panel + data management |
| Manager | `manager` | Limited oversight |
| User | `user` | Regular user |

---

## Update Existing User Role

```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username existing_username --role superadmin
```
Type `yes` when asked to update.

---

## Current System Admins

**Default Super Admin:**
- Username: `admin`
- Email: `admin@admin.com`
- Password: `admin`
- Access: http://127.0.0.1:8000/admin/

**Test Accounts Created:**
- Username: `johndoe`
- Email: `john@example.com`
- Password: `john123`
- Role: Admin

---

## Common Tasks

### Change Password
```bash
/home/r/Python/django/.venv/bin/python manage.py changepassword USERNAME
```

### Create Profiles for Old Users
```bash
/home/r/Python/django/.venv/bin/python manage.py create_profiles
```

### Check All Users
Login to admin panel and click "Users"

---

## Quick Test

**Test the new admin creation:**

1. Create a test admin:
```bash
/home/r/Python/django/.venv/bin/python manage.py create_admin_user --username testadmin --email test@test.com --password test123 --role admin
```

2. Login at: http://127.0.0.1:8000/login/
3. Access admin: http://127.0.0.1:8000/admin/
4. Create a new user from admin panel!

---

**📚 Full Guide**: See ADMIN_GUIDE.md for complete documentation
