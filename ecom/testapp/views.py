from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from testapp.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is Invalid')
            return redirect('login')
    return render(request,"testapp/Login.html")

@login_required
def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'testapp/home.html',context)

@login_required
def cart(request):
    customer=request.user.customer
    order, create=Order.objects.get_or_create(customer=customer,complete=False)  #will grab orders grleted to customer or will create one
    items=order.orderitem_set.all()   #grabed all items related to that order
    context={'items':items,'order':order}
    return render(request,'testapp/cart.html',context)

def checkout(request):
    customer=request.user.customer
    order, create=Order.objects.get_or_create(customer=customer,ordered=False)
    items=order.orderitem_set.all()
    context={'items':items,'order':order}
    return render(request,'testapp/checkout.html',context)

def product_view(request,id):
    product=Product.objects.get(id=id)
    context={"product":product}
    return render(request,"testapp/view.html",context)

def addtocart(request,id):
    product=Product.object.get(id=id)
