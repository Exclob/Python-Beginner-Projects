import requests

def random_quote(api):
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()[0]
        print(data['q'])

random_quote('https://zenquotes.io/api/random')