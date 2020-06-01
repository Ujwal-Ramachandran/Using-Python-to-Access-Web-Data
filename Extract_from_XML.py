import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count = count+1
    sum = sum+x

print("Count : ",count)
print("Sum : ",sum)