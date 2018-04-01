
# coding: utf-8

# # 파이썬 웹 크롤링
# # 출처 : https://blog.naver.com/htk1019/

# # 미국 주식 데이터
#  http://finviz.com/

# In[2]:

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
url = r'http://finviz.com/quote.ashx?t={}'.format("NVDA".lower())
req = Request(url)
html = urlopen(req).read()
soup = bs(html, 'lxml')


# In[3]:

d = soup.find(text="P/E")
d_ = d.find_next(class_='snapshot-td2').text
print(d_)


# In[4]:

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs

def getFinancialRatioUS(symbol, item):
    try:
        url = r'http://finviz.com/quote.ashx?t={}'.format(symbol.lower())
        req = Request(url)
        html = urlopen(req).read()
        soup = bs(html, 'lxml')
        pb = soup.find(text=item)
        pb_ = pb.find_next(class_='snapshot-td2').text
        return pb_
    except Exception as e:
        print(e)

psr = getFinancialRatioUS("NVDA","P/S")
print(psr)


# In[ ]:



