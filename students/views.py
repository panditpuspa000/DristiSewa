from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Student
from core.services import filter_by_branch


@login_required
def student_list(request):
    students = filter_by_branch(request.user, Student.objects.all())

    return render(request, "students/student_list.html", {
        "students": students
    })