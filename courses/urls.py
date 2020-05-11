from django.urls import path
from .views import *

urlpatterns = [
    path('', CoursesList.as_view(), name='courses_url'),
    # path('api/', json_list_courses)
]