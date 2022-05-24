
numpy 1.22.2
pandas 1.4.0
matplotlib 3.5.1
seaborn 0.11.2
openpyxl 3.0.9
Pillow 9.0.1

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image

# LAB 6

#inicjalizacja tablicy
a = np.arange(8) # od 0 do 7
print(a)

a = np.array([0, 1]) # macierz
print(a)

print(type(a))
print(a.dtype)

#inicjalizacja tablicy z konkertnym typem danych
a = np.arange(2, dtype ='int64')
print(a.dtype)

b = a.astype('float')
print(b)
print(b.dtype)

print(b.shape)

print(a.ndim)

m = np.array([np.arange(2), np.arange(2)])
print(m.shape)

print(type(m))

# macierz wypełniona zerami lub jedynkami
zera = np.zeros((5,5))
print(zera)
jedynki = np.ones((4,4))
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)

poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)

macierz = np.array([[1,2],[3,4]])
print(macierz)
# (start, stop, step)
liczby = np.arange(1,2,0.1)
print(liczby)

liczby_lin = np.linspace(1,2,5) # 5 liczb z przedziały od 1 do 2
print(liczby_lin)
z = np. indices((5, 3))
print(z)

#wielowymiarowa macierz
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

#  macierz diagonalna
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

mat_diag_k = np.diag([a for a in range(5)],-1)
print(mat_diag_k)

z = np.fromiter(range(5), dtype='int32')
print(z)

# Macierz jako napis
marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_4 = np.array(list(marcin), dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin,dtype='S1')
mar_7 = np.fromiter(marcin,dtype='U1')
print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)

# Dzialania na macierzach
mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print()
print(mat - mat_1)
print()
print(mat*mat_1)
print()
print(mat/mat_1)
print()

# Cięcie tablic
a = np.arange(10) # od 0 do 9
print(a)
s = slice(2,9,2)
print(a[s])
s = range(2,7,2)
print(a[s])

print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25) # do 24
mat = mat.reshape((5,5))
print(mat)
print()
print(mat[1:]) #od drugiego wiersza
print()
print(mat[:,1]) #druga kolumna jako wektor
print()
print(mat[:,-1:]) #ostatnia kolumna
print()
print(mat[2:6, 1:3]) # 2 i 3 kolumna dla 3,4,5 wierszy
print()
print(mat[:, range(2,6,2)]) # 3 i 5 kolumna
print('')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)


# Lab 8

# tworzenie serii
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek',
'Wiesiek', 'Eleonora']) # seria z indexami
print(s)

#tworzenie dataframe na podstawie słownika
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
daty = pd.date_range('20210324', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty,
columns=list('ABCD'))
print(df)

# Csv, odczyt i zapis
df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',') # znaki w sep, decimal zależą od tego co jest w pliku
print(df)
df.to_csv('plik.csv', index=False)

# xlsx odczyt i zapis
xlsx = pd.ExcelFile('dane.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df.to_excel('wyniki.xlsx', sheet_name='arkusz pierwszy')

s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(s['Wiesiek']) #pojedynczy element serii
print(s.Wiesiek) # wartości serii
print(df[0:1]) # pojedynczy elemenet ramki danych

print(df['Populacja']) #kolumna po etykiecie
print(df.iloc[[0],[0]]) #pobieranie pojedynczej wartości po indeksie wiersza i kolumny
print(df.loc[[0],["Kraj"]]) #pobieranie wartości po indeksie wiersza i etykiecie kolumny
print(df.at[0,"Kraj"])

print(df.sample()) #jeden losowy element
print(df.sample(2)) #n losowych elementów
print(df.sample(frac=0.5)) #ilość elementów procentowo, uwaga na zaokrąglenie
print(df.sample(n=10, replace=True)) # losowanie z powtórzeniami

# wystwietlanie okreslonej liczby elementów
print(df.head())
print(df.head(2))
print(df.tail(1))


s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(s[(s>9)]) #wyświetla dane większe od 9
print(s.where(s > 10)) # zwraca całego dataframe ale tam gdzie nie spelnia warunku pojawia sie NaN
print(s.where(s>10, 'za duże')) # za NaN zostanie podstawione 'za duze'
seria = s.copy()
seria.where(seria > 10, 'za duże', inplace=True) # modyfikowanie oryginalnego zbioru
print(seria)
print(s[~(s > 10)]) # dane które nie są większe od 10
print(s[(s < 13) & (s > 8)]) # łączenie warunków
print(df[df['Populacja']>1200000000]) #warunki dla pobierania DataFrame
print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj)) # isin-> wartosci boolowskie
#zmiana, usuwanie i dodawanie danych
s['Wiesiek'] = 15
print(s.Wiesiek)
s['Alan'] = 16
print(s)
df.loc[3] = 'dodane' # wartość ustawiona dla wszystkich kolumn
print(df)
df.loc[4] = ['Polska', 'Warszawa', 38675467] # dodawanie wiersza
print(df)
new_df = df.drop([3]) # usuwanie wartości
print(new_df)
df.drop([3], inplace=True) # zmiana oryginalnego pliku
print(df)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'] # dodawanie kolumny
print(df)
print(df.sort_values(by='Kraj')) # sortowanie danych (Pandas)
grouped = df.groupby(['Kontynent']) # grupowania
print(grouped.get_group('Europa'))
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']})) # funkcje agregujące zamiast agg można użyć też .sum() , .count()


# LAB 9

# Wykres liniowy
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum() # skumulowana suma
print(ts)
ts.plot()
plt.savefig("wykres.png") # zapis wykresu do pliku png
# pillow do jpg
plt.show()


dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia','Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Populacja': [23568956, 23579056, 35829035, 6235982],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}
        
df = pd.DataFrame(dane)
# Wykres słupkowy
grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
grupa.plot(kind='bar', ylabel='Populacja w mln', xlabel='Kontynent', rot=0, color='green', legend=True, title='Populacja dla kontynentow')
plt.show()

# Wykres kołowy
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.') # csv
print(df)
grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']}) # Grupuje dane i sumuje po wartosci
print(grupa)
grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.legend(loc='upper left')    # legenda w danym miejscu
plt.show()


# wykres z sredniom kroczącą
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts)
print(df)
df['Srednia kroczaca'] = df.rolling(window=50).mean()
print(df)
df.plot()
plt.legend(['Wartosci','Srednia kroczaca'])
plt.show()




xlsx = pd.ExcelFile('imiona.xlsx') # xlsx
df = pd.read_excel(xlsx, header=0)
print(df)

# zad 1


grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
grupa.plot(kind='line', ylabel='Liczba', xlabel='Rok', rot=0, color='green', legend=True, title='Liczba urodzonych dzieci w danym roku')
df = range(len(x))
plt.show()

# zad 2

grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
grupa.plot(kind='bar', ylabel='Liczba', xlabel='Plec', rot=0, color='green', legend=True, title='Liczba urodzonych dzieci w danym roku')
plt.show()

# zad 3

grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
grupa.plot(kind='pie',subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=True, title='Liczba urodzonych dzieci w danym roku')
plt.show()

# zad 4

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)
grupa = df.groupby('Zamowienia').agg({'Liczba': ['sum']})
grupa.plot(kind='bar', ylabel='Liczba', xlabel='Plec', rot=0, color='green', legend=True, title='Liczba urodzonych dzieci w danym roku')
plt.show()

# lAB 10 matplotlib

# wykres liniowy
plt.plot([1, 2, 3, 4])
plt.ylabel('jakies liczby')
plt.show()

# wykres liniowy z punktami
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-') # r->kolor, 0->symbol kola, - -> linia
plt.axis([0, 6, 0, 20]) # okresla osie (0,6)-> os x, (0,20)->os y
plt.show()

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # r-- -> czer. kreski, bs-> nieb. kwadraty, g^->ziel. daszki
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()

x = np.linspace(0, 2, 100)
plt.plot(x, x, label="liniowa")
plt.plot(x, x**2, label="kwadratowa")
plt.plot(x, x**3, label="sześcienna")
plt.xlabel('etykieta x')
plt.ylabel("etykieta y")
plt.title("Prosty wykres")
plt.legend() # pokazuje legende
plt.savefig('wykres matplot.png') # zapisuje wykres w pliku png
plt.show()
im1 = Image.open('wykres matplot.png') # otwiera plik png
im1 = im1.convert('RGB')
im1.save('nowy.jpg') # zapis do jpg


x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label="sin(x)")
plt.xlabel('x') # etykieta osi
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend()
plt.show()


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

print(f"""a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]},
d={data['d'][0]}""")
plt.scatter('a', 'b', c='c', s='d', data=data) # wykres kropkowy z różnymi kolorami
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()

# dwa wykresy na jednym zdjęciu
x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
plt.subplot(2, 1, 1,) # miejsce wykresy na zdjeciu
plt.plot(x1, y1, '-')
plt.title('wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
ax = plt.subplot(2, 1, 2) # miejsce wykresy na zdjeciu
plt.plot(x2, y2, 'r-')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('wykres cos(x)')
plt.subplots_adjust(hspace=0.5)
plt.show()

# 3 wykresy na jednym zdjeciu
x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
fig, axs = plt.subplots(3, 2, )
# axs[] -> ustala miejsce na zdjeciu
axs[0, 0].plot(x1, y1, '-')
axs[0, 0].set_title('wykres sin(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')
axs[1, 1].plot(x2, y2, 'r-')
axs[1, 1].set_title('wykres cos(x)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('cos(x)')
axs[2, 0].plot(x2, y2, 'r-')
axs[2, 0].set_title('wykres cos(x)')
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('cos(x)')
# usuwa miejsca na wykres
fig.delaxes(axs[0, 1])
fig.delaxes(axs[1, 0])
fig.delaxes(axs[2, 1])
plt.show()

# wykres slupkowy
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)
plt.bar(data=df, x='Kontynent', height='Populacja',
color=['red', 'green', 'yellow'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja w mld')
plt.show()

x = np.random.randn(10000)
plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid()
plt.show()

# Wykres kolowy
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")# csv
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum() # grupowanie po imie i suma wartosci
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"), colors=['red', 'green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right') # miejsce legendy
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()



# zad 1

x = np.arange(1, 20, 1)
plt.plot(x, 1/x)
plt.xlabel('x')
plt.ylabel("f(x)")
plt.legend(labels=['f(x) = 1/x'])
plt.axis([1, 20, 0, 1])
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
plt.show()

# zad 2

x = np.arange(1, 20, 1)
plt.plot(x, 1/x, 'g:^' )
plt.xlabel('x')
plt.ylabel("f(x)")
plt.title('Wykres funkcji f(x) dla [1,20]')
plt.legend(labels=['f(x) = 1/x'])
plt.axis([1, 20, 0, 1])
plt.xticks([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20])
plt.show()

# zad 3

x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, x, c)
plt.title("Funkcja sin(x) i cos(x)")
plt.legend(labels=['Sin(x)', 'Cos(x)'],loc='upper right')
plt.xlabel('x')
plt.ylabel("y")
plt.show()

# zad 4

df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
x = df['sepal length']
y = df['sepal width']
c = np.random.randint(1,50,150)
s = np.abs(x - y)
plt.scatter(x, y, c=c, s=s)
plt.show()

# zad 5

xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
df = pd.read_excel(xlsx, header=0)
print(df)
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec')
etykiety = list(grouped.groups.keys())
wartosci = list(grouped.agg('Liczba').sum())
plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzonych dzieci')
# wykres 2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.xlabel('Rok')

# wykres 3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
y = df.groupby('Rok').agg('Liczba').sum()
plt.bar(x, y)
plt.xlabel('Rok')
# wyświetlamy cały wykres
plt.subplots_adjust(wspace=0.85)
plt.show()


plt.show()



# zad 6

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
a = df['Sprzedawca'].value_counts(ascending=False)
print(a)
wedges, texts, autotext = plt.pie(x=a, labels=a.index, autopct=lambda pct:"{:.1f}%".format(pct), textprops=dict(color="black"), colors=['red', 'green', 'blue', 'yellow','purple',])
plt.title('Suma zamowien sprzedawcow')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik ilosci zamowien')
plt.show()

# lAB 11 Seaborn

# Seaborn zacznyna się od sns.set()
# Wykres liniowy
sns.set(rc={'figure.figsize':(8, 8)}) # wielkosc wykresu
sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
             label='linia nr1', color='red', marker='o', linestyle=':')  # marker-> okrąg co część wykresu
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
#              label='linia nr2', color='green', marker='^', linestyle=':')
plt.xlabel('oś x') # opis osi
plt.ylabel('oś y')
plt.title('Wykres liniowy')
plt.show()

# liniowy z wykorzystaniem serii danych
s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres = sns.relplot(kind='line', data=s, label='linia') # relplot =/ lineplot
wykres.fig.set_size_inches(8,6)
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartosci')
wykres.add_legend() # dodaj legende
wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.6)
plt.show()

# Wykres liniowy z wykorzystaniem ramki danych
sns.set()
df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.') # Wczytanie pliku csv
print(df)
wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['red', 'purple', 'blue'])
wykres.set_xlabel('indeksy')
wykres.set_title('Wykres liniowy danych z iris datasets')
wykres.legend(title='Rodzaj kwiatu')
plt.show()


# wykres punktowy
sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0, 50, 10),
        'd':np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d'])*100
print(data['c'])
print(data['d'])
df = pd.DataFrame(data)
plot = sns.relplot(data=df, x='a', y='b',
                   hue='c', palette='bright', size='d', legend=True) # hue=color
plot.fig.set_size_inches(6,6)
plot.set(xticks=data['a']) # podzial os x
plt.show()

# wykres kolumnowy

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delni', 'Brasilia', 'Warszawa'],
        'Populacja': [3434134, 9812343, 32434241, 896346],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}
df = pd.DataFrame(dane)
sns.set()
plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent',
                   estimator=np.sum, dodge=False, palette=['red', 'green', 'yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres slupkowy')
plt.show()


