from django.shortcuts import render
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def search(request):

    if request.method == 'POST':
        state_name=request.POST['search_text'].capitalize() #grabed searched data and put in state_name
        state_code_data=pd.read_csv("state_code.csv")
        print(state_code_data.head())
        state_code = state_code_data.loc[state_code_data['State'] == state_name, 'State_code'].iloc[0]  # searched statename in state_code_data[csv] and grabed that row wich will be state code
        url = "https://www.covid19india.org/state/"+state_code
        print('State Name :', state_name)
        print('State Code :', state_code)

        #selenium code to grab state map
        driver=webdriver.Chrome()
        driver.get(url)
        map_div=driver.find_element(By.ID,'chart') #grabed the element and stored in variable
        html_code=map_div.getAttribute('outerHTML')
        driver.quit()

        
