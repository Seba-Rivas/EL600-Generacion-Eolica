'''
El presente script, tiene como objetivo proyuectar los costos marginales
a utlizar en el proyecto de generación Eólica supuesto en el curso EL6000.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lo primero es estraer los datos de los archivos .tsv:

df_PA = pd.read_csv(https://raw.githubusercontent.com/Seba-Rivas/EL600-Generacion-Eolica/main/Costos/Pan_de_Azucar_220kV.tsv, header=1)
