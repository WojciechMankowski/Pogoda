import csv
import pytest
from dataclasses import dataclass
import os
from pobranie_danych import *


@dataclass
class Typ:
    Data: str
    Hourser: str
    dane: str
    Tem: float
    Wilgodnosc: float
    Opady: float


fill = "Folder z plikami z csv//Dane.csv"
fille = os.path.normpath(fill)


def Writers():
    with open(fille, mode="a", newline="") as plik:
        header = [
            "Data",
            "Godzina pobrania",
            "Miasto",
            "Temperatura",
            "Wilgodność",
            "Opady",
        ]
        writer_csv = csv.DictWriter(plik, fieldnames=header)
        writer_csv.writeheader()
        i = 0
        for i in range(lenght):
            writer_csv.writerow(
                {
                    "Data": Data[i],
                    "Godzina pobrania": Hourser[i],
                    "Miasto": dane[i],
                    "Temperatura": Tem[i],
                    "Wilgodność": Wilgodnosc[i],
                    "Opady": Opady[i],
                }
            )



def Read():
    with open(fille, mode="r", newline="") as plik:
        read_csv = csv.reader(plik)
        for row in plik:
            print(row)


Writers()



