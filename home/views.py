from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import ProjectModel


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileView(DetailView):
    model = ProjectModel
    context_object_name = 'project'
    template_name = 'student/student_home.html'
