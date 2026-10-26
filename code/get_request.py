import requests
import json

try:
    url ='https://api.open-meteo.com/v1/forcast?latitude=35&lognitude=139&hourly=temperature_2m'
    response =requests.get(url);
    print(response.status_code)
    print(response.headers)
    print (response.text)
    data=response.json()
    print(json.dumps(response.json(), indent=4))
    print(data['hourly']['temperature_2m'])
except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')


