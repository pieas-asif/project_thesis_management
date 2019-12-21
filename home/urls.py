from django.urls import path

from .views import HomeView, ProfileView, FormSubmissonView

urlpatterns = [
    path('student/create/<int:pk>',
         FormSubmissonView.as_view(), name='create_form'),
    path('student/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
]
