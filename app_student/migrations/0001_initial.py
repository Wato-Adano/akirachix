# Generated by Django 5.0.6 on 2024-07-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('student_code', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=28)),
                ('gender', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('id_number', models.SmallIntegerField()),
                ('grade_level', models.IntegerField()),
                ('gurdian_name', models.CharField(max_length=28)),
                ('student_next_of_kin', models.CharField(max_length=20)),
                ('student_national_id_number', models.CharField(max_length=30)),
            ],
        ),
    ]