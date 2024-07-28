from django.db import models

class Service(models.Model):
    service_image=models.FileField(upload_to="service/",max_length=250, null=True, default=None)
    service_name=models.CharField(max_length=50)
    service_desc=models.TextField()
# Create your models here.
