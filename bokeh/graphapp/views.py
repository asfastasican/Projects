from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

# Create your views here.
def home(request):
    first_graph="First Graph"
    return render(request,"graphapp/home.html")

def starter(request):
    plot=figure()
    plot.circle([1,10,35,27],[0,0,0,0],size=20,color="blue")
    script,div=components(plot)
    return render(request,"graphapp/starter.html",{"script":script,"div":div})
