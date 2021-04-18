import requests
import bs4
import re





def personal(url, user):
    html_content = requests.get(url).text
    match = re.findall(r'[\w\.-]+@[\w\.-]+', html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    result = soup(text=re.compile(self.word), limit=1)
    for c in match:

        if c == user:
            print(f"\033[32m{user}\033[m found in \033[31m{url}\033[m")
        else:
            print(f"\033[32mUser not found in {url}\033[m")




def domain():
    with open("archives/vazamentos.txt", "r") as fileRead:
        for url in fileRead:
            url = url.replace("\n", "")
            html_content = requests.get(url).text
            match = re.findall(r'[\w\.-]+@[\w\.-]+', html_content)
            with open("archives/contents/emails.txt", "a") as file:
                for c in match:
                    print(c)
                    file.write(f"{c}\n")



#personal("https://tecnoblog.net/352662/twitter-sofre-ataque-e-contas-famosas-publicam-fraude-com-bitcoins/", "bill")


