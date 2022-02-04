from django.test import TestCase, Client
from django.urls import reverse
from apps.person.models import Student
from tests.factories import ScheduleFactory
from apps.course.views import *

class FilterTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('course:course_list')
        self.students = Student.objects.all()
        self.teachers = Teacher.objects.all()

        self.request = {
            'modality':'Grupal',
            'capacity':'6',
            'level':'Begginer',
            'schedule': ScheduleFactory.build(),
            'tolerance':'2',
        }
        

    # VIEW

    def test_course_create_get_context_data(self):
        """Course list view works"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    # FILTERS
        
    def test_filter_view_is_valid_param(self):
        """Useful validation queryparam function works"""
        param = 'Individual'
        self.assertEqual(is_valid_queryparam(param), True)

    def test_teacher_handler(self):
        disponibility = self.request['schedule']

        # Both of them are Querysets - I'm getting the first element to compare
        # ALERT! Just if the Queryset dont't empty  -> else, queryset type return error
        expected = self.teachers.filter(disponibility=disponibility)
        result = teacher_handler(self.teachers, disponibility)

        if result.count() == 0: # case: is empty
            result = 0
        else:
            result = result[0] # case: no empty
        if expected.count() == 0: # case: is empty
            expected = 0
        else:
            expected = expected[0] # case: no empty
        
        self.assertEqual(result, expected)
        
        
    def test_filter_view_filter_handler(self):
        """Main filters filter handler works"""
        
        qs = self.students

        modality = self.request['modality']
        level = self.request['level']
        disponibility = self.request['schedule']

        students = self.students.filter(level=level)
        students = self.students.filter(modality=modality)
        students = self.students.filter(disponibility=disponibility)

        # Both of them are Querysets - I'm getting the first element to compare
        # ALERT! Just if the Queryset dont't empty  -> else, queryset type return error
        result = filter_handler(qs, modality, level, disponibility)
        expected = students
        
        if result.count() == 0: # case: is empty
            result = 0
        else:
            result = result[0] # case: no empty
        
        if expected.count() == 0: # case: is empty
            expected = 0
        else:
            expected = expected[0] # case: no empty

        self.assertEqual(result, expected)

    

    def test_filter_view_capacity_handler(self):
        """Capacity filter handler works"""
        
        modality = self.request['modality']
        capacity = self.request['capacity'] # value: 6
        
        if modality == 'Individual':
            self.assertEqual(int(capacity_handler(modality, capacity)), 1)
        else:
            self.assertEqual(int(capacity_handler(modality, capacity)), 6)
        # capacity_handler() return a string


    # def test_filter_gap_handler(self):
    #     """Gap filter handler works"""
    # TO IMPLEMENT

     # def test_filter_gap_handler(self):
    #     """Gap filter handler works"""
    # TO IMPLEMENT
        




        