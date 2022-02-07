from rest_framework import serializers
from .models import Answer, Contest, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    Answer = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'Answer', 'text', 'multiple_answers', 'id_contest')


class AllSerializer(serializers.ModelSerializer):
    Contest = serializers.StringRelatedField(many=True, read_only=True)
    Question = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Contest
        fields = ('id', 'name', 'Contest', 'Question')
