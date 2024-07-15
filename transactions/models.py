from django.db import models
from accounts.models import Useraccount
# Create your models here.
DEPOSIT = 1
WITHDRAWAL = 2
LOAN = 3
LOAN_PAID = 4

TRANSACTION_TYPE = (
    (DEPOSIT, 'Deposite'),
    (WITHDRAWAL, 'Withdrawal'),
    (LOAN, 'Loan'),
    (LOAN_PAID, 'Loan Paid'),
    
)

class Transaction(models.Model):
    account=models.ForeignKey(Useraccount,related_name='transaction',on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['timestamp']     