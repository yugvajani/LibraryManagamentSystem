from django.shortcuts import render,redirect
from users.models import Librarian,Member
from lib.models import Books
from lib.forms import AddBooks, MemberForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from library.settings import UNAUTHORIZED_URL
from lib.views import librarian_check




@user_passes_test(librarian_check, login_url='unauthorized-access')
def manage_users(request):
	return render(request,"lib/manage_users.html")


@user_passes_test(librarian_check, login_url='unauthorized-access')
def add_users(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		member_form = MemberForm(request.POST)
		if member_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			member =  member_form.save(commit=False)
			member.user = user
			member.save()
			messages.success(request, f'Registration complete! You may log in!')
		else:
			messages.error(request, f'Registration error!')
		return redirect('manage-users')

	else:
		user_form = UserForm(request.POST)
		member_form = MemberForm(request.POST)
	return render(request, 'users/add_users.html', {'user_form': user_form, 'member_form': member_form})
		
	# return render(request,"lib/add_users.html",{'form':form})

def view_users(request):
	members = Member.objects.all()
	return render(request,"users/view_users.html",{'members':members})

@user_passes_test(librarian_check, login_url='unauthorized-access')
def delete_users(request,id):
	member = Member.objects.filter(uid=id).first()
	member.user.delete()
	member.delete()
	messages.success(request, 'User deleted!')
	return redirect('view-users')

@user_passes_test(librarian_check, login_url='unauthorized-access')
def update_users(request,id):
	members = Member.objects.get(uid=id)
	if (request.method == 'POST'):
		user_update_form = UserForm(request.POST,instance = members.user)
		member_update_form =  MemberForm(request.POST,instance=members)
		if (user_update_form.is_valid() and member_update_form.is_valid()):
			user  = user_update_form.save()
			member = member_update_form.save(commit=False)
			member.user = user
			member.save()
			messages.success(request, f'Update complete!')
			return redirect('view-users')
		else:
			messages.error(request, f'Update unsucessful')
	else:
		user_update_form = UserForm(instance = members.user)
		member_update_form =  MemberForm(instance=members)
	return render(request,"users/update_users.html",{'user_update_form':user_update_form,"member_update_form" : member_update_form})