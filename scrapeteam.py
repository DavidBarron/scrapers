import requests
from bs4 import BeautifulSoup

url = "http://espn.go.com/nfl/team/roster/_/name/dal/dallas-cowboys"
r = requests.get(url)

soup = BeautifulSoup(r.content)
#links = soup.find_all("a")

#for link in links
#    print (link)

name = "NA"
team = "Dallas Cowboys"
number = "NA"
college = "NA"
exp = "NA"
height = "NA"
weight = "NA"
image = "NA"

data = soup.find_all("tr", {"class" : "oddrow player-28-5209"})
print(data)    
#print(type(player_data))

for item in data :
    #print (item.contents[0])
    for contents in item :
        print (contents)
    #soup2 = BeautifulSoup(item.contents[1])
