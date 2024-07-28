from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=10)
    message=models.TextField()
# Create your models here.
