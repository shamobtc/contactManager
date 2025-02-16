from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title




class Contact(models.Model):
	category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=255)
	zipcode = models.CharField(max_length=50)
	city = models.CharField(max_length=50)


	def __str__(self):
		return f"{self.first_name} {self.last_name}"
