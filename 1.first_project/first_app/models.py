from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.TextField(max_length=200)
    photo=models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.id}. {self.name}"