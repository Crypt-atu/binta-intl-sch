from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Students, Guardians
from django.contrib.auth import authenticate

# All Forms Here
#Student Reg Form Inheriting from UserCreationForm
class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'id': 'first-name',
            'class': 'Register-name',
        })
    )
    middle_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Middle Name',
            'id': 'middle-name',
            'class': 'Register-name',
        })
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'id': 'last-name',
            'class': 'Register-name',
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-mail',
            'class': 'register-container',
        })
    )
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'register-container',
        })
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Address',
            'class': 'register-container',
        })
    )
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'placeholder': 'Date of Birth',
            'type': 'date',
            'class': 'register-container',
        })
    )
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')],
        widget=forms.Select(attrs={
            'class': 'select-gender',
        })
    )

    class Meta:
        model = Students
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'address', 'date_of_birth', 'gender', 'password1', 'password2')

#save function
    def save(self, commit=True):
        # Use the parent class's save method to handle password hashing and other details
        student = super().save(commit=False)
        student.first_name = self.cleaned_data['first_name']
        student.middle_name = self.cleaned_data['middle_name']
        student.last_name = self.cleaned_data['last_name']
        student.email = self.cleaned_data['email']
        student.phone_number = self.cleaned_data['phone_number']
        student.address = self.cleaned_data['address']
        student.date_of_birth = self.cleaned_data['date_of_birth']
        student.gender = self.cleaned_data['gender']
        
        if commit:
            student.save()
        return student
    
    #clean function
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        # Check if passwords match
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    
#Student Login Form
class StudentLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'landing',
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'landing',
            'id': 'id_password',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password.")
            if not user.is_active:
                raise forms.ValidationError("This account is inactive.")
        return cleaned_data

#Student Enrollment Form
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['courses']

        widgets = {
            'courses': forms.CheckboxSelectMultiple(attrs={
                'class': 'check-button'
            })
        }


#Guardian Registration Form
class GuardianRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'Register-container',
        })
    )   
    
    last_name = forms.CharField(
        max_length=50,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'Register-container',
        })
    )   

    occupation = forms.CharField(
        max_length=50,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.TextInput(attrs={
            'placeholder': 'Occupation',
            'class': 'Register-container',
        })
    )

    address = forms.CharField(
        max_length=100,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.TextInput(attrs={
            'placeholder': 'Address',
            'class': 'Register-container',
        })
    )      

    email = forms.EmailField(
        max_length=50,
        required=True,
        #widget styles it according to your html and css styles
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'Register-container',
        })
    )  

    relationship = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Relationship to Student',
            'class': 'Register-container'
        })
    )

    phone_number = forms.CharField(
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'Register-container'
        })
    )

    
    class Meta:
        model = Guardians
        fields = ['first_name', 'last_name', 'occupation', 'address', 'email', 'relationship', 'phone_number']


    # def form_valid(self, form):
    #     # Save the data manually to the model
    #     Guardians.objects.create(
    #         student=self.request.user,  # Link to the logged-in student
    #         first_name=form.cleaned_data['first_name'],
    #         last_name=form.cleaned_data['last_name'],
    #         occupation=form.cleaned_data['occupation'],
    #         address=form.cleaned_data['address'],
    #         email=form.cleaned_data['email'],
    #         relationship=form.cleaned_data['relationship'],
    #         phone_number=form.cleaned_data['phone_number'],
    #     )
    #     return super().form_valid(form)




