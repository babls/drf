# Generated by Django 3.2.12 on 2022-02-07 11:37

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_drf', '0003_auto_20220207_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='id_answer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.fields.CharField, related_name='UserAnswerAnswers', to='test_drf.answer', verbose_name='Ответ'),
        ),
    ]
