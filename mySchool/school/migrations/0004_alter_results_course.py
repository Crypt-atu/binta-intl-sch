# Generated by Django 5.1.3 on 2025-01-03 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_lecturers_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='school.courses'),
        ),
    ]
