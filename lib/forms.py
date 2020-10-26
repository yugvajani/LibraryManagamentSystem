from django import forms
from .models import Books
from django.contrib.auth.models import User
from users.models import Member
from django.contrib.auth.forms import UserCreationForm


class AddBooks(forms.ModelForm):
	class Meta:
		model = Books
		fields = ['book_image','book_title','author_name','book_description','book_subject','book_quantity']













class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'password1', 'password2']


class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['is_type','uid', 'department']