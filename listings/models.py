# listings/models.py

# Django modules
from django.db import models


# Create your models here.

# Category model
class Category(models.Model):

	name = models.CharField(
		max_length=100,
		unique=True
	)

	slug = models.SlugField(
		max_length=100,
		unique=True
	)

	class Meta:
		ordering = ('-name',)
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
    

# Product model
class Product(models.Model):

	name = models.CharField(
		max_length=100, 
		unique=True
	)
	
	slug = models.SlugField(
		max_length=100, 
		unique=True
	)
	
	image = models.ImageField(
		upload_to='products/'
	)
	
	description = models.TextField()
	
	shu = models.CharField(
		max_length=10
	)

	price = models.DecimalField(
		max_digits=10, 
		decimal_places=2
	)
	
	available = models.BooleanField(
		default=True
	)
	
	class Meta:
		ordering = ('shu',)

	def __str__(self):
		return self.name
