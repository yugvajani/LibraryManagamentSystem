from django.shortcuts import render,redirect
from users.models import Librarian,Member
from lib.models import Books
from lib.forms import AddBooks, MemberForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from library.settings import UNAUTHORIZED_URL
# Create your views here.

def librarian_check(user):
	# return user.is_superuser
	librarian = Librarian.objects.filter(user=user).first()
	if librarian:
		return True
	else:
		return False

def welcome(request):
	return render(request,"lib/welcome.html")

def home(request):
	if Librarian.objects.filter(user=request.user).first():
		print("lib")
		return render(request,"lib/librarian_home.html")
	# if Member.objects.filter(user=request.user).first():
	else:
		books = Books.objects.all()
		print("mem")
		return render(request,"lib/member_home.html", {'books':books})

@user_passes_test(librarian_check, login_url='unauthorized-access')
def manage_books(request):
	return render(request,"lib/manage_books.html")

# def manage_fines(request):
# 	return render(request,"Fine/templates/Fine/manage_fines.html")

# @user_passes_test(librarian_check, login_url='unauthorized-access')
# def manage_users(request):
# 	return render(request,"lib/manage_users.html")

@user_passes_test(librarian_check, login_url='unauthorized-access')
def add_books(request):
	if(request.method=='POST'):
		form = AddBooks(request.POST, request.FILES)
		if(form.is_valid()):
			form.save()
			messages.success(request, 'Book has been added!')
			return redirect('manage-books')
		else:
			messages.error(request, 'Error adding book')
	else:
		form = AddBooks()
	return render(request,"lib/add_books.html",{'form':form})

def view_books(request):
	books = Books.objects.all()
	return render(request,"lib/view_books.html",{'books':books})

@user_passes_test(librarian_check, login_url='unauthorized-access')
def delete_books(request,id):
	books = Books.objects.filter(id=id).first()
	books.delete()
	messages.success(request, 'Book deleted successfully!')
	return redirect('view-books')

@user_passes_test(librarian_check, login_url='unauthorized-access')
def update_books(request,id):
	print(id)
	books = Books.objects.get(id=id)
	if (request.method == 'POST'):
		update_form = AddBooks(request.POST,request.FILES,instance=books)
		if (update_form.is_valid()):
			update_form.save()
			messages.success(request, 'Book updated!')
		else:
			messages.error(request, 'Book update error!')
		return redirect('view-books')
	else:
		update_form = AddBooks(instance=books)
	return render(request,"lib/update_books.html",{'update_form':update_form})


def unauthorized_access(request):
	return render(request,"lib/unauthorized_access.html")