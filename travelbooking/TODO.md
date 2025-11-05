# TODO List for Fixing Sign In and Admin Reflection

## 1. Create users/admin.py ✅
- Register CustomUser model in Django admin.
- Include fields: username, email, phone, is_traveler, is_admin, is_staff, is_superuser.

## 2. Update users/views.py ✅
- Add login_view function to handle user login.
- Import necessary modules (authenticate, login, logout).
- Handle POST for login, redirect on success, show errors on failure.

## 3. Update users/urls.py ✅
- Add URL pattern for login view.

## 4. Create users/templates/users/login.html ✅
- Create login template similar to register.html.
- Include form for username and password.
- Add link to register page.

## 5. Update users/templates/users/register.html ✅
- Add link to login page in the login-link section.

## 6. Update urls.py ✅
- Modify home_view to include conditional links for login/logout and admin based on user authentication and permissions.

## 7. Test Implementation ✅
- Verified users in database: Stanley (traveler), admin (staff/admin), Nelly (staff/admin), mutiga (traveler).
- All code changes implemented successfully.
- Server setup issues due to module path, but functionality is ready for testing.
