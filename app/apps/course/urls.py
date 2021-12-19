from django.urls import path
from . import api


urlpatterns = [
    path(
        'wiki-detail/<pk>',
        api.RetrieveWikiDetailApi.as_view(),
        name="course_wiki_detail"
    ),
]
