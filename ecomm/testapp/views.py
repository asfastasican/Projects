from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from testapp.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import *
from testapp.forms import AddProductForm

# Create your views here.
@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)

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

@login_required(login_url = 'login')
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'testapp/home.html',context)

@login_required
def cart(request):
    customer = request.user.customer
    order, create=Order.objects.get_or_create(customer = customer,ordered=False)  #will grab orders grleted to customer or will create one
    items = order.orderitem_set.all()   #grabed all items related to that order
    orderitem=OrderItem.objects.all()
    context = {'items':items,'order':order,'orderitem':orderitem}
    return render(request,'testapp/cart.html',context)

def checkout(request):
    customer = request.user.customer
    order, create=Order.objects.get_or_create(customer = customer,ordered = False)
    items = order.orderitem_set.all()
    context = {'items':items,'order':order}
    return render(request,'testapp/checkout.html',context)

def product_view(request,id):
    product = Product.objects.get(id = id)
    context = {"product":product}
    return render(request,"testapp/view.html",context)

def addtocart(request,id):
    customer = request.user.customer
    order, create = Order.objects.get_or_create(customer = customer,ordered=False)
    items = order.orderitem_set.all()
    product = Product.objects.get(id = id)
    existing_orderitem_count = OrderItem.objects.filter(product = product).count()
    if existing_orderitem_count == 0:
        orderitem = OrderItem.objects.create(product = product,order = order)
        print(existing_orderitem_count)
    else:
        orderitem=OrderItem.objects.get(product = product)
        orderitem.quantity=orderitem.quantity +1
    return redirect("home")

def about(request):
    return render(request,"testapp/about.html")

def add_product(request):
    form=AddProductForm()
    if request.method == "POST":
        form=AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context={"form":form}
    return render(request,"testapp/add_product.html",context)

def delete_orderitem(request,id):
    orderitem=OrderItem.objects.get(id=id)
    orderitem.delete()
    return redirect("cart")
