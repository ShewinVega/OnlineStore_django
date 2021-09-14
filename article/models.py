from django.db import models

# Create your models here.

class Articles(models.Model):
  name=models.CharField(max_length=30)
  section=models.CharField(max_length=20)
  price= models.IntegerField()
  
  def __str__(self):
    return 'Name is  %s the section is %s and price is %s' % (self.name , self.section , self.price)
