import requests
from bs4 import BeautifulSoup


def fees_extractor(uid,pwd):
    Notices = []

    s = requests.Session()

    headers_h = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'referer': 'https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php'}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Content-Length': '52',
               'Referer': 'https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    data = {'uid': uid, 'pwd': pwd, 'txtInput': '*', 'sub': 'Login'}

    r = s.post('https://hib.iiit-bh.ac.in/Hibiscus/Login/auth.php?client=iiit', headers=headers, data=data)

    if r.url =='https://hib.iiit-bh.ac.in/Hibiscus/Start/setWindowSize.php':
        print(r.url)
        x = r.request.headers
        cookie = x['Cookie']
        cook = cookie[10::]
        jar = requests.cookies.RequestsCookieJar()
        jar.set('PHPSESSID', cook)
        s.cookies = jar

        a = s.get('https://hib.iiit-bh.ac.in/Hibiscus/Fees/stuFee.php?stuid='+uid, headers=headers_h)


        soup = BeautifulSoup(a.text, 'lxml')

        # html = soup.html
        html = soup
        html=str(html)

        notice = {'html': html}
        Notices.append(notice)

        return Notices

    else:
        return [{"html":""}]
