# Generated by Django 3.1.7 on 2021-04-13 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_auto_20210412_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtransversalpost',
            name='optional_author',
        ),
    ]
