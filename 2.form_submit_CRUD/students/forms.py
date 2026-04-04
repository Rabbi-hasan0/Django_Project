from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'program', 'email', 'mobile_no', 'blood_group', 'dob', 'profile_pic']

        # Labels - string
        labels = {
            'name': 'Full Name',
            'program': 'Department',
            'email': 'Email',
            'mobile_no': 'Phone',
            'blood_group': 'Blood Group',
            'dob': 'Date of Birth',
            'profile_pic' : 'Profile',
        }

        # Widgets - must be Django Widget objects
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'program': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CSE/EEE/Civil/LAW'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }),
            'mobile_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '01XXXXXXXXX'
            }),
            'blood_group': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        }
