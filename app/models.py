from django.db import models
class Register(models.Model):
    name=models.IntegerField(primary_key=True)
    foodname=models.FileField(upload_to="profile_pice/",blank=True )
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    Total=models.CharField(max_length=30)
    Booking=models.CharField(max_length=30)
    Date=models.DateField(auto_now_add=True)
    discount=models.CharField(max_length=30)
class Food(models.Model):
    Quality=models.CharField(max_length=30)
    Date = models.DateField(auto_now_add=True)
class FoodAmmount(models.Model):
    Total = models.CharField(max_length=30)
    Date = models.DateField(auto_now_add=True)

class FoodMaxmam(models.Model):
    foodname=models.FileField(upload_to="profile_pice/",blank=True )
    Booking=models.CharField(max_length=30)
class Fooditems(models.Model):
    name = models.IntegerField(primary_key=True)
    Quality=models.CharField(max_length=30)
    Date = models.DateField(auto_now_add=True)
class Fooitem(models.Model):
    name = models.IntegerField(primary_key=True)
    Quality = models.CharField(max_length=30)



