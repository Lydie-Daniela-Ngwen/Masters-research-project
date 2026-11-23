from requests_html import HTMLSession
session=HTMLSession()
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}

monde_df=pd.DataFrame(columns=["title","snippet"])

with open("inputs/liens_maxi_monde.txt","r",encoding="utf8") as f:
    for line in f:
        lien=line.strip()
        pages = requests.get(lien)
        soup = BeautifulSoup(pages.text, "html.parser")
        titre = soup.find('h1')
        if titre:
            title=re.sub("<\/?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->"," ",str(titre))
                #print(f'title : {title}')
        else:
            title=""
        bref=soup.select_one("span.ds-chapo")
        if bref:
            snippet=re.sub("<\/?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->","",str(bref))
        else:
            snippet=""
        monde_df.loc[len(monde_df)] = [title, snippet]
#print(len(monde_df))
monde_df.to_csv("outputs/monde_df.csv")
print(len(monde_df))
