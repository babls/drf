from rest_framework.response import Response
from rest_framework.views import APIView
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


class TestList(APIView):
    def get(self, request):
        contests = Question.objects.all()
        serializer = TestSerializer(contests, many=True)
        return Response(serializer.data)

class AllList(APIView):
    def get(self, request):
        contests = Question.objects.all()
        serializer = AllSerializer(contests, many=True)
        return Response(serializer.data)
