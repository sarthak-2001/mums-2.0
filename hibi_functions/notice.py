import requests
from bs4 import BeautifulSoup
from hibi_functions import login



limit = 50

def notice_data(uid, pwd):
    notices = []
    try:
        headers1 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                    }
        cookies = login.login(uid, pwd)
        # print(cookies)
        s = requests.Session()
        jar = requests.cookies.RequestsCookieJar()
        jar.set('PHPSESSID', cookies)
        s.cookies = jar
        s.get('https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/setWindowSize.php', headers=headers1)
        # time.sleep(0.1)

        headers2 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/?w=766&h=749'
                    }
        a = s.get('https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docList.php', headers=headers2)

        soup = BeautifulSoup(a.text, 'lxml')

        s.close()

        l=0

        all_tr = soup.find_all('tr')
        del all_tr[0]
        for r in all_tr:
            l+=1
            all_td = r.find_all('td')
            date = all_td[0].text
            title = all_td[1].text
            by = all_td[2].text
            attention = all_td[3].text
            date_text = " ".join(date.split())
            title_text = " ".join(title.split())
            by_text = " ".join(by.split())
            attention_text = " ".join(attention.split())
            link_text = all_td[1].a['href']
            unique_id_text = all_td[1].a['href'][17:]
            notice = {
                "date": date_text,
                "title": title_text,
                "posted_by": by_text,
                "attention": attention_text,
                "id_link": link_text,
                "id": unique_id_text
            }
            notices.append(notice)
            if l==limit:
                break

        return notices
    except Exception as e:
        return notices

