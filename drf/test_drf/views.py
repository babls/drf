import django_filters.rest_framework
from rest_framework.response import Response
from .models import Question, Answer, Contest
from .serializers import QuestionSerializer, AnswerSerializer, ContestSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView


class QuestionList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
        filter_fields = ['name']
        question_name = self.request.query_params.get('id')
        if question_name:
            queryset = queryset.filter(name=question_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AnswerList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        answer_name = self.request.query_params.get('text')
        if answer_name:
            queryset = queryset.filter(text=answer_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ContestList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ContestSerializer

    def get_queryset(self):
        queryset = Contest.objects.all()
        contest_name = self.request.query_params.get('name')
        if contest_name:
            queryset = queryset.filter(name=contest_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)