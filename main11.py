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