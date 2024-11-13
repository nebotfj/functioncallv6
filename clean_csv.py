import csv

def remove_unknown_entries(file_path: str):
    # Leer el contenido del archivo CSV
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        lines = [line for line in reader if 'UNKNOWN' not in line]

    # Escribir el contenido filtrado de nuevo en el archivo CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

# Ruta al archivo CSV
csv_file_path = 'local_signatures.csv'

# Llamar a la función para eliminar las líneas "UNKNOWN"
remove_unknown_entries(csv_file_path)