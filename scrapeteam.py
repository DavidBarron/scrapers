import requests
from bs4 import BeautifulSoup


url = "http://www.dallascowboys.com/team/roster"
url2 = "http://www.philadelphiaeagles.com/team/roster.html"
r = requests.get(url2)
#print(type(r))
#print(type(r.content))
soup = BeautifulSoup(r.content)
#links = soup.find_all("a")

#for link in links
#    print (link)

name = "NA"
team = "Philadelphia Eagles"
number = "NA"
college = "NA"
exp = "NA"
height = "NA"
weight = "NA"
image = "NA"

number_data = soup.find_all("div", {"class" : "field field--name-field-jersey-number field--type-number-integer field--label-hidden"})

player_data = soup.find_all("div", {"class" : "field field--name-field-player field--type-entityreference field--label-hidden"})
#print(type(player_data))
for item in player_data :
    print (item.contents[1])
    soup2 = BeautifulSoup(item.contents[1])