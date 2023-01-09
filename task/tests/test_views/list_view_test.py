from django.test import Client, TestCase
from django.urls import reverse

from task.models import Task


class ListTestViews(TestCase):
    client = None
    
    def setUp(self):
        self.client = Client()
        self.task_list_url = reverse('task_list')
        
        for n in range(100):
            test_task = Task.objects.create(title=f"Test task {n}")
            test_task.save()


    def test_todo_list_GET(self):
        """Should return task list"""
        
        response = self.client.get(self.task_list_url)
        
        expected_task_list = Task.objects.all()[:25]

        self.assertEqual(response.status_code, 200)
        
        self.assertDictEqual( {
            'data': {
                'item_list': [{
                    'id': task.id,
                    'title': task.title,
                    'is_done': task.is_done,
                    'user__username': task.user.username,
                    'created_at': task.created_at,
                    'updated_at': task.updated_at,
                } for task in expected_task_list],
                'total_count': 100,
            },
            'error': None,
        } )