# Generated by Django 3.1.7 on 2021-04-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_auto_20210401_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
