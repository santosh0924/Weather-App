#   File: Assignment 12.1
#   Name: Santosh Omprakash
#   Assignment number: 12.1
#   Description: This module returns weather forecast based on Zip code or City name entered by user

import requests
import datetime

# function to call openweathermap to get weather forecast based on zip code
def call_weather_zip(userInp):
    apiKey = '6429d6c9beeca1075a4517138499d263'
    webSite = 'http://api.openweathermap.org/data/2.5/weather?lat=0&lon=1&units=imperial&appid='
    weather_req = requests.get(webSite + apiKey)
    try:
        weather_req.raise_for_status()
# 200 is successful return code
        if weather_req.status_code == 200:
            passValue = 'http://api.openweathermap.org/data/2.5/weather?' + "appid=" + apiKey + "&zip=" + userInp
            try:
                response = requests.get(passValue)
                response.raise_for_status()
                getWeather = response.json()
                weather_display(getWeather)
            except requests.exceptions.HTTPError:
                print('Invalid Zip code entered, please try again!')
        else:
            print('Connection was not successful, please try again!')
    except requests.exceptions.HTTPError as e:
        print('Connection was not successful, please try again!')
        return "Error: " + str(e)

# function to call openweathermap to get weather forecast based on city name
def call_weather_city(userInp):
    apiKey = '6429d6c9beeca1075a4517138499d263'
    webSite = 'http://api.openweathermap.org/data/2.5/weather?lat=0&lon=1&units=imperial&appid='
    weather_req = requests.get(webSite + apiKey)
    try:
        weather_req.raise_for_status()
# 200 is successful return code
        if weather_req.status_code == 200:
            passValue = 'http://api.openweathermap.org/data/2.5/weather?' + "appid=" + apiKey + "&q=" + userInp
            try:
                response = requests.get(passValue)
                response.raise_for_status()
                getWeather = response.json()
                weather_display(getWeather)
            except requests.exceptions.HTTPError:
                print('Invalid City or Zip entered, please try again!')
        else:
            print('Connection was not successful, please try again!')
    except requests.exceptions.HTTPError as e:
        print('Connection was not successful, please try again!')
        return "Error: " + str(e)

#function to format the values in openweathermap and display in readable/standard format
def weather_display(getWeather):
    weathr_main = getWeather['main']
    city = getWeather['name']
    weathr = getWeather['weather']
    tempe = weathr_main['temp']
    min_temp = weathr_main['temp_min']
    max_temp = weathr_main['temp_max']
    humidity = weathr_main['humidity']
#convert temperature from Kelvin to Fahrenheit
    tempe_far = (9 * (tempe - 273.15))/5 + 32
    min_far = (9 * (min_temp - 273.15))/5 + 32
    max_far = (9 * (max_temp - 273.15))/5 + 32
    print('Weather information is below:')
    print('Location -', city)
    for item in weathr:
        print('Conditions -', (item['description']))
    tempf = int(float(tempe_far))
    minTempF = int(float(min_far))
    maxTempF = int(float(max_far))
#display temperature in degree Fahrenheit
    print('Temperature -', str(tempf) +'\u00b0F')
    print('Minimum Temp -', str(minTempF) + '\u00b0F')
    print('Maximum Temp -', str(maxTempF) + '\u00b0F')
    SunRS = getWeather['sys']
    sunR = SunRS['sunrise']
    sunS = SunRS['sunset']
#convert time to standard format
    conv_sunR = datetime.datetime.fromtimestamp(int(sunR)).strftime('%I:%M %p')
    conv_sunS = datetime.datetime.fromtimestamp(int(sunS)).strftime('%I:%M %p')
    print('Sunrise -', conv_sunR)
    print('Sunset -', conv_sunS)
    winds = getWeather['wind']
    wind_speed = winds['speed']
#convert wind speed from meters per second to miles per hour
    conv_windS = wind_speed * 2.237
    round_windS = round(conv_windS, 1)
    print('Wind -', str(round_windS), 'mph')
    print('Humidity -', str(humidity) + '%')

# main section to receive zip or city from user. Program ends when user enters 'terminate'.
def main():
    print('Welcome to THE WEATHER APP!')
    while True:
        userInp = input('Please enter zip code or city for weather forecast! Enter terminate to stop\n')
        if userInp.isdigit():                                       #get forecast if zip code is entered
            call_weather_zip(userInp)
        elif userInp == 'terminate':
            print('Thank you for using THE WEATHER APP')
            break
        else:                                                       #get forecase if city is entered
            call_weather_city(userInp)

if __name__ == "__main__":
    main()
