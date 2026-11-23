from bs4 import BeautifulSoup
import requests
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
rubriques=["politique","societe","economie","culture","international","sport","groenland","iran","vox"]

with open("inputs/liens_maxi_figaro.txt", "w", encoding="utf8") as f:
    for rubrique in rubriques:
        page = requests.get(f"https://www.lefigaro.fr/{rubrique}", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", class_="fig-ranking-profile-link")
        if links:
            for link in links:
                lien=link.get("href")
                f.write(lien+"\n")
        else:
            print(f"Aucun lien trouvé pour la rubrique {rubrique}")
            #print(len(lien))
            #for link in links:
                #lien = link.get("href")
                #f.writelines(lien)