# Generated by Django 3.0.1 on 2019-12-20 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191220_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='final_def_desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='first_def_desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='mid_def_desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
