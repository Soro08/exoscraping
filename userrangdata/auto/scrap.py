import requests
from bs4 import BeautifulSoup
from userrangdata import models


def getuserperpage(pagenumb):
    req = requests.get("https://www.marketwatch.com/game/invest-until-you-die/rankings?partial=true&index={0}".format(pagenumb))

    soup = BeautifulSoup(req.text, 'html.parser')

    data = soup.find_all('tr', {'class': 'table__row'})

    print(len(data))

    for item in data:
        
        try:
            td = item.find_all('td')
            # rank
            user_rank = td[0].text 

            #name
            user_info = td[1].find('a')
            user_name = user_info.text
            user_link = user_info['href']
            
            # rank
            network = td[2].text 

            # rank
            last = td[3].text 

            # rank
            trades = td[4].text 

            # rank
            total_retuns = td[5].text 
            try:
                user = models.UserRank.objects.filter(rank=user_rank)[:1].get()
            except:
                user = models.UserRank(
                    rank= user_rank,
                    name = user_name,
                    user_url= user_link,
                    network = network,
                    
                    last = last,
                    trades = trades,
                    total_return = total_retuns
                    
                )
                
                user.save()

        except Exception as e:
            print(str(e))
        
def getuserinfo(user_url):
    req = requests.get(user_url)

    soup = BeautifulSoup(req.text, 'html.parser')

    data = soup.find('div', {'class': 'element element--profile'})
    
    listul = data.find('ul', {'class': 'list list--kv'})
    
    lis = listul.find_all('li', {'class': 'kv__item'})

    print(len(lis))
    
    # NET WORTH
    network = lis[0].find('span', {'class': 'primary'})
    print(network.text)
    # TODAY'S GAINS
    todaysgains = lis[1].find('span', {'class': 'primary'})
    print(todaysgains.text)
    #OVERALL GAINS
    overlaagains = lis[2].find('span', {'class': 'primary'})
    print(overlaagains.text)
    #OVERALL RETURNS
    averallreturns = lis[3].find('span', {'class': 'primary'})
    print(averallreturns.text)
    #CASH REMAINING ?

    cashremaining = lis[4].find('span', {'class': 'primary'})
    print(cashremaining.text)
    #BUYING POWER ?

    buyingpower = lis[5].find('span', {'class': 'primary'})
    print(buyingpower.text)
    #SHORT RESERVE ?

    shortreserve = lis[6].find('span', {'class': 'primary'})
    print(shortreserve.text)
    #CASH BORROWED ?
    cashborrowed = lis[7].find('span', {'class': 'primary'})
    print(cashborrowed.text)
    
    

# getuserinfo('https://www.marketwatch.com/game/invest-until-you-die/portfolio?p=1352012&name=chris%20reese')

def getinfo():
    while i <=17345:
        getuserperpage(i)
        i += 10