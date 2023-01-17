import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1379542.xml'
    
url_read = urllib.request.urlopen(url, context=ctx).read()
url_xml = ET.fromstring(url_read)
counts = url_xml.findall('.//comment')
print('Count:', len(counts))

total = []

for count in counts:
    total.append(int(count.find('count').text))
    
print(sum(total))