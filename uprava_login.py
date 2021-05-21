#prevedeni xlsx souboru do csv bez indexu a hlavicky
import pandas as pd
df = 'C:\\Users\\dhajek\\Desktop\\Skoda-materialy\\NewProject\\Nazev_souboru.xlsx'
df = pd.read_excel(df)
df.to_csv('C:\\Users\\dhajek\\Desktop\\Skoda-materialy\\NewProject\\pokus1.csv', index=False, header=False)

#otevreni souboru, prevedeni na list, odstraneny /n noveho radku z listu
seznam = open('C:\\Users\\dhajek\\Desktop\\Skoda-materialy\\NewProject\\pokus1.csv', encoding='utf-8')
seznam1 = list(seznam)
seznam2 = []
for e in seznam1:
    seznam2.append(e.strip())
#print(seznam2)

#pridani " ' " pred login a " ', " za login
string1 = "'"
string2 = "',"
my_new_seznam1 = [string1 + x + string2 for x in seznam2]
#print(my_new_seznam1)

#prevedeni seznamu do csv souboru, bez indexu a bez hlavicky
dfs = pd.DataFrame(my_new_seznam1)
dfs.to_csv('C:\\Users\\dhajek\\Desktop\\Skoda-materialy\\NewProject\\vysledek.csv', index=False, header=False)
