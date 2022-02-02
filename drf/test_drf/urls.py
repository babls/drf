from django.urls import path
from .views import AnswerList, QuestionList, ContestList

urlpatterns = [
    path('answer/', AnswerList.as_view(), name='answer_list'),
    path('question/', QuestionList.as_view(), name='question_list'),
    path('contest/', ContestList.as_view(), name='contest_list')
]
