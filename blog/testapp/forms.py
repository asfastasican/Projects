from django.forms import ModelForm
from django import forms
from testapp.models import Post
from testapp.models import Comment

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields="__all__"

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body',)
