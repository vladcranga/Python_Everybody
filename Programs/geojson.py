# this program doesn't work without an API key nowadays
from urllib import request, parse
from json import loads

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter location: ')

# this adds address= and encodes things like spaces, commas...
url = service_url + parse.urlencode({'address': address})
print('Retrieving:', url)
host = request.urlopen(url)  # get the handle
data = host.read().decode()  # utf-8 to unicode

try:
    js = loads(data)
except Exception:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('Failed to retrieve the data.')

    if js['status'] == 'REQUEST_DENIED':
        print('You must use an API key to authenticate each request.')

else:
    print('Retrieved', len(data), 'characters')
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat:', lat, 'long:', lng)
    location = js['results'][0]['formatted_address']
    print(location)
