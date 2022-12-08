import csv
import requests
from bs4 import BeautifulSoup
taipei = []
URL= "https://www.319papago.idv.tw/lifeinfo/family/family-231.html"
list_req = requests.get(URL)    
if list_req.status_code == requests.codes.ok:
    soup = BeautifulSoup(list_req.content, 'html.parser')
    #textarea = soup.find_all('textarea')
    area = soup.find_all('td',{"height":"33"})
    #print(tags)
    for i in area:
        if i.string[0:3] == "新北市" :
            print(i.string)
            taipei.append(i.string)