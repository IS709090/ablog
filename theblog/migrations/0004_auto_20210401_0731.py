# Generated by Django 3.1.7 on 2021-04-01 13:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20210401_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
