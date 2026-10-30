from django.test import TestCase
from django.urls import reverse


class StudentAPITests(TestCase):

    def test_student_api_status(self):
        response = self.client.get(reverse('student-home'))
        self.assertEqual(response.status_code, 200)

    def test_student_api_message(self):
        response = self.client.get(reverse('student-home'))
        self.assertEqual(
            response.json()['message'],
            'Welcome to the Student API'
        )

# Create your tests here.
