from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    page = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


gender = [('Male','Male'),('Female','Female')]

class Post(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=gender)
    post = models.TextField()
    bio = models.CharField(max_length=100,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    phone_number = PhoneNumberField(blank=True,null=True)

    def __str__(self):
        return self.name
