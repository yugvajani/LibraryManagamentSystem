from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils import timezone
# Create your models here.
is_type = (
	('Student','Student'),
	('Teacher','Teacher'),
	)
departments = (
	('Computer','Computer' ),
	('IT','IT'),
	('EXTC','EXTC'),
	('ETRX','ETRX'),
	)
class Librarian(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	# librarian_id = models.CharField(primary_key='True',max_length=60)
	librarian_name = models.CharField(max_length=100)
	dob = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))

	def __str__(self):
		return self.librarian_name

class Member(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	uid = models.IntegerField(primary_key=True,null=False,default=000000000)
	is_type = models.CharField(max_length=50,choices=is_type,default='Students')
	# member_id = models.CharField(primary_key='True',max_length=55)
	# member_name = models.CharField(max_length=100)
	department = models.CharField(max_length=50,choices=departments)

	def __str__(self):
		return self.user.first_name

# class User(AbstractBaseUser):
# 	uid = models.IntegerField(max_length=10,primary_key=True,unique=True)
# 	name = models.CharField()
# 	department = models.CharField(max_length=8)
# 	user_type = models.CharField(max_length=50,choices=is_type,default='Student')
# 	is_admin = models.BooleanField(default=False)
# 	is_active = models.BooleanField(default=False)
# 	is_staff = models.BooleanField(default=False)
# 	is_superuser = models.BooleanField(default=False)

# 	USERNAME_FIELD = 'uid'
# 	REQUIRED_FIELDS = ['uid','name','department','user_type']

# 	def __str__(self):
# 		return self.name
	
# 	def has_perm
