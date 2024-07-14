from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from .serializers import ClassroomPeriodSerializer
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self, request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes, many=True)
        return Response(serializer.data)


class ClassroomPeriodListView(APIView):
    def get(self, request):
        Periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(Periods, many=True)
        return Response(serializer.data)


class CoursesListView(APIView):
    def get(self, request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods, many=True)
        return Response(serializer.data)


