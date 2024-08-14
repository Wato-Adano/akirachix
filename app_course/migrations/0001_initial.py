# Generated by Django 5.0.6 on 2024-07-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.SmallIntegerField()),
                ('department', models.CharField(max_length=20)),
                ('course_discription', models.TextField()),
                ('class_starting_time', models.TimeField(auto_now=0, verbose_name=0)),
                ('course_instructor', models.CharField(max_length=28)),
                ('number_of_students', models.PositiveSmallIntegerField()),
                ('grade_level', models.PositiveSmallIntegerField()),
                ('school_term', models.IntegerField()),
                ('assement_requirements', models.TextField()),
                ('course_trainer_name', models.CharField(max_length=20)),
            ],
        ),
    ]
