from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def snaps(request):
    return render(request,'snaps.html')
