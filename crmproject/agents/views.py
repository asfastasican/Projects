from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.views import generic
from agents.form import AgentForm

# Create your views here.

class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name='Agents/Agent_list.html'

    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin,generic.CreateView):
     template_name='Agents/Agent_Create.html'
     form_class=AgentForm

     def get_sucess_url(self):
         return reverse("agentlist")

    #overriding the form valid method to add organization manually
     def form_valid(self, form):
        Agent=form.save(commit=False) #not saving in db
        Agent.organisation=self.request.user.userprofile #grabing the userprofile from request
        Agent.save()
        return super(AgentCreateView, self).from_valid(form)

class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='Agents/AgentDetails.html'

    def get_queryset(self):
        return Agent.objects.all()
    

    
