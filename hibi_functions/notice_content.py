import requests,time
from bs4 import BeautifulSoup
from hibi_functions import login




def notice_content(uid, pwd, id):
    notices = []
    # html = ''
    full_link = ""
    try:
        cookies = login.login(uid, pwd)
        # cookies = login.login('b418018', 'Barbie17*')
        s = requests.Session()
        jar = requests.cookies.RequestsCookieJar()
        jar.set('PHPSESSID', cookies)
        s.cookies = jar

        headers = {
            'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docList.php'
        }
        url = 'https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docDet.php?docid=' + id
        x = s.get(url, headers=headers)

        soup = BeautifulSoup(x.text, 'lxml')

        # print(soup.prettify())

        html = soup.select('body > div > div')
        html = str(html[0])
        time.sleep(0.2)
        link = soup.find('a', class_='btn btn-info btn-md btn-danger')
        # print(link)

        time.sleep(0.2)

        if (link):
            half_link = link['href'][5:]
            full_link = 'https://hib.iiit-bh.ac.in/m-ums-2.0' + half_link
            # print(type(full_link))

        # notices=[]

        notice = {'html': html, 'link': full_link}
        # print(notice)
        notices.append(notice)

        return notices

    except Exception as e:
        # pass
        # print(e)
        return notices



