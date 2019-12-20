# Generated by Django 3.0.1 on 2019-12-19 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('student_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True)),
                ('teacher', models.CharField(default='', max_length=255, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
