import pandas as pd
import numpy as np
# 1. Leer el archivo CSV
df = pd.read_csv("Emisiones_CO2.csv",     sep="|",
    encoding="latin-1",   # si falla, prueba encoding="cp1252"
    engine="python")

# 2. Ver estructura inicial
print("Primeras filas del dataset:")
print(df.head())

print("\nValores faltantes por columna:")
print(df.isnull().sum())

# 3. Eliminar filas con valores nulos en las columnas principales
df = df.dropna(subset=["CO2 (kt)"])
df = df.dropna(subset=["CO2 per cápita (toneladas métricas)"])

def convertir_numero(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip()
    x = x.replace(".", "")   # elimina separador de miles
    x = x.replace(",", ".")  # cambia coma decimal a punto
    try:
        return float(x)
    except:
        return np.nan

# 4. Convertir tipos de datos
df["CO2 (kt)"] = df["CO2 (kt)"].apply(convertir_numero)
df["CO2 per cápita (toneladas métricas)"] = df["CO2 per cápita (toneladas métricas)"].apply(convertir_numero)

# 5. Verificar resultado
print("\nTipos de datos luego de la conversión:")
print(df.dtypes)

# 6. Guardar versión limpia
df.to_csv("Emisiones_CO_limpio.csv", index=False)
print("\nArchivo limpio guardado como 'Emisiones_CO_limpio.csv'")