# EJEMPLOS DE ESTADÍSTICA DESCRIPTIVA CON PYTHON
import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd #importando pandas

np.random.seed(2134982) # para poder replicar el random
datos = np.random.randn(5, 4) # datos normalmente distribuidos
print("Datos normalmente distribuidos:")
print(datos)

# media aritmética
media_aritmetica_01 = datos.mean() #Se calcula invocando al atributo por mean de python
print("Media aritmética desde el atributo 'mean()':")
print(media_aritmetica_01)

media_aritmetica_02 = np.mean(datos) # mismo resultado desde la función numpy
print("Media aritmética con Numpy:")
print(media_aritmetica_02)

media_aritmetica_03 = datos.mean(axis=1) # media aritmetica desde ca
da fila
print("Media aritmetica desde cada fila:")
print(media_aritmetica_03)

# mediana
mediana = np.median(datos)
print("mediana:")
print(mediana)

mediana_01 = np.median(datos, 0) # media aritmetica de cada columna
print("Mediana por columna:")
print(mediana_01)

# desviación típica
desviacion_01 = np.std(datos)
print("Desviación:")
print(desviacion_01)

desviacion_02 = np.std(datos, 0) # desviación típica de cada columna
print("Desviación típica de cada columna:")
print(desviacion_02)

# varianza
varianza_01 = np.var(datos)
print("Varianza:")
print(varianza_01)

varianza_02 = np.var(datos, 0) #varianza de cada columna
print("Varianza de cada columna:")
print(varianza_02)

# moda
moda_01 = stats.mode(datos) # calcula la moda de cada columna
# el segundo array devuelve la frecuencua
print("Moda:")
print(moda_01)

datos2 = np.array([1, 2, 3, 6, 6, 1, 2, 4, 2, 2, 6, 6, 8, 10, 6])
moda_02 = stats.mode(datos2) # aqui la moda es el 6 porque aparece 5 veces en el vector.
print("Moda para un vector")
print(moda_02)

# correlación
correlacion_01 = np.corrcoef(datos) # crea matriz de correlación
print("Correlación:")
print(correlacion_01)

# Calculando la correlación entre dos vectores
correlacion_02 = np.corrcoef(datos[0], datos[1])
print("Correlación entre dos vectores:")
print(correlacion_02)

# covarianza
covarianza_01 = np.cov(datos)
print("Covarianza:")
print(covarianza_01)

# usando pandas
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'],
                         columns=['col1', 'col2', 'col3', 'col4'])
print(dataframe)

# resumen estadístico con pandas
resumen = dataframe.describe()
print("Resumen estadístico:")
print(resumen)

# sumando las columnas
suma = dataframe.sum()
print("Sumando las columnas:")
print(suma)

# sumando filas
dataframe.sum(axis=1)
print("Sumando filas:")
print(dataframe)

acumulado = dataframe.cumsum() #acumulados
print("Acumulado:")
print(acumulado)

# media aritmética de cada columna con pandas
media_aritmetica = dataframe.mean()
print("Media aritmetica:")
print(media_aritmetica)

# media aritmetica de cada fila con pandas
media_aritmetica_02 = dataframe.mean(axis=1)
print("media aritmetica de cada columna:")
print(media_aritmetica_02)

# HISTOGRAMAS Y DISTRIBUCIÓN

# Distribución normal
# graficos embebidos
#%matplotlib inline
import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn

# parametros estéticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8,4)})

mu, sigma = 0, 0.1 # media y desvío estandar
s = np.random.normal(mu, sigma, 10000) # creando muestra de datos

# histograma de distribución normal
#cuenta, cajas, ignorar = plt.hist(s, 30, normed=1)
cuenta, cajas, ignorar = plt.hist(s, 30, density=1)
normal = plt.plot(cajas, 1/(sigma * np.sqrt(2 * np.pi)) *
                  np.exp( - (cajas - mu)**2 / (2 * sigma**2)),
                  linewidth=2, color='r')
plt.show()

