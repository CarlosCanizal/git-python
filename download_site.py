import urllib.request

url = 'https://www.bbbuy.mx'

request = urllib.request.Request('https://www.bbbuy.mx/')
request.add_header('User-Agent', 'Mozilla/5.0')
request.add_header('Content-type', 'text/xml; charset="utf-8"')
response = urllib.request.urlopen(request)
webContent = response.read()
webContent = webContent.decode('utf-8')
f = open('obo-t17800628-33.html', 'w')
f.write(webContent)
f.close