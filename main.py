import weather_api

def main():
    weatherData = weather_api.getWeatherData()
    #print('Current temperature in %s is %d℃' % (weatherData['location']['name'], weatherData['current']['temperature']))

    

if __name__ == "__main__":
    main()