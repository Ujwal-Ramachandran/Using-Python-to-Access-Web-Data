
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter - ")
count = int(input("Enter count - "))
pos = int(input("Enter position - "))
for i in range(0, count) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')    
    print("Retrieving:",tags[pos-1])
    url = tags[pos-1].get('href', None)
