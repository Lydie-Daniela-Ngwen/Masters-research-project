from bs4 import BeautifulSoup
import requests
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
rubriques=["politique","societe","planete","economie","culture","international","sciences","sport","groenland"]

with open("inputs/liens_maxi_monde.txt", "w", encoding="utf8") as f:
    for rubrique in rubriques:
        page = requests.get(f"http://lemonde.fr/{rubrique}/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", class_="teaser__link")
        if links:
            for link in links:
                lien=link.get("href")
                f.write(lien+"\n")
        else:
            print("Aucun lien trouvé")
            #print(len(lien))
            #for link in links:
                #lien = link.get("href")
                #f.writelines(lien)