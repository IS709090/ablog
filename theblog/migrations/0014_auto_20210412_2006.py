# Generated by Django 3.1.7 on 2021-04-13 01:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtransversalpost',
            name='author',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nombre Completo', 'Nombre Completo'), ('Nombre Completo3', 'Nombre Completo3'), ('Holaaa', 'Holaaa'), ('Nombre Completo4', 'Nombre Completo4')], max_length=5600),
        ),
        migrations.AlterField(
            model_name='event',
            name='author',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nombre Completo', 'Nombre Completo'), ('Nombre Completo3', 'Nombre Completo3'), ('Holaaa', 'Holaaa'), ('Nombre Completo4', 'Nombre Completo4')], max_length=5600),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nombre Completo', 'Nombre Completo'), ('Nombre Completo3', 'Nombre Completo3'), ('Holaaa', 'Holaaa'), ('Nombre Completo4', 'Nombre Completo4')], max_length=5600),
        ),
    ]
