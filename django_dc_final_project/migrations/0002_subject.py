# Generated by Django 4.1.1 on 2022-09-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dc_final_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
