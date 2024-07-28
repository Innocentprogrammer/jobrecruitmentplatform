from django.db import models

class Recruitment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    position=models.CharField(max_length=50)
    passout=models.CharField(max_length=5)
    experience=models.CharField(max_length=5)
    summary=models.TextField()
    resume=models.FileField(upload_to="resume/",null=True, default=None)


# Create your models here.
