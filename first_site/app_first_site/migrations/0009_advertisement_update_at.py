# Generated by Django 4.2.4 on 2023-08-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_first_site', '0008_remove_advertisement_create_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
