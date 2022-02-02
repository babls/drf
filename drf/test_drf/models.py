from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название конкурса')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название вопроса')
    text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    id_contest = models.ForeignKey('Contest', default=None, null=True, on_delete=models.CASCADE, related_name='Contest', verbose_name='Конкурс')
    multiple_answers = models.BooleanField(default=False, verbose_name='Несколько ответов у вопроса?')

    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст ответа')
    id_questions = models.ForeignKey('Question', default=None, null=True, on_delete=models.CASCADE, related_name='Question', verbose_name='Вопрос')
    true_answer = models.BooleanField(default=False, verbose_name='Верный вариант ответа?')

    def __str__(self):
        return self.text
