from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .serializers import CoursesSerializer

from .serializers import ClassesSerializer
from .serializers import ClassroomPeriodSerializer
from models import ClassroomPeriod
from models import Courses
from models import Student
from models import Class
from teacher.models import Teacher

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
class StudentListView(APIView):
    def get(self, request):
        Student= Student.object.all()
        first_name = request.query_params.get("first_name")   
        if first_name:
            students = students.filter(first_name= first_name) 
            country = request.query_params.get("country")
        if country:
           country= Students.filter(country=country)
        serializer = StudentSerializer(Student, many= True)
        return Response(serializer.data)
        
        
        
    def get(self, request):
        Student = Student.object.all()
        country = request.query_params.get("Country")
        if country:
            student = Student.objects.filter(Country= country)

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
    
    
    
    
class StudentDetailView(APIView):
    def enroll_student(self, student, courses_id):
        course = Courses.objects.get(id = course_id)
        student.cource.add(course)
    
    def post(self, request, id):
        studet = Student.objects.get(id=id)
        action = request.data.get("action")
        if action =="enroll":
            course_id =request.data.get("course_id")
            self.enroll_student(student, course_id)
            return Response(status=status.HTTP_202_ACCEPTED
                            )

    
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
def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Courses.objects.get(id=course_id)
        class_period = ClassroomPeriod(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)

def delete(self,request,id):
        teachers.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)
def assign_class(self, teacher, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




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
    


class TeacherListView(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
    def get(self,request,id):
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
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def enroll(self, student, course_id):
        course = Courses.objects.get(id = course_id)
        student.courses.add(course)



    def post(self, request,id):
        student = Student.obj<ects.get(id=id)
        action = request.data.get("action")
        if action=="email":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)

        return Response(status=status.HTTP_201_CREATED)





class TeacherDetailView(APIView):
    def get(self,request,id):
        teachers = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)
    
    def put(self,request,id):
       teachers = Teacher.objects.get(id=id)
       serializer = TeacherSerializer(teachers, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        teachers = Teacher.objects.get(id=id)
        teachers.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)
    def assign_class(self, teacher, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

