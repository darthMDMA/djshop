# Generated by Django 4.1.5 on 2023-02-20 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='discussions',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reply',
        ),
    ]
