# Generated by Django 3.1.7 on 2021-04-02 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_carousel_datosduros_lectura'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectura',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
