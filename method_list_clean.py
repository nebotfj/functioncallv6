import pandas as pd

def clean_methodids():
    # Leer el CSV
    print("Leyendo el archivo CSV...")
    df = pd.read_csv('function_analysis.csv')
    
    # Agrupar por method_id y combinar los protocolos
    print("Agrupando por method_id...")
    grouped = df.groupby('method_id').agg({
        'function': lambda x: ', '.join(sorted(set(x))),  # Combinar funciones únicas
        'protocol': lambda x: ', '.join(sorted(set(', '.join(x).split(', ')))),  # combinar protocolos únicos
        'direction': 'first',  # mantener la primera dirección
        'description': 'first',  # mantener la primera descripción
    }).reset_index()
    
    # Ordenar por función alfabéticamente
    print("Ordenando resultados...")
    grouped = grouped.sort_values('function', key=lambda x: x.str.lower())
    
    # Guardar el resultado
    print("Guardando resultados...")
    grouped.to_csv('function_analysis_cleaned.csv', index=False)
    
    print(f"\nProceso completado.")
    print(f"Registros originales: {len(df)}")
    print(f"Registros únicos por method_id: {len(grouped)}")
    print("Resultados guardados en 'function_analysis_cleaned.csv'")

    # Llamar a la función para encontrar duplicados
    find_duplicate_functions()

def find_duplicate_functions():
    print("\nBuscando method_ids con múltiples funciones...")
    # Leer el CSV limpio
    df = pd.read_csv('function_analysis_cleaned.csv')
    
    # Encontrar registros donde la columna 'function' contiene comas
    duplicates = df[df['function'].str.contains(',', na=False)]
    
    if not duplicates.empty:
        # Ordenar por method_id
        duplicates = duplicates.sort_values('method_id')
        
        # Guardar en nuevo archivo
        duplicates.to_csv('function_analysis_cleaned_dup.csv', index=False)
        
        print(f"Se encontraron {len(duplicates)} method_ids con múltiples nombres de función")
        
        # Mostrar resumen
        for _, row in duplicates.iterrows():
            print(f"\nMethod ID: {row['method_id']}")
            print(f"Funciones: {row['function']}")
    else:
        print("No se encontraron method_ids con múltiples nombres de función")

if __name__ == "__main__":
    clean_methodids()