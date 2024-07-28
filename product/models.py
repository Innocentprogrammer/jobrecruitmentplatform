from django.db import models

class Product(models.Model):
    product_image=models.FileField(upload_to="product/",max_length=250, null=True, default=None)
    product_name=models.CharField(max_length=50)
    product_desc=models.TextField()

# Create your models here.
