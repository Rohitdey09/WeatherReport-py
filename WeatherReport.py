##Current weather of a city with python
##[Note you need a account in openweathermap.com]
import request
import json
api_Key="**" #Ypur api key from the website
base_url = "http://api.openweather.org/data/2.5/waether??"
city_name = input("Enter the city name:")
complete_url=base_url+"appid="+api_Key+"&q"+city_name
response=request.get(complete_url)
x=response.json()
if x["cod"] !="404":
    y=x["main"]
    current_temperature=y["temp"]
    current_pressure=y["pressure"]
    current_pressure=y["humidity"]
    z=x["weather"]
    weather_description=z[0]["description"]
    print("Temperature(in K))="=str(current_temperature)+"\n atmospheric pressure= " + str(current_pressure)+"\n humidity= "+str(current_humidity)+ "\n description= " +str(weather_descripion))
    else:
        print("City not found")
