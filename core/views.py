from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def manager_dashboard(request):
    return render(request, "dashboards/manager_dashboard.html")


@login_required
def frontdesk_dashboard(request):
    return render(request, "dashboards/frontdesk_dashboard.html")


@login_required
def student_dashboard(request):
    return render(request, "dashboards/student_dashboard.html")