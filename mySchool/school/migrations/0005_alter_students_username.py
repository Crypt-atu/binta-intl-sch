# Generated by Django 5.1.3 on 2024-12-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_students_email_alter_students_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
