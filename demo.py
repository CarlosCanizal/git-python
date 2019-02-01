import urllib.request
with urllib.request.urlopen('https://thecomicsociety.com') as response:
    webContent = response.read()
    webContent = webContent.decode('utf-8')
    f = open('obo-t17800628-33.html', 'w')
    f.write(webContent)
    f.close