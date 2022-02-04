from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.course.views import FilterView
from apps.person.views import StudentCreate, StudentUpdate, StudentDelete, TeacherCreate, TeacherUpdate, TeacherDelete
from apps.schedule.views import ScheduleCreate, ScheduleDelete

class TestStudentUrls(SimpleTestCase):

    def test_student_create_resolves(self):
        """The create student page loads properly"""
        url = reverse('person:student_create')
        """ 
        print(resolve(url)) shows something like -> 
        ResolverMatch(func=apps.person.views.TeacherCreate, args=(), kwargs={}, url_name='teacher_create', 
        app_names=['person'], namespaces=['person'], route='person/teacher_create/')
        
        So I do an assertEquals like... 
        """
        self.assertEqual(resolve(url).func.view_class, StudentCreate) # This works!! The same to others!

    def test_student_update_resolves(self):
        """The update student page loads properly"""
        url = reverse('person:student_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, StudentUpdate)

    def test_student_delete_resolves(self):
        """The delete student page loads properly"""
        url = reverse('person:student_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, StudentDelete)


class TestTeacherUrls(SimpleTestCase):

    def test_teacher_create_resolves(self):
        """The create teacher page loads properly"""
        url = reverse('person:teacher_create')
        self.assertEqual(resolve(url).func.view_class, TeacherCreate)

    def test_teacher_update_resolves(self):
        """The update teacher page loads properly"""
        url = reverse('person:teacher_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, TeacherUpdate)

    def test_teacher_delete_resolves(self):
        """The delete teacher page loads properly"""
        url = reverse('person:teacher_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, TeacherDelete)



class TestScheduleUrls(SimpleTestCase):

    def test_schedule_create_resolves(self):
        """The create teacher page loads properly"""
        url = reverse('schedule:schedule_create')
        self.assertEqual(resolve(url).func.view_class, ScheduleCreate)

    def test_schedule_delete_resolves(self):
        """The delete student page loads properly"""
        url = reverse('schedule:schedule_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, ScheduleDelete)



class TestCourseUrls(SimpleTestCase):

    def test_course_filter_view_resolves(self):
        """The filter to courses page loads properly"""
        url = reverse('course:course_list')
        self.assertEqual(resolve(url).func.view_class, FilterView)
