from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

User = get_user_model()


# -------------------
# LOGIN VIEW (EMAIL + ROLE BASED)
# -------------------
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate using email (USERNAME_FIELD = email)
        user = authenticate(request, username=email, password=password)

        # Check user + active status
        if user is not None and user.is_active:
            login(request, user)

            role = user.role

            # ROLE-BASED REDIRECT (CLEAN PHASE 2 ARCHITECTURE)
            if role == "ADMIN":
                return redirect("/admin/")
            elif role == "MANAGER":
                return redirect("/accounts/manager/dashboard/")
            elif role == "FRONTDESK":
                return redirect("/accounts/frontdesk/dashboard/")
            elif role == "STUDENT":
                return redirect("/accounts/student/dashboard/")
            else:
                return render(request, "accounts/login.html", {
                    "error": "Invalid role assigned in database"
                })

        # authentication failed
        return render(request, "accounts/login.html", {
            "error": "Invalid email or password"
        })

    return render(request, "accounts/login.html")


# -------------------
# REGISTER VIEW
# -------------------
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # prevent duplicate email
        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {
                "error": "Email already exists"
            })

        # create user (default role = STUDENT)
        User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="STUDENT"
        )

        return redirect("login")

    return render(request, "accounts/register.html")


# -------------------
# LOGOUT VIEW
# -------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# -------------------
# DASHBOARDS (ROLE PROTECTION)
# -------------------
@login_required
def student_dashboard(request):
    if request.user.role != "STUDENT":
        return HttpResponseForbidden("Access Denied")
    return render(request, "dashboards/student_dashboard.html")


@login_required
def manager_dashboard(request):
    if request.user.role != "MANAGER":
        return HttpResponseForbidden("Access Denied")
    return render(request, "dashboards/manager_dashboard.html")


@login_required
def frontdesk_dashboard(request):
    if request.user.role != "FRONTDESK":
        return HttpResponseForbidden("Access Denied")
    return render(request, "dashboards/frontdesk_dashboard.html")