from urllib.request import urlopen
from xml.etree import ElementTree as ET
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# retrieve the url
address = input('Enter location: ')
print('Retrieving', address)

# read the data
data = urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')

# make the tree and find the counts
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

# loop through the counts
sum = 0
for item in counts:
    sum += int(item.text)

print('Sum:', sum)
