import numpy as np
from scipy import stats
import pandas as pd

import os
from pandas import ExcelWriter
tablaN01_df = pd.read_excel('input_file/Tabla_05.xlsx', 'Hoja7')
df = pd.DataFrame(tablaN01_df) # df es nuestra variable a utilizar
a = type(tablaN01_df)
b = type(df)
print(df.head())
print("\n" )
print("La variable 'tablaN01_df' es de tipo: "+str(a))
print("La variable 'df' es de tipo: "+str(b))
if a == b:
    print("'tablaN01_df' y 'df' son el mismo tipo de dato.")
print("\n")
print("Las dimensiones de la tabla son: ")
print("Total de filas: "+str(len(df.index)))
print("Total de columnas: "+str(len(df.columns)))
print("\n")
print("El tipo de dato de la variable 'df' es: "+str(type(df)))
print("\n")
print("ESTADÍSTICA DESCRIPTIVA")
print("Media aritmetica:")
media_aritmetica_01 = df.mean()
print(media_aritmetica_01)
print("Media aritmética para cada columna:")
media_aritmetica_02 = df.mean(axis=1)
print(media_aritmetica_02)
#print("Media aritmética para cada fila:")
#media_aritmetica_02 = df.mean(axis=1)
#print(media_aritmetica_02)
#print("Mediana:")
#print("Mediana ")
#mediana_01 = np.median(df)
#print(mediana_01)
print("Mediana por cada columna:")
mediana_02 = np.median(df, 0)
print(mediana_02)
#print("Desviación:")
#desviacion_01 = np.std(df)
#print(desviacion_01)
print("Desviación típica de cada columna:")
desviacion_02 = np.std(df, 0)
print(desviacion_02)
#print("Varianza")
#varianza_01 = np.var(df)
#print(varianza_01)
print("Varianza de cada columna:")
varianza_02 = np.var(df, 0)
print(varianza_02)
print("Moda:")
moda_01 = stats.mode(df)
print(moda_01)
#print("Correlación:")
#correlacion_01 = np.corrcoef(df)
#print(correlacion_01)
#print("Co
#print("Covarianza:")
#covarianza_01 = np.cov(df)
#print(covarianza_01)

resumen = df.describe()
print("Resumen estadístico:")
print(resumen)

print("Sumando el valor de cada columna:")
suma = df.sum()
print(suma)

print("Acumulado de las sumas por columnas")
acumulado = df.cumsum()
print(acumulado)

#print("Media aritmetica:")
#media_aritmetica = df.
#pri
print("\n")
print("HISTOGRAMA DE DISTRIBUCIÓN")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8,4)})

mu, sigma = 0, 0.1 # media y desvío estándar
s = np.random.normal(mu, sigma, 100)

cuenta, cajas, ignorar = plt.hist(s, 30, density=True)
normal = plt.plot(cajas, 1/(sigma * np.sqrt(2*np.pi)) *
                  np.exp( - (cajas -mu)**2 / ( 2*sigma**2)),
                  linewidth=2, color='r')
plt.show()
