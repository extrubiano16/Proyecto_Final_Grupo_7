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
  

def percentiles(nombre_archivo, nombre_columna):
    try:
        df = pd.read_csv(nombre_archivo)
    
        if nombre_columna not in df.columns:
            print('Error al procesar la columna')
            return
        
        p25 = df[nombre_columna].quantile(0.25)
        p50 = df[nombre_columna].quantile(0.50)
        p75 = df[nombre_columna].quantile(0.75)
        return p25, p50, p75

    except Exception as e:
        print('Error al procesar la columna: {e}')

