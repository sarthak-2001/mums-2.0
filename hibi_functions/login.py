import requests

def login(id, password):
    flag = 0
    s = requests.Session()
    data = {'uid': id, 'pwd': password, 'txtInput': 3}

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded'
               }

    r = s.post('https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/auth.php?client=iiit', headers=headers, data=data)

    # print(r.content.decode())

    if r.url == 'https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit&mes=UserID_or_Password_Incorrect':
        flag = 0
    else:
        flag = 1
    s.close()

    if flag == 1:
        x = r.request.headers
        cookie = x['Cookie']
        cook = cookie[10::]
        return cook
    else:
        return 'fail'

