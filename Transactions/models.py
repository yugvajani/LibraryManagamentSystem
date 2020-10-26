from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from lib.models import Books
from users.models import Member

class Transaction(models.Model):
	# user = models.ForeignKey(User, on_delete = models.CASCADE)
	member = models.ForeignKey(Member, on_delete= models.CASCADE, null=False)
	book = models.ForeignKey(Books, on_delete = models.CASCADE)
	issue_date = models.DateField(default=timezone.localdate)
	return_date = models.DateField(blank=True, null=True)
