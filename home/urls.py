from django.urls import path

from .views import (
    HomeView,
    ProfileView,
    FormSubmissonView,
    TeacherHomeView,
    TeacherDetailView,
    TeacherReviewView
)

urlpatterns = [
    path('teacher/review/<int:pk>',
         TeacherReviewView.as_view(), name='teacher_review'),
    path('teacher/detail/<int:pk>',
         TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/', TeacherHomeView.as_view(), name='teacher_home'),
    path('student/create/<int:pk>',
         FormSubmissonView.as_view(), name='create_form'),
    path('student/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
]
