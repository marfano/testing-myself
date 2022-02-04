from django.test import SimpleTestCase
from apps.course.forms import ScheduleForm
from apps.person.forms import StudentForm, TeacherForm
from faker import Faker

fake = Faker()

from .providers.forms_providers import FormStudentProvider, FormTeacherProvider, FormScheduleProvider
fake.add_provider(FormStudentProvider)
fake.add_provider(FormTeacherProvider)
fake.add_provider(FormScheduleProvider)


class TestStudentForm(SimpleTestCase):

    def test_forms_is_valid(self):
        form_data = fake.form_student_data()
        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())
        # ... other tests relating forms, for example checking the form data

    def test_forms_no_valid(self):
        form =  StudentForm(data={})
        self.assertFalse(form.is_valid())


class TestTeacherForm(SimpleTestCase):
    
    def test_forms_is_valid(self):
        form_data = fake.form_teacher_data()
        form = TeacherForm(data=form_data)
        self.assertTrue(form.is_valid())
        # ... other tests relating forms, for example checking the form data

    def test_forms_no_valid(self):
        form =  TeacherForm(data={})
        self.assertFalse(form.is_valid())
