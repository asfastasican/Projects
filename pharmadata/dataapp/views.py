from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import *
from .models import *
from math import pi
import pandas as pd
from bokeh.palettes import Category20c,Spectral6
from bokeh.plotting import figure
from bokeh.transform import cumsum,dodge,factor_cmap
from bokeh.models import ColumnDataSource, FactorRange,LabelSet
from bokeh.embed import components
# Create your views here.

####                                                         ######
 ######Authentication 1.login ...2.Logout... and 3.Registration #####
####                                                         ######

@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is Invalid')
            return redirect('login')
    return render(request,"dataapp/Login.html")

@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form=CreateUser()  # replica of usercreationform and customized to add email
        if request.method == 'POST':
            form=CreateUser(request.POST)
            if form.is_valid():
                form.save()

                return render(request,"dataapp/Login.html")
        context={'form':form}
        return render(request,'dataapp/Register.html',context)



@login_required
def logoutpage(request):
    logout(request)
    return redirect('login')

####                                                         ######
 ###### View functions for Home.......and....product..........  #####
####                                                         ######

#@login_required(login_url = 'login')
def home(request):
    doc=Doctor.objects.count()
    med=Medical.objects.count()
    org=Organization.objects.count()

    x = {
    'Doctor': doc,
    'Medical': med,
    'Organization': org
    }
    #for customer counts
    customer_count=doc+med+org
    print("the customer count is :" ,customer_count)
    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'Customer'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p1 = figure(plot_height=250, tools="pan,wheel_zoom,box_zoom,reset, hover",plot_width=450, title="Customers",
        tooltips="@Customer: @value")

    p1.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="royalblue", fill_color='color', legend='Customer', source=data)
    source = ColumnDataSource(data)

    labels = LabelSet(x=0, y=1, text='value',
            angle=cumsum('angle', include_zero=True), source=source, render_mode='canvas')

    p1.add_layout(labels)
    p1.background_fill_color = "ivory"
    p1.background_fill_alpha = 0.2
    p1.legend.background_fill_color = "ivory"
    p1.legend.background_fill_alpha = 0.2
    p1.legend.label_standoff = 2
    p1.legend.glyph_width = 20
    p1.legend.spacing = 2
    p1.legend.padding = 2
    p1.legend.margin = 2
    p1.border_fill_color = "ivory"
    p1.border_fill_alpha =0.6

    #plot for stocks
    names=list(Product.objects.values('name'))
    currents=Stocks.objects.values('current_quantity')
    current_stock=[]
    product_name=[]

    #grabbing data and extracting data from queryset
    for n in names:
        product_name.append(n['name'])

    for c in currents:
        current_stock.append(c['current_quantity'])

    #bokeh stuff
    products=product_name
    counts=current_stock

    #Current Stock and Product count
    current_stock_total=sum(current_stock)
    product_count=Product.objects.count()

    #Plotting of Figure
    source = ColumnDataSource(data=dict(products=products, counts=counts, color=Spectral6))
    p2 = figure(x_range=products, plot_height=250,plot_width=600, title="Product Units Available",
        tools="pan,wheel_zoom,box_zoom,reset, hover")

    #Formatting of figure
    p2.vbar(x='products', top='counts', width=0.9, color='color',line_color="palevioletred", source=source)
    p2.xgrid.grid_line_color = None
    p2.background_fill_color = "ivory"
    p2.background_fill_alpha = 0.2
    p2.border_fill_color = "ivory"
    p2.border_fill_alpha =0.6

    #Figure3
    # plot for Quaterly Sale Graph
    data=Sale.objects.values()
    names=Product.objects.values('name')
    sale_pro=[]
    Q1=[]
    Q2=[]
    Q3=[]
    Q4=[]


    #Grabing the Product name
    for y in names:
        sale_pro.append(y['name'])

    #grabing the Quaters data
    for d in data:
        Q1.append(d['quater1_sale'])
        Q2.append(d['quater2_sale'])
        Q3.append(d['quater3_sale'])
        Q4.append(d['quater4_sale'])

    #data Preparation
    Products=sale_pro
    Quaters = ['Q1', 'Q2', 'Q3','Q4']

    #Counting the Total Product
    total_product_sale=sum(Q1)+sum(Q2)+sum(Q3)+sum(Q4)

    #Assembling the Data for Figure
    data = {'Products' : Products,
        'Q1'   : Q1,
        'Q2'   : Q2,
        'Q3'   : Q3,
        'Q4'   : Q4,
        }

    #Plotting the Figure
    x = [ (Product, Quater) for Product in Products for Quater in Quaters ]
    counts = sum(zip(data['Q1'], data['Q2'], data['Q3'],data['Q4']), ())
    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p3 = figure(x_range=FactorRange(*x), plot_height=250,plot_width=600, title="Quaterly Sale of Product",
        tools="pan,wheel_zoom,box_zoom,reset, hover, crosshair")

    #Formatting of third figure
    p3.vbar(x='x', top='counts', width=0.9, source=source,line_color="palevioletred",
        fill_color=factor_cmap('x', palette=Spectral6,factors=Quaters, start=1, end=2))
    p3.x_range.range_padding = 0.1
    p3.xgrid.grid_line_color = None
    p3.background_fill_color = "ivory"
    p3.background_fill_alpha = 0.3
    p3.border_fill_color = "ivory"
    p3.border_fill_alpha =0.6

    #passing all plots to components function for ploting/Drawing it.
    script, div = components(p1)
    script2,div2=components(p2)
    script3,div3=components(p3)


    return render(request,'dataapp/home.html',{'script': script, 'div':div,'script2':script2,'div2':div2,'script3':script3,'div3':div3,'total_product_sale':total_product_sale,"current_stock_total":current_stock_total,"customer_count":customer_count,"product_count":product_count})

def product_details(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'dataapp/product_detail.html',context)

def addproduct(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    return render(request,'dataapp/addproduct.html',{'form':form})

def productinfo(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'dataapp/productinfo.html',context)

def updateproduct(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/detail')
    return render(request,'dataapp/updateproduct.html',{'product':product})

def deleteproduct(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('product')

####
    ####                                                         ######
     ######.................View functions Customes...............  #####
    ####                                                         ######
####

# views for customer.
#Doctor Related Functions
def doctor_details(request):
    doctor=Doctor.objects.all()
    return render(request,'customer/Doctor.html',{'doctor':doctor})

def adddoctor(request):
    form=DoctorForm()
    if request.method=='POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctor_details')
    return render(request,'customer/adddoctor.html',{'form':form})

def doctor_info(request,id):
    info=Doctor.objects.get(id=id)
    return render(request,'customer/doctorinfo.html',{'info':info})

def deletedoctor(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/doctordetails')

#Medical Related Functions
def medical_details(request):
    medical=Medical.objects.all()
    return render(request,'customer/Medical.html',{'medical':medical})

def addmedical(request):
    form=MedicalForm()
    if request.method=='POST':
        form=MedicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medical_details')
    return render(request,'customer/addmedical.html',{'form':form})

def medical_info(request,id):
    info=Medical.objects.get(id=id)
    return render(request,'customer/medicalinfo.html',{'info':info})

def deletemedical(request,id):
    medical=Medical.objects.get(id=id)
    medical.delete()
    return redirect('/medicaldetails')

#Organization Related Functions
def org_details(request):
    organization=Organization.objects.all()
    return render(request,'customer/Organization.html',{'organization':organization})

def addorg(request):
    form=OrganizationForm()
    if request.method=='POST':
        form=OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orgdetails')
    return render(request,'customer/addorg.html',{'form':form})

def org_info(request,id):
    info=Organization.objects.get(id=id)
    return render(request,'customer/orginfo.html',{'info':info})

def deleteorg(request,id):
    org=Organization.objects.get(id=id)
    org.delete()
    return redirect('/orgdetails')

####
    ####                                                         ######
     ######.................View functions for Stocks..............  #####
    ####                                                         ######
####
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource,LabelSet
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.embed import components

def stocks(request):
    stocks=Stocks.objects.all()
    context={"stocks":stocks}
    return render(request,"stocks/stocks.html")

def add_stock(request):
    form=StocksAddForm()
    if request.method == 'POST':
        form=StocksAddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("stocks")
