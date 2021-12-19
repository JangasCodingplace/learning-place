from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path(
        'auth/',
        LoginView.as_view(
            template_name="auth/index.html",
        ),
        name="auth"
    ),
    path(
        '',
        views.Dashboard.as_view(),
        name="dashboard"
    ),
    path(
        'course/<number>',
        views.CourseIndex.as_view(),
        name="course_index"
    )
]
