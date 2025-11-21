import pandas as pd

def promedios(nombre_archivo, nombre_columna):
    df = pd.read_csv(nombre_archivo)
    
    if nombre_columna not in df.columns:
        return "No existe la columna"
    else:
        return df[nombre_columna].mean()