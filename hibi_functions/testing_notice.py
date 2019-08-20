from bs4 import BeautifulSoup
f=open('x.html')
soup = BeautifulSoup(f,'lxml')
f.close()
# print(soup.prettify())
# req = soup.tbody.a.text
# req1 = soup.tbody.a['href']

#---------------------------------

# req  = soup.find_all(class_='fancybox fancybox.iframe')
# print(len(req))
# # print(req,'\n')
# # for l in req:
# #     print(l.text)
# z=req[0].text
#
# aa=" ".join(z.split())
# print(aa)

#-----------------------------------
import codecs
# print(soup.find_all())
req = soup.find_all('tr')
# del req[0]
# for r in req:
#     all_td = r.find_all('td')
#     date = all_td[0].text
#     print(date)
###############################https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docDet.php?docid=11217
del req[0]
# # print(len(req))
# # print(req[0])
# print(req[1])
all_td = req[0].find_all('td')
# # print(all_td[0])
#
# date = all_td[0].text
# print(repr(date))
#
# title = all_td[1]
# idd = title.a['href'][17:]
# print(repr(title.a['href']))
# full_link = 'https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/'+title.a['href']
# print(full_link)
# print(repr(title.a['href'][17:]))
# print(repr(title))
# print(title.replace('\t','').replace('\n',' '))
#
# aa=" ".join(title.split())
# print(repr(aa))
#
# by=all_td[2].text
# attention = all_td[3].text
# print(by,attention)


# x= codecs.decode(title, 'raw_unicode_escape')
# print(x)


#x = codecs.decode(c, 'unicode_escape')

x={"as":"ds"}
y={"dgs" : "fas"}
print(type(x))
z=[]
# print(type(z))
z.append(x)
z.append(y)
print(z)
