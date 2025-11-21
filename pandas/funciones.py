import pandas as pd

def promedios(nombre_archivo, nombre_columna):
    df = pd.read_csv(nombre_archivo)
    
    if nombre_columna not in df.columns:
        return "No existe la columna"
    else:
        return df[nombre_columna].mean()
def desviacion(nombre_archivo, columna):
    try:
        df = pd.read_csv(nombre_archivo)
        if columna not in df.columns:
            return "Error al procesar la columna"
        numeric_values = pd.to_numeric(df[columna], errors='coerce') 
        numeric_values = numeric_values.dropna()  
        return round(numeric_values.std(), 2)
    except Exception as e:
        return f"Error al procesar la columna: {e}"
  