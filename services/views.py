from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
import mysql.connector
from services.models import Employee
from services.models import Customer


con=mysql.connector.connect(database='bank1',user='root',password='')
cur=con.cursor()

def index(request):  
    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render())

def aboutus(request):  
    template = loader.get_template('aboutus.html') # getting our template  
    return HttpResponse(template.render())

def adminlogin(request):  
    template = loader.get_template('testbank.html') # getting our template  
    return HttpResponse(template.render()) 

def employlogin(request):  
    template = loader.get_template('EmployeeLogin.html') # getting our template  
    return HttpResponse(template.render())

def customerlogin(request):  
    template = loader.get_template('CustomerLogin.html') # getting our template  
    return HttpResponse(template.render())

def addemploy(request):  
    template = loader.get_template('addempl.html') # getting our template  
    return HttpResponse(template.render())
def addcustomer(request):  
    template = loader.get_template('EmployeeAddCustomer.html') # getting our template  
    return HttpResponse(template.render())

def newaccount(request):  
    template = loader.get_template('CustomerNewAcc.html') # getting our template  
    return HttpResponse(template.render())

def customerlogin(request):  
    template = loader.get_template('CustomerLogin.html') # getting our template  
    return HttpResponse(template.render())

def addcustomerDB(request):
    cano=request.GET.get("t1")
    name=request.GET.get("t2")
    add=request.GET.get("t3")
    mail=request.GET.get("t4")
    cont=request.GET.get("t5")
    password=request.GET.get("t6")
    bal=request.GET.get("t7")
    data=Customer(ano=cano,cname=name,cadd=add,cemail=mail,ccontact=cont,cpassword=password,cbal=bal)
    data.save()
    template = loader.get_template('EmployeeHome.html') # getting our template  
    return HttpResponse(template.render())

def newaccountDB(request):
    cano=request.GET.get("t1")
    name=request.GET.get("t2")
    add=request.GET.get("t3")
    mail=request.GET.get("t4")
    cont=request.GET.get("t5")
    password=request.GET.get("t6")
    bal=request.GET.get("t7")
    data=Customer(ano=cano,cname=name,cadd=add,cemail=mail,ccontact=cont,cpassword=password,cbal=bal)
    data.save()
    template = loader.get_template('CustomerLogin.html') # getting our template  
    return HttpResponse(template.render())

def addemployDB(request):
    eid=request.GET.get("t1")
    name=request.GET.get("t2")
    mail=request.GET.get("t3")
    cont=request.GET.get("t4")
    password=request.GET.get("t5")
    sal=request.GET.get("t6")
    data=Employee(eid=eid,ename=name,eemail=mail,econtact=cont,password=password,esal=sal)
    data.save()
    template = loader.get_template('adminm.html') # getting our template  
    return HttpResponse(template.render())

def AdminLoginDB(request):
    
    un=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    if un=='admin' and pwd=='admin':
        template = loader.get_template('adminm.html') # getting our template  
        return HttpResponse(template.render())
    else:
        template = loader.get_template('testbank.html') # getting our template  
        return HttpResponse(template.render()) 


def EmployLoginDB(request):
    
    un=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    s="select * from employee where eemail='"+un+"' and password='"+pwd+"'"
    cur.execute(s)
    d=cur.fetchall()
    if len(d)>0:
        request.session['id']=d[0][0]
        template = loader.get_template('EmployeeHome.html') # getting our template  
        return HttpResponse(template.render())
    else:
        template = loader.get_template('EmployeeLogin.html') # getting our template  
        return HttpResponse(template.render())
def CustomerLoginDB(request):
    
    un=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    s="select * from customer where cemail='"+str(un)+"' and cpassword='"+str(pwd)+"'"
    cur.execute(s)
    d=cur.fetchall()
    if len(d)>0:
        request.session['id']=d[0][0]
        template = loader.get_template('CustomerHome.html') # getting our template  
        return HttpResponse(template.render())
    else:
        template = loader.get_template('CustomerLogin.html') # getting our template  
        return HttpResponse(template.render())

def logout(request):  
    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render())




def CustomerloginDB(request):
    
    un=request.GET.get('uname')
    pwd=request.GET.get('psw')
    s="select * from customer where cemail='"+un+"' and cpassword='"+pwd+"'"
    cur.execute(s)
    d=cur.fetchall()
    if len(d)>0:
        template = loader.get_template('CustomerHome.html') # getting our template  
        return HttpResponse(template.render())
    else:
        template = loader.get_template('CustomerLogin.html') # getting our template  
        return HttpResponse(template.render()) 

def logout(request):  
    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render())
def viewemploy(request):
    employees = Employee.objects.all()
    return render(request,"viewempl.html",{'employees':employees})

def ViewCustomer(request):
    customers = Customer.objects.all()
    return render(request,"CustomerViewPro.html",{'customers':customers})
def ViewCustomer2(request):
    customers = Customer.objects.all()
    return render(request,"EmployeeViewCustomer.html",{'customers':customers})
def ViewCustomer1(request):
    customers = Customer.objects.all()
    return render(request,"viewcust.html",{'customers':customers})

def edit(request):
    eid=request.GET.get('eid')
    employees = Employee.objects.filter(id=eid)
    return render(request,"editemploy.html",{'employees':employees})


def ViewProfile(request):
    eid=request.session['id']
    employees = Employee.objects.filter(id=eid)
    return render(request,"ViewEmployee.html",{'employees':employees})

def ViewProfile1(request):
    eid=request.session['id']
    customers = Customer.objects.filter(id=eid)
    return render(request,"CustomerViewPro.html",{'customers':customers})



def UpdateEmployDB(request):
    id=request.GET.get("t0")
    eid=request.GET.get("t1")
    name=request.GET.get("t2")
    mail=request.GET.get("t3")
    cont=request.GET.get("t4")
    password=request.GET.get("t5")
    sal=request.GET.get("t6")
    Employee.objects.filter(id=id).update(eid=eid,ename=name,eemail=mail,econtact=cont,password=password,esal=sal)
    
    template = loader.get_template('adminhome.html') # getting our template  
    return HttpResponse(template.render())


def deleteEmploy(request):
    id=request.GET.get("eid")
    Employee.objects.filter(id=id).delete()
    template = loader.get_template('adminhome.html') # getting our template  
    return HttpResponse(template.render())

def deposit(request):
    template = loader.get_template('EmployeeDeposit.html') # getting our template  
    return HttpResponse(template.render())


def depositDB(request):
    
    ano=request.GET.get('t1')
    damt=request.GET.get('t2')
    s="select * from customer where ano="+ano
    cur.execute(s)
    d=cur.fetchall()
    Customer.objects.filter(id=d[0][0]).update(cbal=float(d[0][-1])+float(damt))    
    template = loader.get_template('EmployeeHome.html') # getting our template  
    return HttpResponse(template.render())

def withdrawl(request):
    template = loader.get_template('EmployeeWithdrawl.html') # getting our template  
    return HttpResponse(template.render())


def withdrawlDB(request):
    ano=request.GET.get('t1')
    wamt=request.GET.get('t2')
    s="select * from customer where ano="+ano
    cur.execute(s)
    d=cur.fetchall()
    Customer.objects.filter(id=d[0][0]).update(cbal=float(d[0][-1])-float(wamt))    
    template = loader.get_template('EmployeeHome.html') # getting our template  
    return HttpResponse(template.render())

def transfer(request):
    template = loader.get_template('CustomerTransfer.html') # getting our template  
    return HttpResponse(template.render())


def transferDB(request):
    ano=request.GET.get('t1')
    tano=request.GET.get('t2')
    tamt=request.GET.get('t3')
    s="select * from customer where ano="+ano
    cur.execute(s)
    d=cur.fetchall()
    Customer.objects.filter(id=d[0][0]).update(cbal=float(d[0][-1])-float(tamt))

    
    s="select * from customer where ano="+tano
    cur.execute(s)
    d=cur.fetchall()
    Customer.objects.filter(id=d[0][0]).update(cbal=float(d[0][-1])+float(tamt))    
    template = loader.get_template('CustomerHome.html') # getting our template  
    return HttpResponse(template.render())


def index1(request):  
    template = loader.get_template('aboutus.html') # getting our template  
    return HttpResponse(template.render())
    

