from django.shortcuts import render, redirect
from .models import Fine
from Transactions.models import Transaction
from users.models import Member,Librarian
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from lib.views import librarian_check
from django.contrib import messages


@login_required
def check_fines(request):
	user = request.user
	if librarian_check(request.user):
		fines = Fine.objects.all() 
		print(fines)
	else:
		print(user)
		member = Member.objects.get(user = user)
		transactions_of_member = Transaction.objects.filter(member =member).all()
		fines = Fine.objects.filter(transaction__in = transactions_of_member).all()
	return render(request, 'Fine/view_fines.html',{'fines' : fines, 'librarian' : librarian_check(user)})


#  function will be called from Transactions.views.return_book()
def calculate_fines(transaction):
	# print("1",(transaction.return_date - transaction.issue_date).days)
	if  transaction.return_date - transaction.issue_date >= timezone.timedelta(7):
		amount = (transaction.return_date -transaction.issue_date).days * 5
		# print(amount, transaction)
		fine = Fine.objects.create(amount=amount, transaction=transaction)
		# print("2", fine.transaction, fine.amount)
		fine.save()
		return True
	else:
		return False

# only librarian access
@user_passes_test(librarian_check, login_url='unauthorized-access')
def pay_fine(request, id):
	fine = Fine.objects.get(id = id)
	fine.date_paid = timezone.localdate()
	fine.save()
	messages.success(request, 'Fine paid successfully')
	return redirect('view-fines')
	# return render(request, 'Fine/fine_paid.html')
