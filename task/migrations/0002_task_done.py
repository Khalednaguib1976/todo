# Generated by Django 3.0.4 on 2020-10-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Done',
            field=models.BooleanField(default=False),
        ),
    ]
