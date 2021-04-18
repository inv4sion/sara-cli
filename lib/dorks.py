import requests
from googlesearch import search
from bs4 import BeautifulSoup
from lxml import html

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }





def dorkfun(site):
    with open("archives/vazamentos.txt", "a") as file:
        sites = []
        for result in search(f"site: pastebin.com '{site}'", stop=5):
            sites.append(result)
            file.write(f"{result}\n")
            print(result)

        for result in search(f"intext:'t.me + {site}'", stop=5):
            sites.append(result)
            file.write(f"{result}\n")
            print(result)

        for result in search(f"inurl:'t.me + {site}'", stop=5):
            sites.append(result)
            file.write(f"{result}\n")
            print(result)
        return sites



def google(q):


    file = open("archives/vazamentos.txt", "a")
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'

    r = s.get(url, headers=headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    total = []

    for searchWrapper in soup.find_all('h3', {'class':'r'}):
        url = searchWrapper.find('a')["href"]
        text = searchWrapper.find('a').text.strip()
        total.append(url)
        print(url)
        file.write(f"{url}\n")

    file.close()

    return total






