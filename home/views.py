from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import ProjectModel


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileView(DetailView):
    model = ProjectModel
    context_object_name = 'project'
    template_name = 'student/student_home.html'


class FormSubmissonView(CreateView):
    model = ProjectModel
    fields = ('title', 'subtitle', 'teacher', 'description',)
    template_name = 'student/create_form.html'
