# Generated by Django 4.2.4 on 2023-08-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_first_site', '0010_alter_advertisement_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.CharField(default='', max_length=64, verbose_name='автор'),
        ),
    ]
