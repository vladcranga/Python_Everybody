from urllib.request import urlopen
from bs4 import BeautifulSoup

try:

    # hostname input and data parsing
    host = input('Enter the url of the website: ')
    html = urlopen(host).read()
    soup = BeautifulSoup(html, 'html.parser')

    # retrieve the span tags
    tags = soup('span')

    # initialise the sum
    sum = 0

    for tag in tags:
        # compute the sum of the values in the tag
        sum += int(tag.contents[0])

    print(sum)

except Exception:
    print("Invalid URL, please try again.")
