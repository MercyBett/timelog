
from rest_framework.test import APITestCase, APIClient
from freezegun import freeze_time
import datetime
from .models import User
from .models import Project


@freeze_time("2022-09-24")
class ProjectTests(APITestCase):

    client = APIClient()

    def setUp(self) -> None:
        self.user = self.create_user()
        self.client.force_authenticate(user=self.user)
        self.project = None
        return super().setUp()
    def tearDown(self) -> None:
      pass

    title = 'DRF takehome'
    deadline = datetime.date(2022, 10, 1)
    data = {
        'title': title,
        'deadline': deadline,
    }

    def create_user(self):
        name = 'test_user'
        email = 'test_user@gmail.com'
        password = '#test@1234#'
        data = {'name': name,
                'email': email,
                'password': password,
                }
        return User.objects.create_user(**data)

    def create_project(self):
        project = Project.objects.create(**self.data)
        project.assigned_to.add(self.user)
        return project

    def test_create_project_without_api(self):

        self.project = self.create_project()
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project.title, 'DRF takehome')
        self.assertEqual(self.project.deadline,
                         datetime.date(2022, 10, 1))
        self.assertFalse(self.project.is_deadline)
        self.assertEqual(self.project.time_to_complete, 7)

    def test_create_project_with_api(self):

        url = 'http://127.0.0.1:8000/api/projects/'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.project = response.data
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project['title'], 'DRF takehome')
        self.assertEqual(self.project['slug'], 'drf-takehome')
        deadline = datetime.strptime(self.project['deadline'], '%Y-%m-%d').date()
        self.assertEqual(deadline,
                         datetime.date(2022, 10, 1))
        self.assertFalse(self.project['is_deadline'])
        self.assertEqual(self.project['time_to_complete'], 7)

    def test_delete_project(self):

        self.project = self.create_project()
        self.assertEqual(Project.objects.count(), 1)
        self.project.delete()
        self.assertEqual(Project.objects.count(), 0)
