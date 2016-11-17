from urllib.request import urlretrieve,urlopen,Request
from bs4 import BeautifulSoup
import re

for page in range(2, 10):
    Url = "http://pic.ali213.net/list/game/index_%s.html" % (page)
    print(Url)
    req = Request(Url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'})
    html = urlopen(req)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("(/html/)")):
        if 'href' in link.attrs:
            href = link.attrs['href']
            imageurl = "http://pic.ali213.net" + href
            print(imageurl)


