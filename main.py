import weather_api
import send_message

def main():
    weatherData = weather_api.getWeatherData()
    #print('Current temperature in %s is %d℃' % (weatherData['location']['name'], weatherData['current']['temperature']))
    send_message.sendWeather(weatherData)
    


if __name__ == "__main__":
    main()
