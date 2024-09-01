from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    password = models.CharField(max_length=55)
    esal = models.CharField(max_length=25)
    class Meta:  
        db_table = "employee" 



class Customer(models.Model):  
    ano = models.CharField(max_length=20)  
    cname = models.CharField(max_length=60)
    cadd = models.CharField(max_length=200)  
    cemail = models.EmailField()  
    ccontact = models.CharField(max_length=15)
    cpassword = models.CharField(max_length=55)
    cbal = models.CharField(max_length=15)
    class Meta:  
        db_table = "customer"
