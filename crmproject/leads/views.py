from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class=UserCreationForm

    def get_success_url(self):
        return reverse('lead-list')


def landing_page(request):
    return render(request,'leads/landing.html')

def lead_list(request):
    leads=lead.objects.all()
    context={
        'leads':leads
    }
    return render(request,'leads/lead_list.html',context)
    
def lead_detail(request,pk):
    leads=lead.objects.get(pk=pk)
    context={
        'leads':leads
    }
    return render(request,'leads/lead_detail.html',context)


class LeadCreate(generic.CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadForm

    def get_success_url(self):
        return reverse('lead-list')

    def form_valid(self,form):
        send_mail(
            subject="A lead has been created",
            message="Go to site to check new lead",
            from_email="test@test.com",
            recipient_list=['test2@test.com']
        )
        return super(LeadCreate, self).form_valid(form)


def lead_update(request,id):
    led=lead.objects.get(id=id)
    form=LeadForm(instance=led)
    if request.method == 'POST':
        form=LeadForm(request.POST,instance=led)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form,'led':led}
    return render(request,'leads/lead_update.html',context)

def lead_delete(request,id):
    led=lead.objects.get(id=id)
    led.delete()
    return redirect('/')


def logoutredirect(request):
    return render(request,'leads/logoutredirect.html')