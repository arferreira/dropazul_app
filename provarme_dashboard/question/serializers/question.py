from rest_framework import serializers

from question.models import Question, UserAnswer
from question.serializers.alternative import AlternativeSerializer


class QuestionSerializer(serializers.ModelSerializer):
    alternatives = AlternativeSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnswer
        fields = '__all__'
