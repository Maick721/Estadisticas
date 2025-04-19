import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

# Fijamos la semilla para que sea alazeatoria
np.random.seed(0) #El 0 es la semilla que se utiliza para generar números aleatorios, 

# Generamos 100 lenguajes y sectores aleatorios
lenguajes = np.random.choice(['Python', 'Java', 'C++', 'JavaScript', 'C#'], 100) 
sectores = np.random.choice(['Educación', 'Finanzas', 'Tecnología', 'Salud'], 100)

# Creamos un DataFrame con los datos generados
df = pd.DataFrame({'Lenguaje': lenguajes, 'Sector': sectores})

# Calculamos la moda del lenguaje mas utilizado en general y por sector
moda_general = df['Lenguaje'].mode()[0]  # Moda general el primer elemento de la serie 
moda_por_sector = df.groupby('Sector')['Lenguaje'].agg(lambda x: x.mode()[0])  # Moda por sector 
#el db.groupby agrupa los datos por sector y luego aplicamos la función lambda para obtener la moda de cada grupo

# Graficamos la distribución de lenguajes por sector
plt.figure(figsize=(11, 6))  # Tamaño de la figura
for i, sector in enumerate(df['Sector'].unique()):  # Iteramos sobre cada sector único donde el for es para recorrer los sectores
    plt.subplot(2, 2, i + 1)  # Creamos un subplot para cada sector y el i+1 es para que empiece desde 1 
    # Contamos los lenguajes en el sector actual
    conteo_lenguajes = df[df['Sector'] == sector]['Lenguaje'].value_counts()
    conteo_lenguajes.plot(kind='bar')  # Graficamos un gráfico de barras
    plt.title(f'Lenguajes en Sector: {sector}')  # Título del subplot
    plt.xlabel('Lenguaje')  # Etiqueta del eje x
    plt.ylabel('Frecuencia')  # Etiqueta del eje y
plt.tight_layout()  # Ajustamos el layout
plt.show()  # Mostramos los histogramas

# Creamos un diagrama de pastel para la distribución general de lenguajes
plt.figure(figsize=(8, 6))  # Tamaño de la figura
df['Lenguaje'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)  # Gráfico de pastel
plt.title('Distribución General de Lenguajes de Programación')  # Título del gráfico
plt.ylabel('')  # Sin etiqueta en el eje y
plt.show()  # Mostramos el diagrama de pastel

# Creamos una tabla de frecuencias cruzadas entre Lenguaje y Sector
tabla_frecuencias = pd.crosstab(df['Lenguaje'], df['Sector'])  # Tabla de frecuencias cruzadas 
#El crostab crea una tabla de contingencia

plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.imshow(tabla_frecuencias, cmap='Blues')  # Heatmap con anotaciones y formato de enteros  
plt.title('Lenguaje vs Sector')  # Título del heatmap
plt.xlabel('Sector')  # Etiqueta del eje x
plt.ylabel('Lenguaje')  # Etiqueta del eje y
plt.colorbar() # Barra de color para el heatmap
plt.show()  # Mostramos el heatmap

# Imprimimos los resultados
print(f'Moda general: {moda_general}')  # Moda general
print('Moda por sector:')  # Encabezado para la moda por sector
print(moda_por_sector)  # Mostramos la moda por sector porque no me vale
