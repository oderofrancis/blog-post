from django.db import models

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