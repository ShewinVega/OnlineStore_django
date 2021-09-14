from django.db import models

# Create your models here.
class Clients(models.Model):
  name=models.CharField(max_length=30)
  address= models.CharField(max_length=50,verbose_name="Address (direccion)")
  email= models.EmailField(blank=True,null= True)
  tel= models.CharField(max_length=10)

  
  def __str__(self):
     return self.name