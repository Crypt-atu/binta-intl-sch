#Imported Classes to be used here
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db.models import Q

#Models Created Here

#Courses Table(Model)
class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    #A One to Many Field
    department = models.ForeignKey('Departments', on_delete=models.SET_NULL, blank=True, null=True)
    lecturer = models.ForeignKey('Lecturers', on_delete=models.SET_NULL, blank=True, null=True)

    #Defination for name of the table
    class Meta:
        db_table = 'school_courses'

    #String Representation for the class
    def __str__(self):
        return f'{self.name}'

#Departments Table(Model)
class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    secretary = models.CharField(max_length=45, blank=True, null=True)
    faculty = models.ForeignKey('Faculties', on_delete=models.SET_NULL, related_name="departments", blank=True, null=True)
    #A One to One Related Field
    h_o_d = models.OneToOneField('Lecturers', on_delete=models.SET_NULL, db_column='h_o_d', blank=True, null=True)

    class Meta:
        db_table = 'school_departments'

    def __str__(self):
        return f'{self.name}'

#Faculties Table(Model)
class Faculties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    dean = models.OneToOneField('Lecturers', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'school_faculties'

    def __str__(self):
        return f'{self.name}'

#Guardians Table(Model)
class Guardians(models.Model):

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    active = models.BooleanField(default=True)
    student = models.ForeignKey('Students', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'school_guardians'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Lecturers Table(Model)
class Lecturers(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    active = models.BooleanField(default=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, related_name="lectures", blank=True, null=True)

    class Meta:
        db_table = 'school_lecturers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#Levels Table(Model)
class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_level = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'school_levels'

    def __str__(self):
        return f'{self.student_level}'

#Result Table(Model)
class Results(models.Model):
    id = models.BigAutoField(primary_key=True)
    attendance = models.IntegerField(blank=True, null=True)
    assignment = models.IntegerField(blank=True, null=True)
    test_score = models.IntegerField(blank=True, null=True)
    exam_scores = models.IntegerField(blank=True, null=True)
    total_scores = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=1, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True, related_name='courses')
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'school_results'

    def __str__(self):
        return f'{self.student} Result'

#Calendar Table(Model)
class SchoolCalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    event = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'school_calendar'

    def __str__(self):
        return f'{self.event}'

from django.db import models

#Making the Student table the main user authentication model
#(Only Needed when you are trying to make another field what the user will use and login)
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

#Students Table(Model) Inheriting from the AbstractUser class
class Students(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    username = None#Since it is not needed
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)  
    d_o_b = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    active = models.BooleanField(default=True)
    department = models.ForeignKey('Departments', on_delete=models.SET_NULL, blank=True, null=True)
    level = models.ForeignKey('Levels', on_delete=models.SET_NULL, blank=True, null=True)
    courses = models.ManyToManyField('Courses', related_name='students')

    USERNAME_FIELD = 'email'  # Use email as the username
    REQUIRED_FIELDS = ['first_name', 'last_name']  

    #calling from the Manger class above
    objects = StudentManager()

    class Meta:
        db_table = 'school_students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
