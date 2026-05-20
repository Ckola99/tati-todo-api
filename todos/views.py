from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
import logging

logger = logging.getLogger(__name__)

"""ViewSet providing CRUD operations for Todo items with logging."""
class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	def create(self, request, *args, **kwargs):
		try:
			response = super().create(request, *args, **kwargs)
			logger.info(f"Todo created with id:{response.data['id']}")
			return response
		except Exception as e:
			logger.error(f"Failed to create todo item: {e}")
			raise

	def update(self, request, *args, **kwargs):
		todo_id = kwargs.get('pk')
		try:
			response = super().update(request, *args, **kwargs)
			logger.info(f"Todo with id:{response.data['id']} updated")
			return response
		except Exception as e:
			logger.error(f"Failed to update todo item with id:{todo_id}: {e}")
			raise

	def destroy(self, request, *args, **kwargs):
		todo_id = kwargs.get('pk')
		try:
			response = super().destroy(request, *args, **kwargs)
			logger.info(f"Todo with id:{todo_id} deleted")
			return response
		except Exception as e:
			logger.error(f"Failed to delete todo item with id:{todo_id}: {e}")
			raise
