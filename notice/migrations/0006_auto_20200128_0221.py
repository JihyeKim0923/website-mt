# Generated by Django 3.0.2 on 2020-01-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20200127_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='파일'),
        ),
    ]
