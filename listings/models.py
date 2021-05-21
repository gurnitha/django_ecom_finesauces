# listings/models.py

# Django modules
from django.db import models


# Create your models here.

# Category model
class Cagegory(models.Model):

	name = models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Cagegory"
        verbose_name_plural = "Cagegories"

    def __str__(self):
        return self.name 
    
