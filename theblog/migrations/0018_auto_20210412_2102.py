# Generated by Django 3.1.7 on 2021-04-13 02:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_remove_blogtransversalpost_optional_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtransversalpost',
            name='optional_author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
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