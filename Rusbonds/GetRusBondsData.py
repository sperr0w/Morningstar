# -*- coding: utf-8 -*-


import requests
import json
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



loginLink = "http://www.rusbonds.ru/auth.asp"
commonDataLink = "http://www.rusbonds.ru/tyield.asp?tool=135547"
couponLink = "http://www.rusbonds.ru/emit_coup.asp?tool=135547"
loginData = {"login":"ipotskhveriia@gmail.com", "password":"iriska"}

loginCookies = {'rusbnd=UseR' : '860762244',
                'ASPSESSIONIDCADDQATS' : 'PPKDOEDDDCNLNOIDKKNJCFOO',
                'ASPSESSIONIDCADCRBTS' : 'KGGADODDBGEKEIIIAMDPHDAB',
                '_ym_uid' : '1526103215751810755',
                '_ym_isad' : '2',
                'ASPSESSIONIDCCDBSATS' : 'OPAHIHEDFEPIGPAHOHDDLGCH',
                'ASPSESSIONIDCACBQBTS' : 'KGMBDJEDFBKGNGECIAAGGCOK',
                'ASPSESSIONIDAABCSBSS' : 'HHHKOJEDJEEKIGOGFJDIGOCN',
                'ASPSESSIONIDACBBTASS' : 'FDBNPKEDKHGPKBIGFPBBENHL',
                'ASPSESSIONIDACDASATS' : 'NNGJHLEDLOPHPAANOIHNLKDA',
                '_gat' : '1',
                ' hotlog' : '1',
                '_ga' : 'GA1.2.1536452702.1526103215',
                '_gid' : 'GA1.2.238364642.1526103215',
                '_ym_visorc_24545993' : 'w'}

driver = webdriver.Chrome()
driver.get(loginLink)

u = driver.find_element_by_name('login')
u.send_keys('ipotskhveriia@gmail.com')
p = driver.find_element_by_name('password')
p.send_keys('iriska')
p.send_keys(Keys.RETURN)

loginSession = requests.Session()

response = requests.post(loginLink,data=loginData, cookies = loginCookies)

print(response)

result = []

commonDataPage = requests.get(commonDataLink)
commonDataPage.encoding = 'cp1251'


commonDataPageSoup = BeautifulSoup(commonDataPage.text , "lxml")

film_list = commonDataPageSoup.find('table', {'class': 'tbl_data'})
items = film_list.find_all('tr')
for item in items:
    if len(item.find_all('td')) == 2:
        property = item.find_all('td')
        propertyName = property[0].text
        propertyValue = property[1].text.split()[0]

        result.append({
            'propertyName': propertyName,
            'propertyValue': propertyValue
        })

for item in result:
    a=1
    #print('{propertyName:40}\t\t{propertyValue:6}'.format(**item))

couponPage = requests.get(couponLink)
couponPage.encoding = 'cp1251'

couponPageSoup = BeautifulSoup(couponPage.text , "lxml")

couponTable = couponPageSoup.find('table', {'class': 'tbl_data tbl_headgrid'})

print(couponPage.text)