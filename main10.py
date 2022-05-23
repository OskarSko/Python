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
im1.save('nowy.jpg')


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

# dwa wykresy na jednum zdjęciu
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