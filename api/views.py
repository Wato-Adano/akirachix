from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .serializers import CoursesSerializer
from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from .serializers import ClassroomPeriodSerializer
from models import ClassroomPeriod
from models import Courses
from models import Teacher
from models import Student
from models import Class




class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

def post(self,request):
    serializers =StudentSerializer(data=request.data)
    if serializers.is_valid :
      serializers.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class StudentDetailView(APIView):
    def get(self, request, id):
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
def put(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    
class ClassListView(APIView):
    def get(self, request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        serializer = ClassroomPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ClassDetailView(APIView):
    def get(self,request,id):
        classes = Class.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)

def put(self,request,id):
       classes = Class.objects.get(id=id)
       serializer = ClassesSerializer(classes, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self,request,id):
        classes = Class.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

        

class ClassroomPeriodListView(APIView):
    def get(self, request):
        Periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(Periods, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        serializer = ClassroomPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    class ClassroomPeriodDetailView(APIView):
     def get(self,request,id):
        class_periods = ClassroomPeriod.objects.get(id=id)
        serializer = ClassroomPeriodSerializer(class_periods)
        return Response(serializer.data)

    def put(self,request,id):
       class_periods = ClassroomPeriod.objects.get(id=id)
       serializer = ClassroomPeriodSerializer(class_periods, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        class_periods = ClassroomPeriod.objects.get(id=id)
        class_periods.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class CoursesListView(APIView):
    def get(self, request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class CoursesDetailView(APIView):
    def get(self,request,id):
       courses = Courses.objects.get(id=id)
       serializer = CoursesSerializer(courses)
       return Response(serializer.data)


def put(self,request,id):
       courses = Courses.objects.get(id=id)
       serializer = CoursesSerializer(courses, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self,request,id):
        courses = Courses.objects.get(id=id)
        courses.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
