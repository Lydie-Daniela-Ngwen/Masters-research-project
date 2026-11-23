from bs4 import BeautifulSoup
import requests
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
rubriques=["politique","economie","sante","international","education","societe","defense","technologie-sciences","police-justice","social","sport","environnement","culture-idees"]

with open("inputs/liens_maxi_canard.txt", "w", encoding="utf8") as f:
    for rubrique in rubriques:
        page = requests.get(f"https://www.lecanardenchaine.fr/{rubrique}/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", class_="title-optimized__link")
        if links:
            for link in links:
                lien=link.get("href")
                lien_full="https://www.lecanardenchaine.fr"+lien
                #print(lien_full)
                f.write(lien_full+"\n")
        else:
            print(f"Aucun lien trouvé pour la rubrique {rubrique}")
            #print(len(lien))
            #for link in links:
                #lien = link.get("href")
                #f.writelines(lien)