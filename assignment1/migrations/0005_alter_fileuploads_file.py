# Generated by Django 4.1.6 on 2023-02-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0004_fileuploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploads',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
