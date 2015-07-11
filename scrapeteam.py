import requests
import re
from bs4 import BeautifulSoup

urls = {
        "Arizona Cardinals" : "http://espn.go.com/nfl/team/roster/_/name/ari/arizona-cardinals",
        "Atlanta Falcons" : "http://espn.go.com/nfl/team/roster/_/name/atl/atlanta-falcons",
        "Baltimore Ravens" : "http://espn.go.com/nfl/team/roster/_/name/bal/baltimore-ravens",
        "Buffalo Bills" : "http://espn.go.com/nfl/team/roster/_/name/buf/buffalo-bills",
        "Carolina Panthers" : "http://espn.go.com/nfl/team/roster/_/name/car/carolina-panthers",
        "Chicago Bears" : "http://espn.go.com/nfl/team/roster/_/name/chi/chicago-bears",
        "Cincinnati Bengals" : "http://espn.go.com/nfl/team/roster/_/name/cin/cincinnati-bengals",
        "Cleveland Browns" : "http://espn.go.com/nfl/team/roster/_/name/cle/cleveland-browns",
        "Dallas Cowboys" : "http://espn.go.com/nfl/team/roster/_/name/dal/dallas-cowboys",
        "Denver Broncos" : "http://espn.go.com/nfl/team/roster/_/name/den/denver-broncos",
        "Detroit Lions" : "http://espn.go.com/nfl/team/roster/_/name/det/detroit-lions",
        "Green Bay Packers" : "http://espn.go.com/nfl/team/roster/_/name/gb/green-bay-packers",
        "Houston Texans" : "http://espn.go.com/nfl/team/roster/_/name/hou/houston-texans",
        "Indianapolis Colts" : "http://espn.go.com/nfl/team/roster/_/name/ind/indianapolis-colts",
        "Jacksonville Jaguars" : "http://espn.go.com/nfl/team/roster/_/name/jax/jacksonville-jaguars",
        "Kansas City Chiefs" : "http://espn.go.com/nfl/team/roster/_/name/kc/kansas-city-chiefs",
        "Miami Dolphins" : "http://espn.go.com/nfl/team/roster/_/name/mia/miami-dolphins",
        "Minnesota Vikings" : "http://espn.go.com/nfl/team/roster/_/name/min/minnesota-vikings",
        "New England Patriots" : "http://espn.go.com/nfl/team/roster/_/name/ne/new-england-patriots",
        "New Orleans Saints" : "http://espn.go.com/nfl/team/roster/_/name/no/new-orleans-saints",
        "New York Giants" : "http://espn.go.com/nfl/team/roster/_/name/nyg/new-york-giants",
        "New York Jets" : "http://espn.go.com/nfl/team/roster/_/name/nyj/new-york-jets",
        "Oakland Raiders" : "http://espn.go.com/nfl/team/roster/_/name/oak/oakland-raiders",
        "Philadelphia Eagles" : "http://espn.go.com/nfl/team/roster/_/name/phi/philadelphia-eagles",
        "Pittsburgh Steelers" : "http://espn.go.com/nfl/team/roster/_/name/pit/pittsburgh-steelers",
        "San Diego Chargers" : "http://espn.go.com/nfl/team/roster/_/name/sd/san-diego-chargers",
        "San Francisco 49ers" : "http://espn.go.com/nfl/team/roster/_/name/sf/san-francisco-49ers",
        "Seattle Seahawks" : "http://espn.go.com/nfl/team/roster/_/name/sea/seattle-seahawks",
        "St. Louis Rams" : "http://espn.go.com/nfl/team/roster/_/name/stl/st-louis-rams",
        "Tampa Bay Buccaneers" : "http://espn.go.com/nfl/team/roster/_/name/tb/tampa-bay-buccaneers",
        "Tennessee Titans" : "http://espn.go.com/nfl/team/roster/_/name/ten/tennessee-titans",
        "Washington Redskins" : "http://espn.go.com/nfl/team/roster/_/name/wsh/washington-redskins"
        }

for dteam,url in urls.items() :

    name = "NA"
    team = dteam
    number = "NA"
    college = "NA"
    exp = "NA"
    height = "NA"
    weight = "NA"
    image = "NA"
    
    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    data = soup.find_all("tr", class_=re.compile("player-28"))   # find all player info

    for player in data :
        print(dteam)
        for attribute in player :
            attribute = attribute.contents   # get data from tags
            if "<" in str(attribute) :   # we need to get player name and image
                bad_soup = BeautifulSoup(str(attribute))
                for thing in bad_soup.find_all("a") :
                    player_url = thing.get("href")
                    name = thing.contents[0]
                    print (name)
                    r2 = requests.get(player_url)
                    nasty_soup = BeautifulSoup(r2.content)
                    pdata = nasty_soup.find_all("div", {"class" : "main-headshot"})   # look for player photo
                    image_url = str(pdata).split("\"")
                    try :
                        print( image_url[5].split("&")[0])
                    except IndexError:
                        print ("http://capstone.cryotek.org/img/team/empty-compressed.png")
            else :   # data is already good to go
                print (attribute[0])