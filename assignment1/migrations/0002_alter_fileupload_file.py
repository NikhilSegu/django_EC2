# Generated by Django 4.1.6 on 2023-02-03 03:50

import assignment1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to=assignment1.models.userDirectoryPath),
        ),
    ]
