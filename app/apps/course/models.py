from django.db import models


WIKI_TYPE_CHOICES = (
    ('def', 'Definition'),
    ('l', 'Lemma'),
    ('p', 'Proposition'),
    ('s', 'Sentence')
)


SUBMISSION_CHOICES = (
    ('wb', 'Workbook'),
    ('sub', 'Submition'),
    ('uc', 'Unit Closing'),
)


class Course(models.Model):
    title = models.CharField(
        max_length=120,
        unique=True
    )
    number = models.CharField(
        unique=True,
        max_length=10
    )
    transfer = models.ManyToManyField(
        to="Course",
        related_name="course_references",
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


class Wiki(models.Model):
    type = models.CharField(
        choices=WIKI_TYPE_CHOICES,
        max_length=3
    )
    title = models.CharField(
        max_length=120
    )
    body = models.TextField()
    transfer = models.ManyToManyField(
        to="Wiki",
        related_name="wiki_references",
        blank=True
    )
    unit = models.SmallIntegerField(
        null=True,
        blank=True
    )
    calculated_references = models.ManyToManyField(
        to="Wiki",
        related_name="calculated_wiki_references",
        blank=True
    )
    course = models.ForeignKey(
        to=Course,
        related_name="wiki_units",
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("type", "title", )

    def __str__(self):
        return self.title


class Submission(models.Model):
    type = models.CharField(
        max_length=3,
        choices=SUBMISSION_CHOICES
    )
    body = models.TextField()
    solution = models.TextField()
    direct_wiki_references = models.ManyToManyField(
        to=Wiki,
        related_name="submissions",
        blank=True
    )
    course = models.ForeignKey(
        to=Course,
        related_name="submissions",
        on_delete=models.PROTECT
    )
    all_wiki_references = models.ManyToManyField(
        to=Wiki,
        related_name="all_submissions",
        blank=True
    )
    unit = models.SmallIntegerField(
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )


class Exam(models.Model):
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name="exams"
    )
    date = models.DateTimeField()
    passed = models.BooleanField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.course.title
