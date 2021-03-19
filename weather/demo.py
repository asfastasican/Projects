import requests

url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=eac632dfe518ba1e1575b36d26153641'
city='Las Vegas'
r=requests.get(url.format(city)).json()
city_weather={ 'city':city,
'temperature':r['main']['temp'],
'description':r['weather'][0]['description'],
'icon':r['weather'][0]['icon']
}
print(city_weather)
