'''
El presente script, tiene como objetivo proyuectar los costos marginales
a utlizar en el proyecto de generación Eólica supuesto en el curso EL6000.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lo primero es estraer los datos de los archivos .tsv:

url_PA = 'https://raw.githubusercontent.com/Seba-Rivas/EL600-Generacion-Eolica/main/Costos/Pan_de_Azucar_220kV.tsv'
df_PA = pd.read_csv(url_PA, sep = '\t',header=0)
drp = df_PA.index[df_PA['hora']==25].tolist() # Sacamos la hora 25
df_PA.drop(drp, axis=0, inplace = True) 
df_dolar = df_PA.iloc[:,[4]] # Apartamos al columna de costos en dolares

