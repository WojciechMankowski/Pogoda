from requests import get
from json import loads
from Listy import voivodeship, dane

Data = []
Hourser = []
Tem = []
Wilgodnosc = []
Opady = []
url = "https://danepubliczne.imgw.pl/api/data/synop"
responsy = get(url)
Pogoda_Data = loads(responsy.text)
i = 0
for row in Pogoda_Data:
    City = row["stacja"]
    data = row["data_pomiaru"]
    Data.append(data)
    hourser = row["godzina_pomiaru"]

    Hourser.append(hourser)

    tem = row["temperatura"]
    Tem.append(tem)

    wilgotnosc = row["wilgotnosc_wzgledna"]
    Wilgodnosc.append(wilgotnosc)

    opady = row["suma_opadu"]
    Opady.append(opady)
    for City in voivodeship:
        dane.append(City)
    i += 1
    if i == 18:
        break
    else:
        continue
lenght = len(voivodeship)
