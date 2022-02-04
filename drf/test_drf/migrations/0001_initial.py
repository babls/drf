# Generated by Django 3.2.12 on 2022-02-04 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название конкурса')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название вопроса')),
                ('text', models.CharField(max_length=200, verbose_name='Текст вопроса')),
                ('multiple_answers', models.BooleanField(default=False, verbose_name='Несколько ответов у вопроса?')),
                ('id_contest', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Contest', to='test_drf.contest', verbose_name='Конкурс')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст ответа')),
                ('true_answer', models.BooleanField(default=False, verbose_name='Верный вариант ответа?')),
                ('id_questions', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Question', to='test_drf.question', verbose_name='Вопрос')),
            ],
        ),
    ]
