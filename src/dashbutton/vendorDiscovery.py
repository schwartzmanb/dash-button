import requests

URL = 'https://api.macvendors.com/'

def returnManufacturor(MAC):
    apiCall = URL + MAC
    r = requests.get(url=apiCall)
    return r.text