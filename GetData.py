import requests
import json

link = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB"
link2 = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=12&dataType=A&order=asc&columnYear=10&number=3"
link3 = "http://quote.morningstar.com/ajax/exportKR2CSV.html?t=FB"
link4 = 'http://globalquote.morningstar.com/globalcomponent/RealtimeHistoricalStockData.ashx?ticker=\",x,\"&showVol=true&dtype=his&f=d&curry=USD&range=1900-1-1|2014-10-10&isD=true&isS=true&hasF=true&ProdCode=DIRECT'
link5 = "http://mschart.morningstar.com/chartweb/defaultChart?type=getcc&secids=0P000001BW;ST&dataid=8226&startdate=1900-01-01&enddate=2017-05-05&currency=&format=1&callback=jQuery164015960861115569203_1494006365716&_=1494006367815"
link6 = "http://quotes.morningstar.com/stockq/c-recommencation?&t=XNAS:MSFT&region=usa&culture=en-US&version=RET&cur="
link7 = "http://quotes.morningstar.com/stockq/c-recommencation?&t=XNAS:FB&region=usa&culture=en-US&version=RET&cur="
link8 = "http://quotes.morningstar.com/stock/analysis-report?t=XNAS:FB"

f = requests.get(link8)


for line in f.text.splitlines():
    print(line)