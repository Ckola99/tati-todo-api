from django.db import models

# Todo model representing a single todo item
class Todo(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=False)
	is_completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
