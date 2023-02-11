from django.shortcuts import render
from .serializers import Account_Serializer,Customer_Account_Details_Serializer,Customer_Serializer
from rest_framework import viewsets
from .models import *

# Create your views here.
class Account_Viewset(viewsets.ModelViewSet):
    serializer_class = Account_Serializer
    queryset = Account.objects.all()

class Customer_Viewset(viewsets.ModelViewSet):
    serializer_class = Customer_Serializer
    queryset = Customer.objects.all()

class Cutomer_Account_Viewset(viewsets.ModelViewSet):
    serializer_class = Customer_Account_Details_Serializer
    queryset = Customer_Account_Details.objects.all()