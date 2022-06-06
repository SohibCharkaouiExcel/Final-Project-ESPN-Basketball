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
    

answer = str(input("Which team are you rooting for?"))
proceed = "Golden State Warriors" or "golden state warriors"
proceed1 = "Memphis Grizzlies" or "memphis grizzlies"
proceed2 = "Denver Nuggets" or "denver nuggets"
proceed3 = "New Orleans Pelicans" or "new orleans pelicans"
proceed4 = "Minnesota Timberwolves" or "minnesota timberwolves"
proceed5 = "Brooklyn Nets" or "brooklyn nets"
proceed6 = "Boston Celtics" or "boston celtics"
proceed7 = "Phoenix Suns" or "phoenix suns"
proceed8 = "Dallas Mavericks" or "dallas mavericks"
proceed9 = "Philadelphia 76ers" or "philadelphia 76ers"
proceed10 = "Miami Heat" or "miami heat"
proceed11 = "Toronto Raptors" or "toronto raptors"
proceed12 = "Milwaukee Bucks" or "milwaukee bucks"
proceed13 = "Utah Jazz" or "utah jazz"
proceed14 = "Atlanta Hawks" or "atlanta hawks"
proceed15 = "Chicago Bulls" or "chicago bulls"



if answer == proceed:
 print("your team has 114 points")
elif answer == proceed1:
    print("your team has 112 points")
elif answer == proceed2:
    print("your team has 110 points")
elif answer == proceed3:
    print("your team has 109 points")
elif answer == proceed4:
    print("your team has 109 points")
elif answer == proceed5:
    print("your team has 109 points")
elif answer == proceed6:
    print("your team has 107 points")
elif answer == proceed7:
    print("your team has 107 points")
elif answer == proceed8:
    print("your team has 106 points")
elif answer == proceed9:
    print("your team has 104 points")
elif answer == proceed10:
    print("your team has 104 points")
elif answer == proceed11:
    print("your team has 103 points")
elif answer == proceed12:
    print("your team has 102 points")
elif answer == proceed13:
    print("your team has 99 points")
elif answer == proceed14:
    print("your team has 97 points")
elif answer == proceed15:
    print("your team has 95 points")
else:
 print("thats not a basketball team goofy fella")


    
    








