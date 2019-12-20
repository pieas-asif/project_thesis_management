from django.urls import path

from .views import HomeView, ProfileView

urlpatterns = [
    path('student/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
]
