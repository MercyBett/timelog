import datetime
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from freezegun import freeze_time
from users.models import User
from project.models import Project
from .models import ProjectTracker


@freeze_time("2022-9-24 01:02:03")
class ProjectTrackerTests(APITestCase):

    client = APIClient()
    tracker_entry = None

    def setUp(self) -> None:
        self.user = self.create_user()
        self.project = self.create_project()
        self.project.assigned_to.add(self.user)
        self.client.force_authenticate(user=self.user)
        return super().setUp()
    def tearDown(self):
      pass

    def create_project(self):
        title = 'DRF takehome'
        deadline = datetime.date(2022, 10, 1)
        data = {
            'title': title,
            'deadline': deadline,
        }
        return Project.objects.create(**data)

    def create_user(self):
        name = 'test_user'
        email = 'test_user@gmail.com'
        password = '#test@1234#'

        data = {'name': name,
                'email': email,
                'password': password,

                }
        return User.objects.create_user(**data)

    def create_tracker_entry(self):
        start_time = timezone.now()
        return ProjectTracker.objects.create(user=self.user, project=self.project, start_time=start_time)

    def test_create_tracker_entry_without_api(self):

        self.tracker_entry = self.create_tracker_entry()
        self.assertEqual(ProjectTracker.objects.count(), 1)
        self.assertEqual(self.tracker_entry.user.name, 'test_user')
        self.assertEqual(self.tracker_entry.start_time,
                         timezone.now())


    def test_create_tracker_entry_with_api(self):

        url = 'http://127.0.0.1:8000/api/projectTrackers/'
        start_time = timezone.now()

        data = {
            'user': self.user.id,
            'project': self.project.id,
            'start_time': start_time
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.tracker_entry = response.json()
        self.assertEqual(ProjectTracker.objects.count(), 1)
        self.assertEqual(
            self.tracker_entry['project']['title'], 'DRF takehome')
        deadline = datetime.strptime(
            self.tracker_entry['project']['deadline'], '%Y-%m-%d').date()
        self.assertEqual(deadline,
                         datetime.date(2022, 10, 1))
        self.assertEqual(ProjectTracker.objects.count(), 1)
        self.assertEqual(self.tracker_entry['user']['name'], 'test_user')
        self.assertEqual(
            self.tracker_entry['start_time'], '2022-9-24T01:02:03Z')
        self.assertTrue(self.tracker_entry['is_paused'])

    def test_delete_tracker_entry(self):

        self.tracker_entry = self.create_tracker_entry()
        self.assertEqual(ProjectTracker.objects.count(), 1)
        self.tracker_entry.delete()
        self.assertEqual(ProjectTracker.objects.count(), 0)

