from django.shortcuts import render,get_object_or_404,redirect
from testapp.models import Post
from testapp.forms import PostForm,EmailSendForm,CommentForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from .models import product

# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    try:
        posts=paginator.page(page_number)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,'testapp/post_list.html',{'posts':posts})

def post_detail_view(request,id):
    post=Post.objects.get(id=id)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'testapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

def add_post(request):
    form=PostForm()

    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    return render(request,'testapp/addpost.html',{'form':form})

def del_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/home')


def email(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{} recommends you A Post {} form rinzlers blog '.format(cd['name'],post.title)
            message='Read Post :\n {} \n Recommended by:{} \n Comments:{} '.format(post.body,cd['name'],cd['comments'])
            send_mail(subject,message,'ascorp89@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'testapp/email.html',{'form':form,'post':post,'sent':sent})

def about(request):
    return render(request,'testapp/about.html')

def logout(request):
    auth.logout(request)
    return redirect('/admin')
