#import pymongo
import requests
from bs4 import BeautifulSoup


def startScrape():
    URL = "https://play.usaultimate.org/events/tournament/?ViewAll=true"
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, 'html5lib')

    games=[]

    upcomingGamesTable=(soup.findAll('table')[2])

    

    gamesList = upcomingGamesTable.findAll('tr')[1::]
    
    for gameHTML in gamesList:
        fields = gameHTML.findAll('td')
        games.append({"Name":fields[1].find('a').get_text().strip(), "City":fields[2].get_text().strip(), "State":fields[3].get_text().strip(), "Date":fields[5].get_text().strip()})

    for game in games:
        print(game)

    return games

if __name__ == "__main__":
    result = startScrape()
