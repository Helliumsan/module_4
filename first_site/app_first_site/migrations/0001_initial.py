    # Generated by Django 4.2.4 on 2023-08-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='текст')),
                ('price', models.FloatField(verbose_name='цена')),
                ('user', models.CharField(max_length=126, verbose_name='пользователь')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата')),
            ],
        ),
    ]
