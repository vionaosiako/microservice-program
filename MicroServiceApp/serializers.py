from rest_framework import serializers
from . import models
from .models import *

class Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class Customer_Account_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Account_Details
        fields = '__all__'