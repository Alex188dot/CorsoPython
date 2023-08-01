import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar) #indica anche il tipo di dati

print(myvar[0])# accede all'elemento con etichetta zero perchè non specificata

print("--------------------------------------------------")

b = [1, 7, 2]

myvar = pd.Series(b, index = ["x", "y", "z"])

print(f"Printing the second value, with index 'y': {myvar['y']}")

print("--------------------------------------------------")

'''In questo caso creiamo un dizionario:
da notare, la chiave sostituisce l'indice'''
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print("--------------------------------------------------")

'''
In questo esempio, creiamo prima un dizionario con coppia chiave/valore
successivamente creiamo una serie composta solo da day1 e day2

'''
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
