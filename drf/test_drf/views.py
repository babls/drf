from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Answer, Question, Contest
from .serializers import AnswerSerializer, QuestionSerializer, ContestSerializer, TestSerializer, AllSerializer


class AnswerList(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class ContestList(APIView):
    def get(self, request):
        contests = Contest.objects.all()
        serializer = ContestSerializer(contests, many=True)
        return Response(serializer.data)


class TestList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        item_id = self.request.query_params.get('id')
        if item_id:
            queryset = queryset.filter(id_contest=item_id)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AllList(APIView):
    def get(self, request):
        queryset = Contest.objects.all()
        serializer = AllSerializer(queryset, many=True)
        return Response(serializer.data)
