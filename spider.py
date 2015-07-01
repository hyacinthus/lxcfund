__author__ = 'Muninn'

from urllib import request
from bs4 import BeautifulSoup

src = request.urlopen("http://fund.eastmoney.com/trade/gp.html#3n;desc")

soup = BeautifulSoup(src)

table = soup.find(id="tblite_gp")

print(table.tbody)
