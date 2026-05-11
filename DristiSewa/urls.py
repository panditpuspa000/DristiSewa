from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from core.views import manager_dashboard, frontdesk_dashboard, student_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    # DASHBOARDS (THIS IS THE FIX)
    path('dashboard/manager/', manager_dashboard, name='manager_dashboard'),
    path('dashboard/frontdesk/', frontdesk_dashboard, name='frontdesk_dashboard'),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),

    # HOME
    path('', lambda request: redirect('/accounts/login/')),
]