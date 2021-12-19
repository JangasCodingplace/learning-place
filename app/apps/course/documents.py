from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django.conf import settings
from .models import Wiki, Course


@registry.register_document
class WikiDocument(Document):
    course = fields.ObjectField(
        properties={
            'title': fields.TextField(),
            'number': fields.TextField(),
            'is_active': fields.BooleanField()
        }
    )

    class Index:
        name = "wiki-dev" if settings.DEBUG else "wiki-prod"

        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Wiki
        fields = ["type", "title", "body", "unit", "synonyms", "timestamp", ]
        related_models = [Course, ]
