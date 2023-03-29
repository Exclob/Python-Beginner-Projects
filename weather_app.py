import requests

def weather(country:str,api_key:str)->str:
        if isinstance(country,str):
            if country.islower() or country.isupper():
                print(f'LOCATION: {country.capitalize().strip()}')
                url = f'http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}'
                response = requests.get(url)
                if response.status_code == 200:
                    weather_data = response.json()
                    print(weather_data)
        else:
            print('You must specify a country')

weather('Venezula')
