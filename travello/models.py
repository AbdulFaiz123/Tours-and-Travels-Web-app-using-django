from distutils.command.upload import upload
from platform import mac_ver
from django.utils import timezone
from unicodedata import name
from django.db import models


# Create your models here.
class destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Detailed_desc(models.Model):
    name = models.CharField(max_length=200)
    days = models.IntegerField(default=5)
    price = models.IntegerField()
    rating = models.IntegerField(default=5)
    dest_name = models.CharField(max_length=25)
    img1=models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    desc = models.TextField()
    day1= models.CharField(max_length=200)
    day2 = models.CharField(max_length=200)
    day3 = models.CharField(max_length=200)
    day4 = models.CharField(max_length=200)
    day5 = models.CharField(max_length=200)
    day6 = models.CharField(max_length=200)

class passaeger_detail(models.Model):
    Trip_same_id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(default=10)
    username = models.CharField(max_length=10)
    Trip_date = models.DateField(null=True)
    payment = models.IntegerField(default=50)
    city = models.CharField(max_length=20)
    pay_done = models.IntegerField(default=0)

class Cards(models.Model):
    Card_number = models.CharField(primary_key=True,max_length=16)
    Ex_month = models.CharField(max_length=2)
    Ex_year = models.CharField(max_length=2)
    CVV = models.CharField(max_length=3)
    Balance = models.CharField(max_length=8,null=True)
    email = models.EmailField(max_length=50,default='faizdummimail21@gmail.com',null=True)


class NetBanking(models.Model):
    Username = models.CharField(primary_key=True, max_length=16)
    Password = models.CharField(max_length=14)
    Bank=models.CharField(max_length=25)
    Balance = models.CharField(max_length=9)

class Transactions(models.Model):
    Transactions_ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    Trip_same_id = models.IntegerField(default=1)
    Amount = models.CharField(max_length=8)
    Status = models.CharField(default="Failed", max_length=15)
    Payment_method = models.CharField(blank=True, max_length=15)
    Date_Time = models.CharField(default=timezone.now(), max_length=100)


