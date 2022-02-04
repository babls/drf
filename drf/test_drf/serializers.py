from rest_framework import serializers
from .models import Answer, Contest, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = 'name'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    Question = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'Question', 'text')


class AllSerializer(serializers.ModelSerializer):
    all_questions = TestSerializer(many=True, read_only=True)

    class Meta:
        model = Contest
        fields = ('all_questions.id', 'all_questions.name', 'all_questions.Question', 'all_questions.text')
