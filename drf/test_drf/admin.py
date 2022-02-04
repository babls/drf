from django.contrib import admin
from .models import Contest, Question, Answer


class ContestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['text', 'id_contest']


class AnswersAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'id_questions', 'true_answer']


admin.site.register(Contest, ContestAdmin)
admin.site.register(Question, QuestionsAdmin)
admin.site.register(Answer, AnswersAdmin)
