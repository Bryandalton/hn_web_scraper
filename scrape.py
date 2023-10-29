import requests
from bs4 import BeautifulSoup
import pprint


plist = []
res_list = []

def scrape_page(i):
    #preconstruct urls
    if i == 1:
        res = requests.get('https://news.ycombinator.com/news')
    else:
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    #grab relevant data
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    subtext= soup.select('.subtext')

    hn= []
    for idx, item in enumerate(links):
        title= links[idx].getText()
        href= links[idx].get('href', None)
        vote= subtext[idx].select('.score')
        if len(vote): 
            points= int(vote[0].getText('', None).replace(' points', ''))
            if points > 99:  
                hn.append({'title':title, 'link':href, 'votes': points})
    return hn




#input num pages in terminal
page_num = input('How many pages? ')

#print page data
for i in range(int(page_num)):
    pprint.pprint(scrape_page(i + 1))
