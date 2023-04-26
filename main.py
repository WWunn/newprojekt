import numpy as np
import pandas as pd
import openpyxl
# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
df = pd.read_excel(xlsx, header=0)
# Zadanie 2

# •tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# print(df[df['Liczba']>1000])
# •tylko rekordy gdzie nadane imię jest takie jak Twoje
# print(df[df['Imie'] == 'WOJTEK'])
# •sumę wszystkich urodzonych dzieci w całym danym okresie,
# print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
# •sumędzieci urodzonych w latach 2000-2005
# print(df.groupby(['Rok']).agg({'Liczba':['sum']}),df[df['Rok']<2005])
# •sumę urodzonych chłopców i dziewczynek,
print(df.groupby(['Plec']).agg({'Liczba':['max']}))
# •najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(df.groupby(['Rok']).agg({'Imie'})
# •najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# •listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# •5 najwyższych wartości zamówień•ilość zamówień złożonych przez każdego sprzedawcę•sumę zamówień dla każdego kraju
# •sumę zamówień dla roku 2005, dla sprzedawców z Polski
# •średnią kwotę zamówienia w 2004 roku,
# •zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv


