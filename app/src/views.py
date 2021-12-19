from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.course import models as course_models
from apps.course import documents as course_documents


@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["active_courses"] = course_models.Course.objects.filter(is_active=True).all()
        return kwargs


@method_decorator(login_required, name='dispatch')
class CourseBaseView(DetailView):
    queryset = course_models.Course.objects
    pk_url_kwarg = None
    slug_url_kwarg = "number"
    slug_field = "number"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["course_view"] = self.object
        return kwargs


class CourseIndex(CourseBaseView):
    template_name = "course/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["exams"] = self.object.exams.order_by('-date')
        return kwargs


class CourseSearch(CourseBaseView):
    template_name = "course/search/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        q = self.request.GET.get("q")
        if q is not None:
            title_match = list(
                course_documents.WikiDocument.search().query("match", synonyms=q)
            )
            if len(title_match) > 0:
                title_match_ids = [match.id for match in title_match]
                kwargs["title_match"] = title_match

            body_match = list(
                course_documents.WikiDocument.search().query("match", body=q)
            )
            if len(body_match) > 0:
                filtered_body_matches = [
                    match for match in body_match if match.id not in title_match_ids
                ]
                if filtered_body_matches:
                    kwargs["body_match"] = filtered_body_matches
        return kwargs
