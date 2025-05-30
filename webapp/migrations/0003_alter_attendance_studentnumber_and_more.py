# Generated by Django 5.1.7 on 2025-04-16 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_attendance_studentnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='studentNumber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.student'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='subjectCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.subject'),
        ),
    ]
