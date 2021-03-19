from django.shortcuts import render,redirect
from .models import Poll
from .forms import CreatePollForm

# Create your views here.
def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,'testapp/home.html',context)

def create(request):
    if request.methos=='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['question'])
            form.save()
            return redirect('home')
    else:
        form=CreatePollForm()
    context={'form':form}
    return render(request,'testapp/create.html',context)

def vote(request,id):
    poll=Poll.objects.get(id=id)
    if request.method=='POST':
        selected_option=request.POST['poll']
        if selected_option=='option1':
            poll.option_one_count +=1
        elif selected_option=='option2':
            poll.option_two_count +=1
        elif selected_option=='option3':
            poll.option_three_count +=1
        else:
            print('Invalid Option')
        poll.save()

        return redirect('results',id)

    context={'poll':poll}
    return render(request,'testapp/vote.html',context)

def results(request,id):
    poll=Poll.objects.get(id=id)
    context={'poll':poll}
    return render(request,'testapp/result.html',context)
