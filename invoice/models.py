from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField(null=True)
    password=models.CharField(max_length=50)

    class Meta:
        db_table="user_signup"

class AddProduct(models.Model):
    pname=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=200,null=True)
    cat=models.CharField(max_length=100,null=True)
    sub_cat=models.CharField(max_length=100,null=True )
    weight=models.BigIntegerField(null=True)
    unit=models.CharField(max_length=100,null=True)
    qty=models.BigIntegerField(null=True)
    amount=models.BigIntegerField(null=True)
    



    class Meta:
        db_table="add_product"
