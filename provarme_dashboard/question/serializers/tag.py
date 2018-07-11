from rest_framework	import serializers

from question.models import Tag


class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ('description', 'tag')