# Generated by Django 4.1.7 on 2023-03-02 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SignopediaEntry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
