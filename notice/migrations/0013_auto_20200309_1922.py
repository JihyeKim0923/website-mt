# Generated by Django 3.0.2 on 2020-03-09 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0012_auto_20200309_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='files',
            new_name='upload_images',
        ),
    ]