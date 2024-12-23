from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(null=True)  # Corrected the typo
    code = models.CharField(max_length=10, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    department = models.ForeignKey('Departments', on_delete=models.DO_NOTHING, blank=True, null=True)
    lecturer = models.ForeignKey('Lecturers', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_courses'

    def __str__(self):
        return f'{self.name}'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    secretary = models.CharField(max_length=45, blank=True, null=True)
    faculty = models.ForeignKey('Faculties', on_delete=models.DO_NOTHING, blank=True, null=True)
    h_o_d = models.OneToOneField('Lecturers', on_delete=models.DO_NOTHING, db_column='h_o_d', blank=True, null=True)

    class Meta:
        db_table = 'school_departments'

    def __str__(self):
        return f'{self.name}'


class Faculties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    dean = models.OneToOneField('Lecturers', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_faculties'

    def __str__(self):
        return f'{self.name}'


class Guardians(models.Model):
    OPTION = [('true', 'True'),
                ('false', 'False')]

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    active = models.CharField(max_length=5, choices=OPTION, null=True)
    student = models.ForeignKey('Students', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'school_guardians'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lecturers(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    active = models.CharField(max_length=5, blank=True, null=True)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_lecturers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_level = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'school_levels'

    def __str__(self):
        return f'{self.student_level}'


class Results(models.Model):
    id = models.BigAutoField(primary_key=True)
    attendance = models.IntegerField(blank=True, null=True)
    assignment = models.IntegerField(blank=True, null=True)
    test_score = models.IntegerField(blank=True, null=True)
    exam_scores = models.IntegerField(blank=True, null=True)
    total_scores = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=1, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_results'

    def __str__(self):
        return f'{self.student} Result'


class SchoolCalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    event = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'school_calendar'

    def __str__(self):
        return f'{self.event}'


class StudentManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Students(AbstractUser):
    GENDER = [('male', 'Male'),
              ('female', 'Female')]

    OPTION = [('true', 'True'),
              ('false', 'False')]

    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)  # Optional, override if needed
    email = models.EmailField(unique=True, blank=True, null=True)  # Email as the primary identifier
    d_o_b = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    active = models.CharField(max_length=6, choices=OPTION, null=True)
    department = models.ForeignKey('Departments', on_delete=models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('Levels', on_delete=models.DO_NOTHING, blank=True, null=True)
    courses = models.ManyToManyField('Courses', related_name='courses')

    USERNAME_FIELD = 'email'  # Set email as the username field
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Ensure that 'email' is not in REQUIRED_FIELDS

    objects = StudentManager()

    class Meta:
        db_table = 'school_students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
