# Generated by Django 2.2 on 2019-05-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190430_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complexity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
