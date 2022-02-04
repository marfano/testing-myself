from apps.person.models import Student, Teacher
from apps.schedule.models import Schedule
from django.views.generic import ListView

from django.core.paginator import Paginator

"""
'Django’s generic views were developed to ease that pain. 
They take certain common idioms and patterns found in view development 
and abstract them so that you can quickly write common views of data 
without having to write too much code.' - Django Project
>> I want to know more! I should visit: https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
"""


"""Filter view - Tentative courses handler"""
class FilterView(ListView):
    model = Student
    template_name = 'index.html'
    success_url = 'student_create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_queryset()
        return context

    """Main handler method"""
    def get_queryset(self):
        teachers = Teacher.objects.all()
        qs = Student.objects.all()
        disponibility = self.request.GET.get('schedule')
        modality = self.request.GET.get('modality')
        level = self.request.GET.get('level')
        capacity = self.request.GET.get('capacity')
        schedules = Schedule.objects.all()
        tolerance = self.request.GET.get('tolerance')
        
        
        qs = filter_handler(qs, modality, level, disponibility) # filter students / queryset
        gap = gap_handler(schedules, disponibility, tolerance) # to confirm students
        capacity = capacity_handler(modality, capacity) # capacity of group (individual = 1, grupal > 1)
        groups = group_handler(self.request, capacity, qs) # students clustering
        teachers = teacher_handler(teachers, disponibility)

        context = {
            'teachers': teachers,
            'entity': groups['entity'], 
            'paginator': groups['paginator'],
            'gap': gap,
            'modality': self.request.GET.get('modality')
        }
        return context



"""Useful function to validate filters"""
def is_valid_queryparam(param):
    return param != '' and param is not None

""""Teacher handler"""
def teacher_handler(teachers, schedule):
    # Filtering theachers by disponibility -> 
    # Remember: What disponibility match students? The teacher disponibility! 
    # Just teachers be able to suggest schedules
    if is_valid_queryparam(schedule):
        teachers = teachers.filter(disponibility=schedule)
    return teachers	

"""Handling level, modality & disponibility"""
def filter_handler(qs, modality, level, disponibility):
    # Filtering students by modality, level and disponibility
    """Handler the level"""
    if is_valid_queryparam(level):
        qs = qs.filter(level=level)

    if is_valid_queryparam(modality):
        qs = qs.filter(modality=modality)

    if is_valid_queryparam(disponibility):
        qs = qs.filter(disponibility=disponibility)
    return qs

"""Manage the capacity"""
def capacity_handler(modality, capacity):
    # Stating the course capacity by selected modality
    if is_valid_queryparam(modality):
        if modality == 'Individual':
            capacity = 1

        return capacity

"""Manage the tolerance"""
def gap_handler(schedules, disponibility, tolerance):
    # Filtering the gap-students to confirm enrolment (by time tolerance) 
    if is_valid_queryparam(tolerance) & is_valid_queryparam(disponibility):
        # hour and day from the selected disponibility:
        hour = disponibility.hour 
        day = disponibility.day

        # tolerance gap:
        positive_gap = hour + tolerance # example: hour 10.00 + 2 on tolerance = 12.00hs 
        negative_gap = hour - tolerance # example: hour 10.00 - 2 on tolerance = 10.00hs 
        
        if positive_gap - hour == 1: # example: 11.00 - 10.00 = 1 hour -> just take 11.00 gap hour
            for schedule in schedules:
                if schedule.hour == positive_gap and schedule.day == day:
                    # finding the correct schedule and filtering the students that contain the same...
                    positive_gap_students = Student.objects.filter(disponibility=schedule)
            
            # ...And the same with the negative gap...
            for schedule in schedules:
                if schedule.hour == negative_gap and schedule.day == day:
                    negative_gap_students = Student.objects.filter(disponibility=schedule)
        
        else: # case (gap - hour) > 1 
            for i in range(hour+1, positive_gap): # example: 10.00 to 12.00hs -> 11 to 12
                for schedule in schedules:
                    if schedule.hour == i and schedule.day == day:
                        # finding the correct schedule and filtering the students that contain the same...
                        positive_gap_students = Student.objects.filter(disponibility=schedule)
            
            # ...And the same with the negative gap...
            for i in range(negative_gap, hour-1): # example: 8.00 to 10.00hs
                for schedule in schedules:
                    if schedule.hour == i and schedule.day == day:
                        negative_gap_students = Student.objects.filter(disponibility=schedule)


        gap = {
            'positive': positive_gap_students,
            'negative': negative_gap_students
        } # the gap students to confirm

        return gap

"""Manage the clustering"""
def group_handler(request, capacity, qs):
    # the same logic than the pagination method
    """
    'Django provides high-level and low-level ways to help you manage paginated data 
    – that is, data that's split across several pages, with “Previous/Next” ...'
    >> - Django Project. >> To know more: https://docs.djangoproject.com/en/4.0/topics/pagination/ 
    """
    students = Student.objects.all()
    paginator = None
    group = request.GET.get('group', 1)

    if is_valid_queryparam(capacity):
        if int(capacity) > 1: # no individual modality => show group
            show = capacity 
        else:            # individual modality => show individual posibilities
            show = 20

        paginator = Paginator(qs, show)
        students = paginator.page(group)

    groups = {
        'entity': students,  # call this entity! To be able to use the 'paginator.html' template (it's generic!)
        'paginator': paginator
    }

    return groups
