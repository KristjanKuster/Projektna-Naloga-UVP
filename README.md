 Projektna naloga: Analiza cen goriv

## Opis projekta

Ta projekt zajema pridobivanje, obdelavo in analizo podatkov o cenah goriv v Sloveniji zadnjih 20 let.  
Podatki so pridobljeni iz javno dostopne Excel datoteke na spletni strani Evropske komisije (Weekly Oil Bulletin).

V projektu so izvedene naslednje analize:
- Prikaz cen bencina 95, dizla, kurilnega olja in LPG plina skozi leta
- Izračun povprečnih cen po posameznih letih
- Primerjava razlik med ceno bencina in dizla skozi čas
- Izpis najvišjih in najnižjih cen goriv
- Grafične vizualizacije podatkov za lažjo interpretacijo

Vse analize so predstavljene v **Jupyter Notebooku**, kjer so tudi grafi in razlage.

---

## Navodila za zagon

### Zahteve
- Python 3.10 ali novejši
- Knjižnice:
  - pandas
  - matplotlib
  - requests
  - openpyxl (za branje Excel datotek)

### Namestitev knjižnic
```bash
pip install pandas matplotlib requests openpyxl
