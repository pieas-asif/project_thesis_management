# Generated by Django 3.0.1 on 2019-12-20 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191220_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='final_def_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='first_def_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='mid_def_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
