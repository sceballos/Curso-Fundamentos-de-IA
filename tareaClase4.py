import numpy as np

def analizar_ventas():
    ventas = []
    for i in range(10):
        monto = float(input(f"Ingrese el monto de la venta {i+1}: "))
        ventas.append(monto)
        break
    
    ventas_np = np.array(ventas)

    # 2. Promedio
    promedio = np.mean(ventas_np)

    # 3. Ventas por encima del promedio
    superiores = ventas_np[ventas_np > promedio]

    # 4. Total recaudado
    total = np.sum(ventas_np)

    # 5. Mejor y peor venta
    mejor = np.max(ventas_np)
    peor = np.min(ventas_np)

    # Resultados
    print("\n--- Resultados ---")
    print(f"Ventas ingresadas: {ventas_np}")
    print(f"Promedio de ventas: {promedio:.2f}")
    print(f"Ventas por encima del promedio: {superiores if superiores.size > 0 else 'Ninguna'}")
    print(f"Total recaudado: {total:.2f}")
    print(f"Mejor venta: {mejor:.2f}")
    print(f"Peor venta: {peor:.2f}")

if __name__ == "__main__":
    analizar_ventas()
