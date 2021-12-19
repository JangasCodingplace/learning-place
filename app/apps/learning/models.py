from django.db import models
from apps.course import models as course_models


BOX_ELEMENT_TYPE_CHOICES = (
    ("w", "Wiki"),
    ("s", "Submission"),
)


class Box(models.Model):
    title = models.CharField(
        max_length=80
    )
    course = models.ForeignKey(
        to=course_models.Course,
        related_name="boxes",
        on_delete=models.PROTECT
    )
    description = models.TextField(
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class BoxElement(models.Model):
    box = models.ForeignKey(
        to=Box,
        on_delete=models.PROTECT,
        related_name="elements"
    )
    type = models.CharField(
        max_length=3,
        choices=BOX_ELEMENT_TYPE_CHOICES
    )
    wiki = models.ForeignKey(
        to=course_models.Wiki,
        related_name="in_boxes",
        on_delete=models.PROTECT
    )
    submission = models.ForeignKey(
        to=course_models.Submission,
        related_name="in_boxes",
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )


class BoxElementActivity(models.Model):
    element = models.ForeignKey(
        to=BoxElement,
        related_name="activities",
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    correct_answer = models.BooleanField()


class ShortTermUnit(models.Model):
    course = models.ForeignKey(
        to=course_models.Course,
        related_name="short_term_units",
        on_delete=models.PROTECT
    )
    type = models.CharField(
        max_length=3,
        choices=BOX_ELEMENT_TYPE_CHOICES
    )
    wiki = models.ForeignKey(
        to=course_models.Wiki,
        related_name="short_term_units",
        on_delete=models.PROTECT
    )
    submission = models.ForeignKey(
        to=course_models.Submission,
        related_name="short_term_units",
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )


class ShortTermUnitActivity(models.Model):
    unit = models.ForeignKey(
        to=ShortTermUnit,
        related_name="activities",
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    correct_answer = models.BooleanField()
