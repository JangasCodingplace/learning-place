# Generated by Django 4.0 on 2021-12-19 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transfer', models.ManyToManyField(related_name='course_references', to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('def', 'Definition'), ('l', 'Lemma'), ('p', 'Proposition'), ('s', 'Sentence')], max_length=3)),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('unit', models.SmallIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('calculated_references', models.ManyToManyField(related_name='calculated_wiki_references', to='course.Wiki')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wiki_units', to='course.course')),
                ('transfer', models.ManyToManyField(related_name='wiki_references', to='course.Wiki')),
            ],
            options={
                'unique_together': {('type', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('wb', 'Workbook'), ('sub', 'Submition'), ('uc', 'Unit Closing')], max_length=3)),
                ('body', models.TextField()),
                ('solution', models.TextField()),
                ('unit', models.SmallIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('all_wiki_references', models.ManyToManyField(related_name='all_submissions', to='course.Wiki')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='course.course')),
                ('direct_wiki_references', models.ManyToManyField(related_name='submissions', to='course.Wiki')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('passed', models.BooleanField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='course.course')),
            ],
        ),
    ]
