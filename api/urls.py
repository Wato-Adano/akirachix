from django.urls import path
from .views import StudentListView
from .views import ClassListView
from .views import ClassroomPeriodListView
from .views import CoursesListView
from .views import TeacherListView


urlpatterns = [
    path(
        "students/", StudentListView.as_view(), name="student_list_view"
    ),
    path(
        "classes/", ClassListView.as_view(), name="class_list_view"
    ),
    path(
        "periods/", ClassroomPeriodListView.as_view(), name="classroomPeriod_list_view"
    ),
    path(
        "courses/", CoursesListView.as_view(), name="course_list_view" 
    ),
    path(
        "teachers/", TeacherListView.as_view(), name="teachers_list_view"
    )
]
