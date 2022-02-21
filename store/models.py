from unicodedata import name
from django.db import models

# Create your models here.
class Usercontact(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)

    class Meta:
        db_table='contactuser'