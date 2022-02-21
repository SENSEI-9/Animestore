from django.db import models

# Create your models here

class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    image = models.FileField(upload_to='product',default="default.jpg")
    class Meta:
        db_table="customer"