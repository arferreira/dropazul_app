from rest_framework import serializers

from question.models import Alternative


class AlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternative
        fields = '__all__'
