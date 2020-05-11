from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from courses.models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'short_name', 'name', 'position', 'imageUrl'
        ]


class CoursesSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = [
                    'name',
                    'description',
                    'place',
                    'teacher',
                    'startTime',
                    'endTime',
                    'weekDay',
                    'appointment_id',
                    'service_id',
                    'pay',
                    'appointment',
                    'color',
                    'availability',
                    # 'teacher_v2'
        ]


