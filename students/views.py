from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Student
from core.services import filter_by_branch


@login_required
def student_list(request):
    queryset = Student.objects.all()

    students = filter_by_branch(request.user, queryset)

    return render(request, "students/student_list.html", {
        "students": students
    })