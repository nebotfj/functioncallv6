from web3 import Web3
import requests
import csv
import os
from eth_abi import decode, encode
from eth_utils import encode_hex, keccak

def read_from_csv(method_id, filename='ethereum_functions.csv'):
    if not os.path.isfile(filename):
        return None
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['method_id'] == method_id:
                return row
    return None

def calculate_method_signature(method_id):
    """Calcula la firma usando eth_abi directamente"""
    try:
        # Eliminar el prefijo '0x' si existe
        method_id = method_id.replace('0x', '')
        
        # Crear un Web3 instance
        w3 = Web3()
        
        # Calcular el selector de función
        selector = bytes.fromhex(method_id)
        
        # Lista de nombres comunes de funciones
        common_functions = ['transfer', 'approve', 'mint', 'burn', 'swap', 'stake']
        
        # Lista de tipos comunes en Ethereum
        common_types = [
            ['address'],
            ['uint256'],
            ['bool'],
            ['bytes'],
            ['string'],
            ['address', 'uint256'],
            ['address', 'address'],
            ['uint256', 'uint256'],
            ['address', 'uint256', 'bytes'],
            ['address[]', 'uint256[]'],
        ]
        
        # Intentar diferentes combinaciones de nombres y tipos
        for func_name in common_functions:
            for types in common_types:
                try:
                    signature = f"{func_name}({','.join(types)})"
                    if w3.keccak(text=signature)[:4] == selector:
                        return signature
                except:
                    continue
                
        return None
    except Exception as e:
        print(f"Error calculando la firma: {e}")
        return None

def get_function_signature(method_id):
    method_id = method_id.replace('0x', '')
    
    # Primero intentar obtener la firma calculándola
    calculated_signature = calculate_method_signature(f"0x{method_id}")
    if calculated_signature:
        return {
            'method_id': f"0x{method_id}",
            'name': calculated_signature.split('(')[0],
            'signature': calculated_signature
        }
    
    # Si no se puede calcular, intentar con 4byte.directory
    url = f"https://www.4byte.directory/api/v1/signatures/?hex_signature=0x{method_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            signature = data['results'][0]['text_signature']
            return {
                'method_id': f"0x{method_id}",
                'name': signature.split('(')[0],
                'signature': signature
            }
    return None

def save_to_csv(data, filename='ethereum_functions.csv'):
    file_exists = os.path.isfile(filename)
    fieldnames = ['method_id', 'nombre_de_la_funcion', 'firma']
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'method_id': data['method_id'],
            'nombre_de_la_funcion': data['name'],
            'firma': data['signature']
        })

# Lista de method_ids para procesar
method_ids = [
    "0x8e1a55fc", "0xf39b5b9b", "0x095ea7b3", "0xddf7e1a7", "0xc2998238",
    "0xf3541901", "0xa0712d68", "0x1249c58b", "0xc5ebeaec", "0x852a12e3",
    "0xdb006a75", "0x4e07008d", "0x546cb17e", "0x4254b155", "0x0bde6eb7",
    "0x39039497", "0x6b1d4db7", "0xd2d0e066", "0x082fef45", "0xfbabdebd",
    "0xa9059cbb", "0x1cff79cd", "0x29589f61", "0x8f6ede1f", "0x40c10f19",
    "0x9dc29fac", "0x81a6b250", "0x5a3b74b9", "0x95e3c50b", "0x422f1043",
    "0x03152429", "0xf88bf15a", "0xf88309d7", "0xa67a6a45", "0xab832b43",
    "0x23440944", "0xc858f5f9", "0x3ccfd60b", "0x5ceae9c4", "0xfc6f4e16"
]

def process_method_ids(method_ids):
    for method_id in method_ids:
        print(f"\nProcesando {method_id}...")
        
        # Primero buscar en el CSV
        existing_data = read_from_csv(method_id)

        if existing_data:
            print(f"Información encontrada en el CSV:")
            print(f"Method ID: {existing_data['method_id']}")
            print(f"Nombre de la función: {existing_data['nombre_de_la_funcion']}")
            print(f"Firma completa: {existing_data['firma']}")
        else:
            # Si no está en el CSV, intentar obtener la firma
            result = get_function_signature(method_id)
            if result:
                save_to_csv(result)
                print(f"Nueva información guardada en el CSV:")
                print(f"Method ID: {result['method_id']}")
                print(f"Nombre de la función: {result['name']}")
                print(f"Firma completa: {result['signature']}")
            else:
                print(f"No se pudo encontrar la firma para el method_id {method_id}")

# Procesar todos los method_ids
process_method_ids(method_ids)




