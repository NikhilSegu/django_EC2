# Generated by Django 4.1.6 on 2023-02-03 04:26

import assignment1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0003_alter_fileupload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=assignment1.models.userDirectoryPath)),
            ],
        ),
    ]
