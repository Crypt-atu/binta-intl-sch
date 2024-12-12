from django.db import models



class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    desription = models.TextField(null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    department = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)
    lecturer = models.ForeignKey('Lecturers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_courses'

    def __str__(self):
        return f'{self.name}'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    secretary = models.CharField(max_length=45, blank=True, null=True)
    faculty = models.ForeignKey('Faculties', models.DO_NOTHING, blank=True, null=True)
    h_o_d = models.OneToOneField('Lecturers', models.DO_NOTHING, db_column='h_o_d', blank=True, null=True)

    class Meta:
        db_table = 'school_departments'

    def __str__(self):
        return f'{self.name}'


class Faculties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    dean = models.OneToOneField('Lecturers', models.DO_NOTHING, blank=True, null=True)

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
    student = models.ForeignKey('Students', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'school_guardians'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lecturers(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    active = models.CharField(max_length=5, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

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
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_results'

    def __str__(self):
        return f'{self.student} Result'


class calendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    calendar_date = models.DateField(blank=True, null=True)
    calendar_time = models.TimeField(blank=True, null=True)
    calendar_event = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'school_calendar'

    def __str__(self):
        return f'{self.calendar_event}'



class Students(models.Model):
    
    GENDER = [('male', 'Male'), 
              ('female', 'Female')]
    
    OPTION = [('true', 'True'),
              ('false', 'False')]

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    d_o_b = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    active = models.CharField(max_length=6, choices=OPTION, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey(Levels, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'school_students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
