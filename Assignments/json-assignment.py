from urllib import request
from json import loads

url = input('Enter the URL: ')

try:
    handle = request.urlopen(url)  # get the handle
    data = handle.read().decode()  # read and convert to unicode

except ValueError:
    print('Invalid URL.')

try:
    js = loads(data)
except Exception:
    js = None

if not js or 'comments' not in js:
    print('Failed to retrieve the JSON data.')
else:
    print('The JSON data has been received.')
    sum = 0
    for item in js['comments']:
        sum += int(item['count'])

print('The sum of the count values is:', sum)
