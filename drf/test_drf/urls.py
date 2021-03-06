from django.urls import path
from .views import AnswerList, QuestionList, ContestList, TestList, AllList

urlpatterns = [
    path('answer/', AnswerList.as_view(), name='answer_list'),
    path('question/', QuestionList.as_view(), name='question_list'),
    path('contest/', ContestList.as_view(), name='contest_list'),
    path('test/', TestList.as_view(), name='test_list'),
    path('all/', AllList.as_view(), name='all_list'),
]
