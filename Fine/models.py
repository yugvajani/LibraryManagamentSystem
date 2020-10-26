from django.db import models
from Transactions.models import Transaction
from django.utils import timezone

# Create your models here.
class Fine(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    amount = models.FloatField(null=False,default=0)
    date_paid = models.DateField(blank=True,null= True)

