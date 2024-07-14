from rest_framework import serializers
from student.models import Student
from classes.models import Class
from classroom_period.models import ClassroomPeriod
from courses.models import Courses


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ClassesSerializer(serializers.ModelSerializer):
    model = Class
    fields = "__all__"


class ClassroomPeriodSerializer(serializers.ModelSerializer):
    model = ClassroomPeriod
    fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    model = Courses
    fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    model = Courses
    fields = "__all__"