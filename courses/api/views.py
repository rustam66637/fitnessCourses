from rest_framework import generics
from courses.models import Course, Teacher
from courses.api.serializers import CoursesSerializer


class CoursesListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

