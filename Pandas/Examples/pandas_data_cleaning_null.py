import pandas as pd
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", 9)
df = pd.read_csv('prodotti_scelti.csv')
df["email"].fillna("email mancante", inplace=True)
df["username"].fillna("username mancante", inplace=True)
df["elettrodomestici"].fillna("elettrodomestico mancante", inplace=True)
df["confezionati"].fillna("confezionato mancante", inplace=True)
df["freschi"].fillna("fresco mancante", inplace=True)
df["frigo"].fillna("p. frigo mancante", inplace=True)

#df.fillna(0, inplace=True)
print(df)

'''
new_df = df.dropna()
print(new_df.to_string())'''
'''
df.dropna(inplace = True)
print(df.to_string())
'''

#df.fillna(130, inplace = True)

# This line below will save the new Dataframe on a new file
df.to_csv("new_prodotti_scelti.csv", index=False)