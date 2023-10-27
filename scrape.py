import requests
from bs4 import BeautifulSoup
import pprint


plist = []
res_list = []

def scrape_page(i):
    
    if i == 1:
        res = requests.get('https://news.ycombinator.com/news')
    else:
        res = requests.get(f'https://news.ycombinator.com/news?p={i}') 




#input num pages in terminal
page_num = input('How many pages? ')
#preconstruct urls
for i in range(int(page_num)):
    scrape_page(i + 1)
#     if i == 0:
#         plist.append('https://news.ycombinator.com/news')
#     else:
#         plist.append(f'https://news.ycombinator.com/news?p={i + 1 }')
#request urls
for item in plist:
    res_list.append(requests.get(item))

print(res_list[0].text)
#combine page data

#print page data

exit()
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext= soup.select('.subtext')

soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline > a')
subtext2= soup2.select('.subtext')

mega_links= links + links2
mega_sub= subtext + subtext2

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext): 
    hn= []
    for idx, item in enumerate(links):
        title= links[idx].getText()
        href= links[idx].get('href', None)
        vote= subtext[idx].select('.score')
        if len(vote): 
            points= int(vote[0].getText('', None).replace(' points', ''))
            if points > 99:  
                hn.append({'title':title, 'link':href, 'votes': points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_sub))