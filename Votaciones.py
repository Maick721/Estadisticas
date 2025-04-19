import pandas as pd # Importamos pandas para manejar datos
import numpy as np # Importamos numpy para cálculos numéricos
import seaborn as sns  # Importamos seaborn para visualización de datos
import matplotlib.pyplot as plt # Importamos matplotlib para gráficos
from plotnine import * # Importamos plotnine para gráficos de ggplot2 

# Generar datos aleatorios 
np.random.seed(42) # Fijamos la semilla para  que sea aleatoria 
#El 42 es un número que se utiliza comúnmente como semilla en la programación
data = { 
    'Voto con conciencia': np.random.normal(0, 1, 100) * 10, # np.random.normal genera números aleatorios con una distribución normal
    'Voto sin conciencia': np.random.normal(0, 1, 100) * 10  # Multiplicamos por 10 para escalar los datos
}
df = pd.DataFrame(data) # Creamos un DataFrame con los datos generados

# Calcular varianza y desviación estándar
var_X = np.var(df['Voto con conciencia']) # np.var calcula la varianza de los datos
std_X = np.std(df['Voto con conciencia']) # np.std calcula la desviación estándar de los datos
var_Y = np.var(df['Voto sin conciencia']) # np.var calcula la varianza de los datos
std_Y = np.std(df['Voto sin conciencia']) # np.std calcula la desviación estándar de los datos
# df['Voto con conciencia'] = df['Voto con conciencia'].astype(int) # Convertimos a entero

# Calcular covarianza
covariance = np.cov(df['Voto con conciencia'], df['Voto sin conciencia'])[0][1] # np.cov calcula la covarianza entre dos variables 
#el 0 y el 1 son los índices de la matriz de covarianza 

print(f"Varianza de votos con conciencia: {var_X}") # Imprimimos la varianza de votos con conciencia var_X nos ayuda a ver la dispersión de los datos
print(f"Desviación estándar de las personas que votan con conciencia: {std_X}") # Imprimimos la desviación estándar de los votos con conciencia 
print(f"Varianza de votos sin conciencia: {var_Y}") # Imprimimos la varianza de votos sin conciencia var_Y nos ayuda a ver la dispersión de los datos
print(f"Desviación estándar de las personas que votan sin conciencia: {std_Y}") # Imprimimos la desviación estándar de los votos sin conciencia
print(f"Covarianza entre votos con conciencia y sin conciencia: {covariance}") # Imprimimos la covarianza entre los votos con y sin conciencia

# Gráfico de dispersión con línea de tendencia
grafica = (
    ggplot(df, aes(x='Voto con conciencia', y='Voto sin conciencia')) + # ggplot es una librería de visualización de datos
    geom_point() + # geom_point genera un gráfico de dispersión
    geom_smooth(method='lm', color='red') + # geom_smooth añade una línea de tendencia al gráfico el method='lm' indica que se usará un modelo lineal
    labs(title='Gráfico de Dispersión con Línea de Tendencia', x='Voto con conciencia', y='Voto sin conciencia') # labs añade etiquetas al gráfico
)

grafica.save(filename='scatter_plot.png') # Guardamos el gráfico como una imagen

# Heatmap de la matriz de correlación
correlation_matrix = df.corr() # df.corr calcula la matriz de correlación entre las variables del DataFrame
plt.figure(figsize=(10, 6)) # Tamaño de la figura
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True) # sns.heatmap genera un heatmap de la matriz de correlación 
#que nos sirve para ver la relación entre las variables 
plt.title('Heatmap de la Matriz de Correlación') 
plt.show()