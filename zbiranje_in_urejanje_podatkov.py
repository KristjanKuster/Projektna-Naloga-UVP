import requests
import pandas as pd
from io import BytesIO

url = "https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx" # link excel tabele s podatki

link = requests.get(url)
link.raise_for_status()

cene = pd.read_excel(BytesIO(link.content), 
                   skiprows=2, #izpustimo prve 3 vrstice saj nam ne pridejo v poštev
                   usecols=[0, 204, 205, 206, 209], # v teh vrsticah so podatki ki jih bom obravnaval
                   names=["Datum", "Cena_95", "Cena_Dizel", "Cena_Kurilno_Olje", "Cena_LPG_Plin"])  # nastavimo imena stolpcev

cene = cene.iloc[:1025] # izbrišemo zadnjih par vrstic saj nimajo podatkov ampak samo znake

cene["Cena_95"] = cene["Cena_95"] / 1000                        #vse podatke s cenam delimo s 1000, da dobimo enoto evro/liter
cene["Cena_Dizel"] = cene["Cena_Dizel"] / 1000 
cene["Cena_Kurilno_Olje"] = cene["Cena_Kurilno_Olje"] / 1000 
cene["Cena_LPG_Plin"] = cene["Cena_LPG_Plin"] / 1000 

cene["Datum"] = pd.to_datetime(cene["Datum"]).dt.strftime("%Y-%m-%d") # odstranimo uro iz datuma saj je za nas nepotrebna, kajtu podatki so po tednih

cene.to_csv("cene_slovenija.csv", index=False) #zapišemo podatke v datoteko cene_slovenija.csv, kjer sso podatki s katerimi bomo delali analizo

print(cene.head()) # izpiše prvih par vrstic da vidimo če je pravilno.