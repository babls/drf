# Generated by Django 3.2.12 on 2022-02-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_drf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='true_answer',
            field=models.BooleanField(default=False, verbose_name='Верный вариант ответа?'),
        ),
    ]
