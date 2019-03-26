import requests
import os
from datetime import datetime

def main():
    #get the environment variable key
    key = os.environ.get('APIKey')
    #store the url
    url = 'http://api.openweathermap.org/data/2.5/forecast'

    #printing a welcome message
    print('Welcome to your five day forecast!')
    #getting user input for city and country
    city = input('Enter the name of the city you want the weather forecast for. ')
    country = input('Enter the 2 character country abbreviation. ')
    #setting parameters
    parameters = {'q': '', 'units': 'imperial', 'appid': key }
    parameters['q'] = city.lower() + ',' + country.lower()

    #make the request
    # get the data
    response = requests.get(url, params=parameters).json()
    print(response)

    #print forecast with converted time
    forecasts = response['list']
    for forecast in forecasts:
        #convert the date time to local time so it is relevant to the user
        time = forecast['dt']
        date = datetime.fromtimestamp(time)
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        windSpeed = forecast['wind']['speed']
        print(f'The weather @ {date} is {description} with a temp of {temp}F, and a wind speed of {windSpeed}.')


main()