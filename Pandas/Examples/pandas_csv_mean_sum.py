import pandas as pd

df = pd.read_csv('prodotti_scelti.csv')

print(df)

media_colonna = df["totale"].mean()
somma_colonna = df["totale"].sum()


print("Somma della colonna 'nome_colonna':", somma_colonna)
print("Media della colonna 'nome_colonna':", media_colonna)