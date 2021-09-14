from django.db import models

# Create your models here.

class Orders(models.Model):
  number=models.IntegerField()
  date=models.DateField()
  delivered=models.BooleanField()

  class Meta:
    verbose_name = 'Orden'
    verbose_name_plural = 'Ordenes'

  def __str__(self):
    return self.number