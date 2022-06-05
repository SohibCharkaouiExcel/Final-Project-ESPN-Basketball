import requests
from bs4 import BeautifulSoup

URL = "https://www.espn.com/nba/stats/_/view/team"
page = requests.get(URL)

#print(Tabindexpage.text)
    
soup = BeautifulSoup(page.content, "html.parser")

#css property: tabindex="0"
def has_tabindex(tag):
    return tag.has_attr('tabindex') and tag['tabindex'] == "0"

def has_dataclubid(tag):
    return tag.has_attr('data-clubhouse-uid')

results = soup.find_all(class_='Image Logo Logo__md')

for element in results:
    print(element['title'])
#print(results)

def has_classid(tag):
    return tag.has_attr('class="Table__TD')

results = soup.find_all(class_='td__Tableid')

User=("")
print("What team are you choosing?")

    
    

for element in results:
    teams=(element['title'])
    teams=['Golden State Warriors', 'Brooklyn Nets', 'Boston Celtics', 'Miami Heat','Milwaukee Bucks', 'Memphis Grizzlies', 'Minnesota Timberwovles', 'Philadelphia 76ers']
teams.remove('Golden State Warriors') 
teams.remove('Brooklyn Nets')
teams.remove('Boston Celtics')
teams.remove('Miami Heat')
teams.remove('Milwaukee Bucks') 
teams.remove('Memphis Grizzlies')
teams.remove('Minnesota Timberwovles')
teams.remove('Philadelphia 76ers')


    
    








