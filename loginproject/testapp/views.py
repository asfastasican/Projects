from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user

# Create your views here.
@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form=CreateUser()  # replica of usercreationform and customized to add email
        if request.method == 'POST':
            form=CreateUser(request.POST)
            if form.is_valid():
                form.save()

                return render(request,"testapp/Login.html")
        context={'form':form}
        return render(request,'testapp/Register.html',context)


@unauthenticated_user
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)  #making sure user exist in data base

            if user is not None:
                login(request,user)  #use to login
                return redirect("home")

            else:
                messages.info(request,"Username or password is Incorrect")
        return render(request,'testapp/Login.html')


def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def home(request):
    return render(request,"testapp/Home.html")
