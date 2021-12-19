from django.urls import path, include


urlpatterns = [
    path('course/', include("apps.course.urls")),
]
