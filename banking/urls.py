"""
URL configuration for onlinebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from services import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("index/", views.index),
    path("AdminLoginDB/addemploy/index/", views.index),
    path("addemploy/index/", views.index),
    path("about/", views.aboutus),
    path("addemployDB/index/", views.index),
    path("AdminLoginDB/index/", views.index),
    path("adminlogin/", views.adminlogin),
    path("AdminLoginDB/", views.AdminLoginDB),
    path("logout/", views.logout),
    path("employlogin/", views.employlogin),
    path("CustomerLogin/", views.customerlogin),
    path("EmployLoginDB/", views.EmployLoginDB),
    path("CustomerLoginDB/", views.CustomerLoginDB),
    path("customerlogin/", views.customerlogin),
    path("CustomerloginDB/", views.CustomerloginDB),
    path("AdminLoginDB/viewemploy/", views.viewemploy),
    path("AdminLoginDB/addemploy/viewemploy/", views.viewemploy),
    path("viewemploy/", views.viewemploy),
    path("AdminLoginDB/ViewCustomer/", views.ViewCustomer1),
    path("AdminLoginDB/addemploy/ViewCustomer/", views.ViewCustomer1),
    path("ViewCustomer/", views.ViewCustomer1),
    path("viewcust/", views.ViewCustomer2),
    path("ViewCustomer11/", views.ViewProfile),
    path("AdminLoginDB/addemploy/", views.addemploy),
    path("addemployDB/", views.addemployDB),
    path("addemploy/addemployDB/", views.addemployDB),
    path("addemploy/", views.addemploy),
    path("addcust/", views.addcustomer),
    path("newaccount/", views.newaccount),
    path("addcustDB/", views.addcustomerDB),
    path("newDB/", views.newaccountDB),
    path("edit/", views.edit),
    path("UpdateEmployDB/", views.UpdateEmployDB),
    path("deleteEmploy/", views.deleteEmploy),
    path("deposit/", views.deposit),
    path("depositDB/", views.depositDB),
    path("withdrawl/", views.withdrawl),
    path("withdrawlDB/", views.withdrawlDB),
    path("transfer/", views.transfer),
    path("transferDB/", views.transferDB),
    path("aboutus/", views.index1),
    path("custprofile/", views.ViewProfile1),
    path("ViewEmployee/", views.ViewProfile),
]
