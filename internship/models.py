from django.db import models

class Internship(models.Model):
    job_image=models.FileField(upload_to="internship/",max_length=250, null=True, default=None)
    job_name=models.CharField(max_length=100)
    job_desc=models.TextField()
# Create your models here.
