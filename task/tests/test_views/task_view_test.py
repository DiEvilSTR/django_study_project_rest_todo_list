from django.test import Client, TestCase

from task.models import Task

class TaskTestCase(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

        test_task = Task.objects.create(title="Test task", description="Test task desc")
        test_task.save()

        self.task_pk = test_task.id

    def test_get_task(self):
        """Should return task data"""

        path = f'/task/{self.task_pk}'
        query_string = {'username': 'john', 'password': 'smith'}
        response_data = self.client.get(path, query_string)
        
        self.assertDictEqual(response_data, {
            'id': self.task_pk,
            'title': 'Test task',
            'description': 'Test task desc',
            'is_done': False,
            'user__username': 'Test username',
            # 'created_at': self.assertIsNotNone(),
            # 'updated_at': '',
        })