from django.shortcuts import render,redirect
import requests
from testapp.models import City
from testapp.forms import CityForm

# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=eac632dfe518ba1e1575b36d26153641'

    form=CityForm()
    if request.method=='POST':
        form=CityForm(request.POST)

        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city_count=City.objects.filter(name=new_city).count()

            if existing_city_count==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']== 200:
                    form.save()
                else:
                    print('City not found')
                return redirect('/')
            else:
                print('City already existed')


    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={ 'city':city.name,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }

        weather_data.append(city_weather)


    context={'weather_data':weather_data,'form':form}
    return render(request,'testapp/weather.html',context)
