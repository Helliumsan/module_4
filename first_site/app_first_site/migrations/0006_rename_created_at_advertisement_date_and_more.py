# Generated by Django 4.2.4 on 2023-08-18 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_first_site', '0005_alter_advertisement_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='updated_at',
        ),
    ]
