from testapp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('testapp/latestpost123.html')
def show_latest_posts():
    latest_post=Post.objects.order_by('-publish')[:3]
    return {'latest_post':latest_post}
