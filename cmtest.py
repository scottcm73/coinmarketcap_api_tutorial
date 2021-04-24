from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint 
import os

key=os.environ.get('COINMARKETCAP_API_KEY')
pp = pprint.PrettyPrinter(indent=4)

url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
print(url)
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key,
}
parameters = {
'id':'1,2,3,4'

}

session = Session()
session.headers.update(headers)
try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    pp.pprint(data)
    

except (ConnectionError, Timeout, TooManyRedirects) as e:
    data = json.loads(response.text)
    pp.pprint(data)