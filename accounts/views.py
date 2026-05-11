from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):

    if request.method == "POST":

        role = request.POST.get("role")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "MANAGER":
                return redirect("manager_dashboard")

            elif user.role == "FRONTDESK":
                return redirect("frontdesk_dashboard")

            elif user.role == "STUDENT":
                return redirect("student_dashboard")

            elif user.role == "ADMIN":
                return redirect("/admin/")

        return render(request, "accounts/login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def manager_dashboard(request):
    return render(request, "dashboards/manager_dashboard.html")


def frontdesk_dashboard(request):
    return render(request, "dashboards/frontdesk_dashboard.html")


def student_dashboard(request):
    return render(request, "dashboards/student_dashboard.html")