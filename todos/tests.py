from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo

# Create your tests here.
class TodoAPITests(APITestCase):

	def setUp(self):
		"""Runs before every test to create a sample todo"""
		self.todo = Todo.objects.create(
			title="Test todo",
			description="Test description text",
			is_completed=False
		)
		self.list_url = reverse('todo-list')
		self.detail_url = reverse('todo-detail', kwargs={'pk':self.todo.pk})

	def test_create_todo(self):
		"""This test checks whether we can correctly post a todo item"""
		todo_data = {"title": "New todo title", "description": "New description text"}
		response = self.client.post(self.list_url, todo_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Todo.objects.count(), 2)
