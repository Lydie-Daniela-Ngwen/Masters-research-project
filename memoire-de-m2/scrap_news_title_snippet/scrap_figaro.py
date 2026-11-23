from requests_html import HTMLSession
session=HTMLSession()
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}

figaro_df=pd.DataFrame(columns=["title","snippet"])
heading=[]
sumary=[]
with open("inputs/liens_maxi_figaro.txt", "r", encoding="utf8") as f:
    for line in f:
        lien=line.strip()
        pages = requests.get(lien)
        soup = BeautifulSoup(pages.text, "html.parser")
        titre = soup.find('title')
        if titre:
            title=re.sub("<\/?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->"," ",str(titre))
        else:
            title=""
        bref=soup.select_one("p.fig-standfirst")
        if bref:
            snippet=re.sub("<\/?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->|\n","",str(bref))
        else:
            snippet=""
        figaro_df.loc[len(figaro_df)] = [title, snippet]
#print(figaro_df)
figaro_df.to_csv("outputs/figaro_df.csv")
print(len(figaro_df))
