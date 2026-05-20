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

	def test_list_todos(self):
		"""This test checks whether we are able to list all items in the database"""
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_retrieve_todo(self):
		"""This test checks whether it is able to retieve one single todo item"""
		response = self.client.get(self.detail_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["title"], "Test todo")

	def test_update_todo(self):
		"""This test checks whether we are able to successfully update a todo item"""
		updated_data = {"title": "Updated title", "description": "Updated description", "is_completed": True}
		response = self.client.put(self.detail_url, updated_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["title"], "Updated title")
		self.assertEqual(response.data["is_completed"], True)

	def test_delete_todo(self):
		"""This test checks whether we are able to succefully delete a todo item"""
		response = self.client.delete(self.detail_url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Todo.objects.count(), 0)

	def test_create_todo_invalid_title(self):
		"""This test checks whether our validators are working and we handle error state of creating an invalid todo with an incomplete title"""
		todo_data = {"title": "Ne", "description": "New description text"}
		response = self.client.post(self.list_url, todo_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Todo.objects.count(), 1)

	def test_create_todo_missing_fields(self):
		"""This test checks whether we handle the error state of adding a todo with missing fields"""
		todo_data = {}
		response = self.client.post(self.list_url, todo_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Todo.objects.count(), 1)

	def test_retrieve_nonexistent_todo(self):
		"""This checks whether we handle the error state of retrieving a nonexistent todo item"""
		url = reverse('todo-detail', kwargs={'pk': 999})
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
