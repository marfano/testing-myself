from django.test import SimpleTestCase
from apps.person.forms import StudentForm, TeacherForm
from faker import Faker

fake = Faker()

from .providers.forms_providers import FormStudentProvider, FormTeacherProvider
fake.add_provider(FormStudentProvider)
fake.add_provider(FormTeacherProvider)


class TestStudentForm(SimpleTestCase):
        
    def test_forms_is_valid(self):
        form_data = fake.form_data()
        form = TeacherForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
        # ... other tests relating forms, for example checking the form data
        
    def test_forms_no_valid(self):
        form =  TeacherForm(data={})
        self.assertFalse(form.is_valid())
