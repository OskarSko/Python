# tworzenie serii
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek',
'Wiesiek', 'Eleonora'])
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
df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')
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
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']})) # funkcje agregujące