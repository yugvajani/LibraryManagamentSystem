from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
# Create your models here.
class Books(models.Model):
	book_title = models.CharField(max_length=100)
	book_image = models.ImageField(default = 'default.jpg', upload_to = 'book_pics')
	author_name = models.CharField(max_length=100)
	book_description = models.CharField(max_length=200)
	book_subject = models.CharField(max_length=100)
	book_quantity = models.IntegerField(default=10)

	def __str__(self):
		return self.book_title




 
