import requests, login
from bs4 import BeautifulSoup

cookies = login.login('B418018', 'Barbie17*')
# print(cookies)
s = requests.Session()
jar = requests.cookies.RequestsCookieJar()
jar.set('PHPSESSID', cookies)
s.cookies = jar

headers = {
    'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docDet.php?docid=11217'
}
x=s.get('https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docDet.php?docid=11217',headers=headers)

soup = BeautifulSoup(x.text,'lxml')
# print(soup.prettify())
xx=soup.select('body > div > div > div > div.col-sm-12.table-responsive')
# body > div > div > div > div.col-sm-12.table-responsive
print(xx)