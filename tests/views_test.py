import json
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from faker import Faker
from apps.person.models import Student, Teacher

from tests.factories import StudentFactory


"""Student views"""

class TestStudentViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_url = reverse('person:student_create')
        self.student = Student.objects.create(
            id = 1,
            name = 'John',
            last_name = 'Snow'
        )

        self.update_url = reverse('person:student_update', args=[self.student.id])
        self.delete_url = reverse('person:student_delete', args=[self.student.id])


    # CREATE

    def test_student_create_GET(self):
        """Student create view works"""
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_create.html')

    def test_student_create_POST_no_data(self):
        """Student create POST without data works"""
        response = self.client.post(self.create_url, { })
        self.assertEqual(response.status_code, 200)

    def test_student_create_POST(self):
        """Student create POST works"""
        response = self.client.post(self.create_url, {
            'last_name':'Skywalker',
        })
        self.assertEqual(response.status_code, 200)


    # UPDATE

    def test_student_update_GET(self):
        """Student update view works"""
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_update.html')
        self.assertEqual(response.context['student'].pk, 1)

    def test_student_update_POST(self):
        """Student update POST works"""
        response = self.client.post(self.update_url, {
            'name':'Luke',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['student'].name, 'Luke')


    # DELETE

    def test_student_delete_GET(self):
        """Student delete view works"""
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_confirm_delete.html')

    def test_student_DELETE(self):
        """Student delete works"""
        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        self.assertEqual(response.status_code, 302)

   



"""Teacher views"""

class TestTeacherViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('person:teacher_create')
        self.teacher = Teacher.objects.create(
            id = 1,
            name = 'Master',
            last_name = 'Yoda'
        )

        self.update_url = reverse('person:teacher_update', args=[self.teacher.id])
        self.delete_url = reverse('person:teacher_delete', args=[self.teacher.id])


    # CREATE

    def test_teacher_create_GET(self):
        """Teacher create view works"""
        response = self.client.get(self.create_url, { })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/teacher_create.html')

    def test_teacher_create_POST(self):
        """Teacher create POST works"""
        response = self.client.post(self.create_url, {
            'last_name':'Kenobi',
        })
        self.assertEqual(response.status_code, 200)


    # UPDATE

    def test_teacher_update_GET(self):
        """Teacher update view works"""
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/teacher_update.html')
        self.assertEqual(response.context['teacher'].pk, 1)

    def test_teacher_update_POST(self):
        """Teacher update POST works"""
        response = self.client.post(self.update_url, {
            'name':'Yoda',
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['teacher'].name, 'Yoda')

    def test_teacher_update_POST_no_data(self):
        """Teacher update POST without data works"""
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['teachers'].count(), 1) # Just 'Yoda' yet

    
    # DELETE

    def test_teacher_delete_GET(self):
        """Teacher delete view works"""
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/teacher_confirm_delete.html')

    def test_teacher_DELETE(self):
        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        self.assertEqual(response.status_code, 302)


"""Course view"""
   
class TestCourseView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('course:course_list')

    # VIEW

    def test_course_create_get_context_data(self):
        """Course list view works"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
