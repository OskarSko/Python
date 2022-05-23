# Wykres liniowy
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum() # skumulowana suma
print(ts)
ts.plot()
plt.savefig("wykres.png")
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