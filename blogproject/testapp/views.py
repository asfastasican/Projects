from django.shortcuts import render
from testapp.models import Post

# Create your views here.
def post_list(request):
    post=Post.objects.all()
    return render(request,'testapp/post_list.html',{'post':post})
