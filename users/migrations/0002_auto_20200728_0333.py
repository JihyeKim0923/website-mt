# Generated by Django 2.1.7 on 2020-07-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='circles',
        ),
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
    ]