from rest_framework import serializers
from .models import Todo

"""Serializer for Todo model with title and description validation."""
class TodoSerializer(serializers.ModelSerializer):
	title = serializers.CharField(min_length=3, max_length=100)
	description = serializers.CharField(min_length=3)

	class Meta:
		model = Todo
		fields = ["id", "title", "description", "is_completed", "created_at", "updated_at"]
		read_only_fields = ['id', 'created_at', 'updated_at']
