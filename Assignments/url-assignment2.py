from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input section
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

while count >= 0:
    print('Retrieving:', url)

    # set up BeautifulSoup
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    # extract the needed information
    tag = tags[position-1].contents[0]
    href = tags[position-1].get('href', None)

    # continue the loop
    url = href
    count -= 1
