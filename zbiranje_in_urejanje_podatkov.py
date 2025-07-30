import requests
import pandas as pd
from io import BytesIO

def prenesi_podatke(url):
    
    link = requests.get(url)   #Prenese Excel datoteko s podanim URL naslovom.
    link.raise_for_status()  # Preveri, če je prenos uspel, sicer sproži napako
    return link.content

def obdelaj_podatke(tabela):
    cene = pd.read_excel(BytesIO(tabela), # Prebere podatke iz Excel datoteke, preskoči prve 3 vrstice saj so nepomembne
                        skiprows=2, 
                        usecols=[0, 204, 205, 206, 209], # uporabi samo določene stolpce z cenami za Slovenijo in poimenuj stolpce
                        names=["Datum", "Cena_95", "Cena_Dizel", "Cena_Kurilno_Olje", "Cena_LPG_Plin"])
    
    cene = cene.iloc[:1025] # Odstrani spodnje vrstice, ki ne vsebujejo podatkov ampak tekst ali praznine

    for naslov in ["Cena_95", "Cena_Dizel", "Cena_Kurilno_Olje", "Cena_LPG_Plin"]: # Pretvori cene v evre na liter (deljenje s 1000)
        cene[naslov] = cene[naslov] / 1000
    
    cene["Datum"] = pd.to_datetime(cene["Datum"], errors='coerce').dt.strftime("%Y-%m-%d") # Pretvori stolpec Datum v obliko YYYY-MM-DD brez ure

    return cene

def shrani_csv(datoteka, ime_datoteke="cene_slovenija.csv"):
    
    datoteka.to_csv(ime_datoteke, index=False) #Shrani obdelane podatke v CSV datoteko brez indeksov.

if __name__ == "__main__":
    # URL Excel datoteke s podatki o cenah goriv
    url = "https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx"
    
    vsebina = prenesi_podatke(url) # Prenese podatke z interneta
    cene = obdelaj_podatke(vsebina) # Obdela prenesene podatke in pripravi podatke
    shrani_csv(cene) # Shrani obdelane podatke v CSV datoteko
    print(cene.head()) # Izpiši prvih 5 vrstic, da preverimo rezultate
