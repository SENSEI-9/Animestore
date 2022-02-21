from django.db import models

# Create your models here.
class Booking(models.Model):
    id= models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity=models.CharField(max_length=100,default=1)
    price =models.CharField(max_length=100)
    customer_id =models.CharField(max_length=100)

class Meta:
    db_table ="booking"