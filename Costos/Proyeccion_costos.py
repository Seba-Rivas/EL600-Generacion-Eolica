'''
El presente script, tiene como objetivo proyuectar los costos marginales
a utlizar en el proyecto de generación Eólica supuesto en el curso EL6000.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# Lo primero es estraer los datos de los archivos .tsv y .csv:

# Partimos con los costos
url_PA = 'https://raw.githubusercontent.com/Seba-Rivas/EL600-Generacion-Eolica/main/Costos/Pan_de_Azucar_220kV.tsv'
df_PA = pd.read_csv(url_PA, sep = '\t',header=0)
drp = df_PA.index[df_PA['hora']==25].tolist() # Sacamos la hora 25
df_PA.drop(drp, axis=0, inplace = True)
drp2 = df_PA.indx[df_PA['']] 
df_dolar = df_PA.iloc[:,[4]] # Apartamos al columna de costos en dolares}

# Continuamos con el viento:
url_wind = 'https://raw.githubusercontent.com/Seba-Rivas/EL600-Generacion-Eolica/main/recon_B6RS7S.csv'
df_wind = pd.read_csv(url_wind, sep='[\s+,]' , engine='python', header = None)
drp = np.arange(8781) # Eliminaremos todo el año 1980, pues no está completo
drp  = drp.tolist()
df_wind.drop(drp, axis=0, inplace=True)
df_wind.index = range(len(df_wind))
# Para manipular los datos los pasaremos a numpy:

np_wind = df_wind.to_numpy()
for i in range(len(np_wind)):
    np_wind[i,0] = dt.datetime.strptime(np_wind[i,0], "%Y-%m-%d")

wind = []
for i in range(1,len(np_wind)):
    año = []
    if i == 0:
        año.append(np_wind[0,3])
    elif np_wind[i,0].year != np_wind[i-1,0].year:


# df_wind[0] = pd.to_datetime(df_wind[0])

# Ahora, lo que debemos hacer es generar columnas con los años y filas
#con las horas de cada día. No contemplaremos los días, pero luego debemo
#hallar la manera de reintroducir los días si los necesitamos

# df = pd.DataFrame(columns= ['year', 'hour', 'velocity'])
# w_vel = []
# w_date = []
# w_hour = []

# for j in range(len(df_wind)):
#     data = pd.DataFrame()

#     if df_wind[0][j] == df_wind[0][0]:
#         w_vel.append(df_wind[2][j])
#         w_date.append(df_wind[0][j])
#         w_hour.append(df_wind[1][j])

#     if df_wind[0][j].year != df_wind[0][j-1].year or j == len(df_wind)-1:
#         data['date'] = w_date
#         data['hour'] = w_hour
#         data['velocity'] = w_vel
#         data.head()
#         df.append(data,ignore_index=True)

#         w_vel = []
#         w_date = []
#         w_hour = []

#     else:
#         w_vel.append(df_wind[2][j])
#         w_date.append(df_wind[0][j])
#         w_hour.append(df_wind[1][j])
