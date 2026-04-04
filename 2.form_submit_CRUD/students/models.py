from django.db import models
from django.db.models import Q

# Create your models here.
class Student(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    name=models.CharField(max_length=100)
    program=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile_no=models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    dob=models.DateField(null=True, blank=True)
    profile_pic=models.ImageField(upload_to='media/', null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.name}"


