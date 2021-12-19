from django.contrib import admin
from .models import Course, Exam


@admin.register(Course)
class CourseAdminView(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdminView(admin.ModelAdmin):
    pass
