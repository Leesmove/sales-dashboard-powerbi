import pandas as pd
import random
from datetime import datetime, timedelta

# Configuración
n_rows = 500
start_date = datetime(2024, 1, 1)
products = ['Producto A', 'Producto B', 'Producto C']
categories = ['Electrónica', 'Ropa', 'Alimentos']
regions = ['Bogotá', 'Medellín', 'Cali']

# Generar datos
data = {
    'Fecha': [(start_date + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(n_rows)],
    'Producto': [random.choice(products) for _ in range(n_rows)],
    'Categoría': [random.choice(categories) for _ in range(n_rows)],
    'Cantidad Vendida': [random.randint(1, 100) for _ in range(n_rows)],
    'Ingresos': [round(random.uniform(10000, 500000), 2) for _ in range(n_rows)],
    'Región': [random.choice(regions) for _ in range(n_rows)],
    'Cliente': [f'Cliente_{i}' for i in range(n_rows)]
}

# Crear DataFrame y guardar como CSV
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("Datos generados y guardados en sales_data.csv")