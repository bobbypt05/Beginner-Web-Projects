from django.db import models

# Create your models here.

class SignUpModel(models.Model):

	username = models.CharField(max_length=50)

	first_name = models.CharField(max_length=30)

	last_name = models.CharField(max_length=30)

	email = models.EmailField(max_length=254)

	password1 = models.CharField(max_length=20)

	password2 = models.CharField(max_length=20)

	def __str__(self):
		return self.username 






#'username', 'first_name', 'last_name', 'email', 'password1', 'password2',	