import pandas as pd
import numpy as np

# =============================================================================
# 1. CARGA DE DATOS
# =============================================================================
archivo = "productos99.csv"
df_productos = pd.read_csv(r"C:\Users\srceb\Curso-Fundamentos-de-IA-2\productos99.csv", sep=",")

print("="*80)
print(f"🔍 ANÁLISIS EXPLORATORIO DE DATOS - {archivo}")
print("="*80)

# =============================================================================
# 2. TIPO Y FORMATOS DE DATOS
# =============================================================================
print("\n📘 TIPOS Y FORMATOS DE DATOS:")
print(df_productos.dtypes)

# =============================================================================
# 3. VALORES NULOS Y DUPLICADOS
# =============================================================================
print("\n🚫 VALORES NULOS:")
print(df_productos.isnull().sum())

print("\n📋 CANTIDAD DE FILAS DUPLICADAS:")
print(df_productos.duplicated().sum())

# =============================================================================
# 4. VALORES ATÍPICOS
# (Método del rango intercuartílico - IQR)
# =============================================================================
print("\n⚠️ VALORES ATÍPICOS (IQR):")

columnas_numericas = df_productos.select_dtypes(include=[np.number]).columns

for col in columnas_numericas:
    q1 = df_productos[col].quantile(0.25)
    q3 = df_productos[col].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = df_productos[(df_productos[col] < limite_inferior) | (df_productos[col] > limite_superior)]

    print(f"\n➡ {col}:")
    print(f"   Q1 = {q1:.2f}, Q3 = {q3:.2f}, IQR = {iqr:.2f}")
    print(f"   Límite inferior: {limite_inferior:.2f}")
    print(f"   Límite superior: {limite_superior:.2f}")
    print(f"   Valores atípicos detectados: {len(outliers)}")

# =============================================================================
# 5. RANGOS
# =============================================================================
print("\n📏 RANGOS DE VARIABLES NUMÉRICAS:")

for col in columnas_numericas:
    minimo = df_productos[col].min()
    maximo = df_productos[col].max()
    print(f"{col}: Mínimo = {minimo}, Máximo = {maximo}, Rango = {maximo - minimo}")

# =============================================================================
# 6. MEDIAS, MEDIANAS Y MODAS
# =============================================================================
print("\n📈 MEDIAS, MEDIANAS Y MODAS:")

for col in columnas_numericas:
    media = df_productos[col].mean()
    mediana = df_productos[col].median()
    moda = df_productos[col].mode()[0] if not df_productos[col].mode().empty else None
    print(f"{col}: Media = {media:.2f}, Mediana = {mediana:.2f}, Moda = {moda}")

# =============================================================================
# 7. DESVIACIÓN ESTÁNDAR
# =============================================================================
print("\n📊 DESVIACIÓN ESTÁNDAR:")

for col in columnas_numericas:
    desvio = df_productos[col].std()
    print(f"{col}: Desviación estándar = {desvio:.2f}")

# =============================================================================
# 8. RESUMEN FINAL
# =============================================================================
print("\n✅ ANÁLISIS COMPLETADO EXITOSAMENTE.")
print(f"Total de filas analizadas: {len(df_productos)}")
print(f"Total de columnas: {len(df_productos.columns)}")
