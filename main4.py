# import sys
# import random
# import math
# from math import *

# from pakiet import *
# napis = 'dzis jest piatek'
# litery.wyswietl(napis)
# print(litery.dlugosc(napis))
# print(dodawanie(5, 5))

# plik = open("tekst.txt", 'r')
# znaki = plik.read(10)
# linia = plik.readline()
# wiersze = plik.readlines()
#
# plik.close()
#
# print(znaki)
# print(linia)
# print(wiersze)
# print(len(wiersze))

# import sys
#
# print("podaj kierunek studiow, rok i specjalizacje")
# dane = sys.stdin.readline()
#
# plik = open('dane.txt','w+', encoding='utf-8')
# plik.write(dane)
# plik.close()
# lista = []
# for x in range(0, 7):
#     lista.append(x)
#
# plik = open('dane.txt', 'a+')
# plik.write(str(lista))
# plik.close()

# with open('tekst.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end=' ')

# class PierwszaKlasa:
#     """Pierwsza klasa python"""
#     atrybut = 54321
#     def pierwsza_metoda(self):
#         return 'Pierwsza metoda'
# obiekt = PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# obiekt.tekst = 'aaa'
# print(obiekt.tekst)
# # obiekt2 = PierwszaKlasa()
# # print(obiekt2.tekst)
# print(obiekt.pierwsza_metoda)


class ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = 'to bedzie klasa dla ogolnych ksztaltow'

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik


prostokat = ksztalty(10, 30)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis)
prostokat.dodaj_opis('Prostokat')
print(prostokat.opis)
prostokat.skalowanie(0, 5)
print(prostokat.x)
print(prostokat.y)

# zad 1

# liczba = random.randint(0, 30)
# liczba = liczba * 2
# plik = open('liczba.txt','w+')
# plik.write(str(liczba))
# plik.close()

# zad 2

# file = open('liczba.txt')
# num = file.readline()
# print(num)
# file.close()

# zad 3

# print("Podaj zdanie")
# dane = sys.stdin.readline()
# plik = open('tekst.txt','w+')
# plik.write(dane)
# plik.close()
# with open('tekst.txt','r') as plik:
#     for linia in plik:
#         print(linia)

# zad 4

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("%(zm1)s  %(zm2)s%(zm3)s kosztuje %(zm4)s zl" % {'zm1': self.nazwa_produktu, 'zm2': self.ilosc, 'zm3': self.jednostka_miary, 'zm4': self.cena_jed})
#
#     def ile_produktu(self):
#         print("%(zm1)s %(zm2)s" % {"zm1": self.ilosc, "zm2": self.jednostka_miary})
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# ziemniaki = NaZakupy(nazwa_produktu="ziemniaki", ilosc=5, jednostka_miary="kg", cena_jed=3)
# print(ziemniaki.wyswietl_produkt())
# print(ziemniaki.ile_produktu())
# print(ziemniaki.ile_kosztuje())

# zad 5

# class ciag_arytmetyczny:
#     def __init__(self, a1, r, n, ile):
#         self.a1 = a1
#         self.r = r
#         self.n = n
#         self.ile = ile
#
#     def wyswietl_dane(self):
#         print('a1 = %(z1)d' % {'z1': self.a1})
#         print('r = %(z2)d' % {'z2': self.r})
#         print('n = %(z3)d' % {'z3': self.n})
#         print('ile = %(z4)d' % {'z4': self.ile})
#
#     def pobierz_element(self):
#         self.ile = int(input("Podaj element"))
#
#     def pobierz_parametr(self):
#         self.a1 = int(input("Podaj pierwsza liczbe ciagu: "))
#         self.r = int(input("Podaj roznice w ciagu: "))
#         self.n = int(input("Podaj ilosc elementow ciagu: "))
#
#     def suma(self):
#         return ((2*self.a1+(self.n-1)*self.r)/2)*self.n
#
#     def policz_elementy(self):
#         an = self.a1
#         for x in range(self.ile):
#             k = an + self.r
#             an = k
#             print(k)
#
#
# funkcja = ciag_arytmetyczny(a1=1, r=3, n=2, ile=0)
# print(funkcja.suma())
# print(funkcja.pobierz_element())
# print(funkcja.pobierz_parametr())
# print(funkcja.suma())
# print(funkcja.policz_elementy())
# print(funkcja.wyswietl_dane())

# zad 6

# class robaczek:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
#
#     def idz_w_gore(self, krok):
#         self.y+=krok
#
#     def idz_w_dol(self, krok):
#         self.y-=krok
#
#     def idz_w_prawo(self, krok):
#         self.x+=krok
#
#     def idz_w_lewo(self, krok):
#         self.x-=krok
#
#     def pokaz_gdzie_jestes(self):
#         return (self.x,self.y)
#
# start = robaczek(x=0,y=0)
# print(start.pokaz_gdzie_jestes())
# print(start.idz_w_gore(5))
# print(start.pokaz_gdzie_jestes())
# print(start.idz_w_lewo(5))
# print(start.pokaz_gdzie_jestes())
# print(start.idz_w_prawo(3))
# print(start.pokaz_gdzie_jestes())
# print(start.idz_w_dol(9))
# print(start.pokaz_gdzie_jestes())