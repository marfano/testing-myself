import json

import pytest

from django.urls import reverse
from django.test import RequestFactory

rf = RequestFactory()

from django.test import TestCase


"""General views"""

class TestIndexView(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('localhost:8000')
        self.assertEqual(response.status_code, 404)


"""Student views"""

class TestStudentCreateView(TestCase):

    @pytest.mark.urls('apps.person.urls')
    def test_url_loads_properly(self):
        """The create page loads properly"""
        url = reverse('student_create')  # get up the url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestStudentListView(TestCase):

    @pytest.mark.urls('apps.person.urls')
    def test_url_loads_properly(self):
        """The list page loads properly"""
        url = reverse('student_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


"""Teacher views"""

class TestTeacherCreateView(TestCase):

    @pytest.mark.urls('apps.person.urls')
    def test_url_loads_properly(self):
        """The create page loads properly"""
        url = reverse('teacher_create')  # get up the url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestTeacherListView(TestCase):

    @pytest.mark.urls('apps.person.urls')
    def test_url_loads_properly(self):
        """The list page loads properly"""
        url = reverse('teacher_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)    