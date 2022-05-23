import random

# zad 1

#     # a = {1-x, xE<1,10}
# a = [1-x for x in range(10)]
# print(a)
#     # b={1,4,16,...,4^7}
# b = [4**x for x in range(8)]
# print(b)
#     # c={x:xEB i x jest liczba podzielna przez 2}
# c = [x for x in b if x%2==0]
# print(c)

# zad 2

# lista1=[]
# for x in range(10):
#     lista1.append(random.randrange(0, 50))
# print(lista1)
# a = [x for x in lista1 if x%2==0]
# print(a)

# zad 3

# lista = {'chleb':'szt', 'maslo':'szt','ziemniaki':'kg','buraki':'kg'}

# # a = []
# # for value, key in lista.items():
# #     if key == 'szt':
# #         a.append(value)
# # print(a)


# a = [value for value, key in lista.items() if key == 'szt']
# print(a)

# zad 4

# def prostokatny(a=3, b=4, c=5):
#     if a**2 + b**2 == c**2:
#         return "trojkat prostokatny"
#     else:
#         return "to nie jest trojkat prostokatny"
# print(prostokatny())
# print(prostokatny(1,7,3))

# zad 5

# def pole_trapezu(a=2, b=4, h=3):
#     pole = (a+b)*h
#     return pole
# print(pole_trapezu())

# zad 6

# def iloczyn_ciagu(a=1, b=4, ile=10):
#     for x in range(ile):
#         a = a*b
#     return a
# print(iloczyn_ciagu())

# zad 7

# def iloczyn_ciagu(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma=1
#         for x in liczby:
#             suma = suma*x
#         return suma
# print(iloczyn_ciagu(1,6,2,4))

# zad8
# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow,2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))


# zad 9

print(arytmetyczny.n_ty_wyraz(6, 6, 2))
print(arytmetyczny.suma_ciagu(6, 16, 6))
print(geometryczny.n_ty_wyraz(1, 4, 11))