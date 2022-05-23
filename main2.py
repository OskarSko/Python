import math
# print(math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6))
#
# liczba_szesnastkowa = 0x1f
# print('{0:x}'.format(liczba_szesnastkowa))


# a = 7
# b = 9

# if a > b:
#     print("Liczba a jest wieksza od liczby b")
# elif a < b:
#     print("Liczba a jest mniejsza od liczby b")
# else:
#     print("Liczby a i b sa rowne")


# if a == b:
#     print("Liczby sa rowne")
# else:
#     print("Liczby nie sa rowne")


# a = input('Podaj liczbe: ')
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))
# print(a)


# a = input("Podaj pierwsza liczbe: ")
# b = input("Podaj druga liczbe: ")
# c = input("Podaj trzecia liczbe: ")
# d = input("Podaj czwarta liczbe: ")
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if(a > b) & (c > d):
#     print('a jest wieksze od b i c jest wieksze od d')
# else:
#     print('a jest mniejsze od b lub c jest mniejsze od d')


# for a in range(0, 7, 1):
#     print(a)

# Lista = ['cos', 4, 6, 6.7]
# for a in Lista:
#     print(a)
# else:
#     print('Wyswietlono wszytskie elementy z listy')


# licznik = 0
# while licznik != 11:
#     print(licznik)
#     licznik += 1


# lista = [4, 6, 8, 3, 5, 9, 2]
# licznik = 0
# liczba = input('Wpisz liczbe calkowita: ')
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('Liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
#         break
#     else:
#         licznik += 1
# else:
#     print('Zadna z wartosci nie dala odpowiedniego wyniku')


# lista1 = [4, 5, 7, 3, 7, 4, 5, 8]
# lista2 = [3, 6, 8, 4]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)


# a = input('Podaj pierwsza liczbe: ')
# b = input('Podaj druga liczba: ')
# try:
#     a=int(a)
#     b=int(b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print('nie mozna dzielic przez 0')
# except ValueError:
#     print('nie wczytana liczba calkowita')





# append insert extend del sort reverse pop remove

lista1 = [5, 6, 5, 7, 4, 3]
lista2 = ['o', 'a', 'c']
lista1.sort()
print(lista1)
lista1.insert(7, 6)
print(lista1)
lista1.append(lista2)
print(lista1)
lista2.pop(2)
print(lista1)
lista1.extend([9,2,3])
print(lista1)
lista1.remove(5)
print(lista1)
# zad 1

# lista = ['siatkowka', 'koszykowka', 'pilka nozna', 'ping-pong']
# lista.reverse()
# print(lista)
# lista.append('rugby')
# lista.append('tenis')
# print(lista)

# zad 2

# slownik = {'itd':'i tak dalej', 'itp':'i temu podobne', 'ww':'wyzej wymieniony', 'tj':'to jest'}
# print(slownik.keys())
# print(slownik.values())

# zad 3

# gry = {'League of legends':'Riot games', 'Final fantasy VII':'SQUARE ENIX', 'Scarlet Nexus':'Bandai Namco', 'Elden ring':'From Software'}
# a = 0
# b = 0
# for a in gry:
#     b+=1
# print(b)

# zad 4

# ile = 0
# napis = input('Wpisz dowolne zdanie: ')
# print(napis)
# for x in napis:
#     if x == 'a':
#         ile+=1
# print(ile)

# zad 5

# a = input("podaj pierwsza liczbe")
# b = input("podaj druga liczbe")
# c = input("podaj trzecia liczbe")
# a = int(a)
# b = int(b)
# c = int(c)
# print(a**b+c)

# zad 6

# a = input("podaj pierwsza liczbe")
# b = input("podaj druga liczbe")
# c = input("podaj trzecia liczbe")
# a = int(a)
# b = int(b)
# c = int(c)
# if a>b:
#     if a>c:
#         print("Liczba a jest najewieksza")
#     else:
#         print("Liczba c jest najwieksza")
# else:
#     if b>c:
#         print("Liczba b jest najwieksza")
#     else:
#         print("Liczba c jest najwieksza")

# zad 7

# pod = 0
# lista = [4, 6, 7.8, 4.5, 3, 1.9, 2]
# for x in lista:
#     x*=x
#     print(x)

# zad 8

# lista = []
# ile = 0
# while ile != 10:
#     ile += 1
#     a = input('Podaj liczbe')
#     a =int(a)
#     if a%2 == 0:
#         lista.append(a)
#     else:
#         continue
# print(lista)

# zad 9

# a = input("Podaj liczbe: ")
# a = int(a)
# if a<0:
#     print('zla liczba')
# else:
#     a = math.sqrt(a)
#     print(a)