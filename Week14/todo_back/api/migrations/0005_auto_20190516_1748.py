# Generated by Django 2.2 on 2019-05-16 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task_complexity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_on',
        ),
    ]
