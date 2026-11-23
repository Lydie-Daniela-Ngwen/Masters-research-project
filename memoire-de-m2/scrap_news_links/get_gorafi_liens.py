from bs4 import BeautifulSoup
import requests
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}

#c'est le fichier le plus récents que tu utilise pour ce travail, liens_complets_gorafi, celui qui scrap
#le plus de page, à combiner avec le premier que tu as créé manuellement
with open("inputs/liens_maxi_gorafi.txt", "w", encoding="utf8") as f:
    for i in range(20,90):
        page = requests.get(f"https://www.legorafi.fr/category/france/politique/page/{i}/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.title
        links = soup.find_all("a", rel="bookmark")
        for link in links:
            lien=link.get("href")
            f.write(lien+"\n")
            #print(len(lien))
            #for link in links:
                #lien = link.get("href")
                #f.writelines(lien)