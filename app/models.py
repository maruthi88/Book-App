from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):

	"""creating Model for Book """

	author = models.ForeignKey(User,null=True)
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True,blank=False)
	updated_at = models.DateTimeField(auto_now_add=True,blank=False)
	description = models.CharField(max_length=100)
	price = models.IntegerField()
	publish = models.BooleanField(default=False)

	def __str__(self):

		return self.name

class Rating(models.Model):
	
	""" Its used to give rating to Book"""

	book = models.ForeignKey(Book,null=True)
	user = models.ForeignKey(User,null=True)
	rating = models.FloatField()
