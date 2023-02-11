from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    national_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    percentage = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nextofkin')
    
    def __str__(self):
        return self.surname

class Account(models.Model):
    Account_number = models.TextField()