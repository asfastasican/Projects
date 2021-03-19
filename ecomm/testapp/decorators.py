from django.shortcuts import render,redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):   # will take view func as argument

    def wrap_func(request,*args,**kwargs):
        if request.user.is_authenticated:   #is_authenticated will check is user already login
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrap_func
