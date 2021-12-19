from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.course import models as course_models


@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["active_courses"] = course_models.Course.objects.filter(is_active=True).all()
        return kwargs


class Search:
    pass


@method_decorator(login_required, name='dispatch')
class CourseIndex(DetailView):
    template_name = "course/index.html"
    queryset = course_models.Course.objects
    pk_url_kwarg = None
    slug_url_kwarg = "number"
    slug_field = "number"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["exams"] = self.object.exams.order_by('-date')
        return kwargs
