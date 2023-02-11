from django.db import models

# Create your models here.
class Account(models.Model):
    account_Name = models.TextField()
    account_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.account_Name

class Customer(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    national_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.surname

class Customer_Account_Details(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_Number = models.TextField()
    
    def __str__(self):
        return self.customer
