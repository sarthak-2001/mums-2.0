import time
from bs4 import BeautifulSoup
import requests
import re

#-----------------------------------------------
#LOGGING IN AND GETTING TILL NOTICE
#-----------------------------------------------

s=requests.Session()

headers1={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
         }
headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Content-Length': '37',
         'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit',
            'Connection':'keep-alive',
         'Content-Type':'application/x-www-form-urlencoded'
         }

data={'uid':'B18','pwd':'fdgfge17*','txtInput':3}

r=s.post('https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/auth.php?client=iiit',headers=headers,data=data)

if r.url == 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit&mes=UserID_or_Password_Incorrect':
    print('wrong id or password')
else:
    print('pass')


# print(r.request.headers)
# print()
# print()
# print(r.headers)
# print()

# print(r.content)
x=r.request.headers
# cookie={'Cookie':x['Cookie']}
cookie=x['Cookie']
cook = cookie[10::]

jar=requests.cookies.RequestsCookieJar()
jar.set('PHPSESSID',cook)
s.cookies = jar
#
s.get('https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/setWindowSize.php',headers=headers1)
time.sleep(1)
#
headers2={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer' : 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/?w=766&h=749'
         }
a=s.get('https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docList.php',headers=headers2)
#

# print(a.request.headers,'\n\n')
# print(a.headers,'\n\n')
# with open('x.html','w') as w:
#     w.write(a.content.decode())
# print(a.content.decode())

# #-----------------------------------------------
# #GETTING NOTICE HEADINGS
# #-----------------------------------------------
#
# # final = a.text
# # print(final)
soup = BeautifulSoup(a.text,'lxml')
#
text=re.compile('LOV')
#
#
# # for link in soup.find_all(class_=text):
# #     print(link.a.text)
#
# #-----------------------------------------------
# #GETTING NOTICE TEXT
# #-----------------------------------------------
notice_text = []
notice_header = {
    'Referer':'https://hib.iiit-bh.ac.in/Hibiscus/NoticeBoard/docList.php',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
limit=0

# for link in soup.find_all(class_=text):
#
#     l = 'https://hib.iiit-bh.ac.in/Hibiscus/NoticeBoard/'+link.a['href']
#     s.get(l,headers=notice_header)


link =soup.find(class_=text)
# time.sleep(1)
l = 'https://hib.iiit-bh.ac.in/Hibiscus/NoticeBoard/'+link.a['href']
# print(l)
x = s.get(l,headers=notice_header)
time.sleep(1)
# print(x.content)
notice_soup = BeautifulSoup(x.text,'lxml')
# print(notice_soup.prettify())
# print(notice_soup.find(class_='even').text)
xx=notice_soup.select('body > div > div:nth-child(4)').html()
print(xx)

