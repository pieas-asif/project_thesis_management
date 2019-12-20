from django.db import models
from django.contrib.auth import get_user_model


class ProjectModel(models.Model):
    student_key = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    teacher = models.CharField(
        max_length=255,
        default="",
        null=True,
        blank=True
    )
    description = models.TextField()
    first_def_title = models.CharField(max_length=255, default="Soon")
    first_def_time = models.DateField(null=True, blank=True)
    first_def_desc = models.TextField(default="", null=True, blank=True)
    mid_def_title = models.CharField(max_length=255, default="Soon")
    mid_def_time = models.DateField(null=True, blank=True)
    mid_def_desc = models.TextField(default="", null=True, blank=True)
    final_def_title = models.CharField(max_length=255, default="Soon")
    final_def_time = models.DateField(null=True, blank=True)
    final_def_desc = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.title
