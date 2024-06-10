from django.shortcuts import render, redirect
import json
import urllib.request
from urllib.error import HTTPError

def index(request):
    data = {}
    if request.method == 'POST':    
        city = request.POST['city']
        api_key = 'CpiGLkrEHU1kXeKyoqi7QcXWwYEYJgr3'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        try:
            with urllib.request.urlopen(url) as response:
                source = response.read()
                list_of_data = json.loads(source) 
                
                data = { 
                    "country_code": str(list_of_data['sys']['country']), 
                    "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']), 
                    "temp": str(list_of_data['main']['temp']) + 'k', 
                    "pressure": str(list_of_data['main']['pressure']), 
                    "humidity": str(list_of_data['main']['humidity']),
                    "city": city,
                }
        except HTTPError as e:
            data = {
                "error": f"HTTP Error {e.code}: {e.reason}"
            }
        except Exception as e:
            data = {
                "error": f"An error occurred: {e}"
            }
    
    return render(request, "index.html", data)
