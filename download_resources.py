import urllib.request
from os.path import basename
from urllib.parse import urlsplit
from bs4 import BeautifulSoup # for HTML parsing

global urlList
urlList = []

# recursively download images starting from the root URL
def downloadImages(url, level): # the root URL is level 0
    print(url)
    global urlList
    if url in urlList: # prevent using the same URL again
        return
    urlList.append(url)
    try:
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        request.add_header('Content-type', 'text/xml; charset="utf-8"')
        urlContent = urllib.request.urlopen(request).read()
    except Exception as e:
        raise e;

    print("continue")
    soup = BeautifulSoup(urlContent)
    # find and download all images
    imgTags = soup.findAll('img')
    for imgTag in imgTags:
        imgUrl = imgTag['src']
        print(imgUrl)
        try:
            requestImg = urllib.request.Request(imgUrl)
            requestImg.add_header('User-Agent', 'Mozilla/5.0')
            imgData = urllib.request.urlopen(requestImg).read()
            fileName = basename(urlsplit(imgUrl)[2])
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
        except Exception as e:
            raise e

    # if there are links on the webpage then recursively repeat
    if level > 0:
        linkTags = soup.findAll('a')
        if len(linkTags) > 0:
            for linkTag in linkTags:
                try:
                    linkUrl = linkTag['href']
                    downloadImages(linkUrl, level - 1)
                except:
                    pass

# main
downloadImages('https://www.bbbuy.mx', 0)