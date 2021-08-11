from urllib import request, parse
from json import loads
import ssl

# manage the API key
api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ask for the url and encode the necesary parameters
address = input('Enter location: ')
params = dict()
params['address'] = address
if api_key is not False:
    params['key'] = api_key
url = serviceurl + parse.urlencode(params)

# retrieve the data
print('Retrieving', url)
host = request.urlopen(url, context=ctx)
data = host.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = loads(data)
except Exception:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print("The JSON data couldn't be retrieved.")

# find the place_id in the JSON data and display it
place_id = (js['results'][0]['place_id'])
print("The place id of", address, "is:", place_id)
