from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdminView(admin.ModelAdmin):
    pass
