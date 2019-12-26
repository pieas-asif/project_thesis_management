from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
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


class TeacherHomeView(ListView):
    model = ProjectModel
    context_object_name = 'projects'
    template_name = 'teacher/teacher_home.html'


class TeacherDetailView(DetailView):
    model = ProjectModel
    context_object_name = 'project'
    template_name = 'teacher/teacher_detail_view.html'


class TeacherReviewView(UpdateView):
    model = ProjectModel
    context_object_name = 'project'
    fields = ('first_def_title', 'first_def_time', 'first_def_desc', 'mid_def_title',
              'mid_def_time', 'mid_def_desc', 'final_def_title', 'final_def_time', 'final_def_desc',)
    template_name = 'teacher/teacher_review.html'
