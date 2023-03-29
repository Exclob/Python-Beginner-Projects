import requests

def wiki(url:str)->str:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print('Title:' + " " + data['title'])
        print('Type:' + " " + data['type'])
        print('\n')
        print('Article:' + " " + data['extract'])

wiki('https://en.wikipedia.org/api/rest_v1/page/random/summary')
