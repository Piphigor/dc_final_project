# Generated by Django 4.1.1 on 2022-09-07 04:04
from random import uniform

from django.db import migrations


def populate_test_data(apps, schema_editor):
    Student = apps.get_model('django_dc_final_project', 'Student')
    Subject = apps.get_model('django_dc_final_project', 'Subject')
    Score = apps.get_model('django_dc_final_project', 'Score')

    students = [
        Student(name='Иванов', surname='Иван', email='ivaonv.ivan@iivan.com'),
        Student(name='Иванов', surname='Ибрагим', email='ivaonv.ibrahim@iivan.com'),
        Student(name='Петрова', surname='Екатерина', email='petrova.kate@pkate.com'),
    ]
    Student.objects.bulk_create(students)

    subjects = [
        Subject(name='ТиМП'),
        Subject(name='ЭиС'),
        Subject(name='Философия'),
        Subject(name='Иностранный язык'),
        Subject(name='Физическая культура'),
    ]

    Subject.objects.bulk_create(subjects)

    scores = (
        Score(student=student, subject=subject, value=uniform(0, 5))
        for student in students
        for subject in subjects
    )
    Score.objects.bulk_create(scores)


class Migration(migrations.Migration):

    dependencies = [
        ('django_dc_final_project', '0003_score'),
    ]

    operations = [
        migrations.RunPython(populate_test_data),
    ]
