from django.shortcuts import render
from django.views import View
from .models import Course, Teacher
from django.http import JsonResponse

class CoursesList(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'courses/courses_list.html', context=context)

def json_list_courses(request):
    courses = Course.objects.all()
    return JsonResponse(
        {
            'courses': [
                {
                    'name': c.name,
                    'description': c.description,
                    'place': c.place,
                    'teacher': c.teacher,
                    'startTime': c.startTime,
                    'endTime': c.endTime,
                    'weekDay': c.weekDay,
                    'appointment_id': c.appointment_id,
                    'service_id': c.service_id,
                    'pay': c.pay,
                    'appointment': c.appointment,
                    'color': c.color,
                    'availability': c.availability,
                    'teacher_v2': [
                        {
                            'a': c.teacher.name,
                        }
                    ]
                }
                for c in courses
            ]
    })
