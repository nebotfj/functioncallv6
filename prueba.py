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
        print(f"Firma obtenida por cálculo directo")
        return {
            'method_id': f"0x{method_id}",
            'name': calculated_signature.split('(')[0],
            'signature': calculated_signature,
            'source': 'cálculo directo'
        }
    
    # Lista de APIs y bases de datos de firmas
    signature_apis = [
        {
            'name': '4byte.directory',
            'url': f"https://www.4byte.directory/api/v1/signatures/?hex_signature=0x{method_id}"
        }
    ]

    # Intentar con bases de datos online
    for api in signature_apis:
        try:
            print(f"\nConsultando {api['name']}...")
            response = requests.get(api['url'], timeout=10)
            print(f"Status code de {api['name']}: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"Respuesta de {api['name']}: {data}")
                
                if api['name'] == '4byte.directory':
                    if data['results']:
                        signature = data['results'][0]['text_signature']
                        print(f"Firma encontrada en {api['name']}: {signature}")
                        return {
                            'method_id': f"0x{method_id}",
                            'name': signature.split('(')[0],
                            'signature': signature,
                            'source': api['name']
                        }
                    else:
                        print(f"No se encontraron resultados en {api['name']}")
            else:
                print(f"Error en la respuesta de {api['name']}: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error al consultar {api['name']}: {e}")
            continue
    
    # Segundo intento de cálculo con más combinaciones
    try:
        # Intentar con más combinaciones de tipos
        extended_types = [
            ['uint256', 'address'],
            ['address[]'],
            ['uint256[]'],
            ['bytes32'],
            ['string', 'uint256'],
            ['address', 'bool'],
            ['uint256', 'bytes'],
            ['address', 'uint256', 'uint256'],
            ['address', 'address', 'uint256'],
            ['uint256', 'uint256', 'uint256']
        ]
        
        w3 = Web3()
        selector = bytes.fromhex(method_id)
        
        for types in extended_types:
            try:
                # Probar con nombres de funciones comunes
                for func_name in ['get', 'set', 'add', 'remove', 'update', 'check', 'is', 'has']:
                    signature = f"{func_name}({','.join(types)})"
                    if w3.keccak(text=signature)[:4] == selector:
                        print(f"Firma encontrada por cálculo extendido")
                        return {
                            'method_id': f"0x{method_id}",
                            'name': signature.split('(')[0],
                            'signature': signature,
                            'source': 'cálculo extendido'
                        }
            except:
                continue
                
    except Exception as e:
        print(f"Error en cálculo extendido: {e}")
    
    print(f"\nNo se encontró la firma en ninguna fuente")
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
    "0x8e1a55fc","0xf39b5b9b","0x095ea7b3","0xddf7e1a7","0xc2998238","0xf3541901","0xa0712d68","0x1249c58b","0xc5ebeaec","0x852a12e3","0xdb006a75","0x4e07008d","0x546cb17e","0x4254b155","0x0bde6eb7","0x39039497","0x6b1d4db7","0xd2d0e066","0x082fef45","0xfbabdebd","0xa9059cbb","0x1cff79cd","0x29589f61","0x8f6ede1f","0x40c10f19","0x9dc29fac","0x81a6b250","0x5a3b74b9","0x95e3c50b","0x422f1043","0x03152429","0xf88bf15a","0xf88309d7","0xa67a6a45","0xab832b43","0x23440944","0xc858f5f9","0x3ccfd60b","0x5ceae9c4","0xfc6f4e16","0x0b4c7e4d","0x8059cf3b","0x48ca1300","0x02cce70b","0xd0e30db0","0x34e7a19f","0xb02f0b73","0x6cfd80c9","0x517a55a3","0xe9af0292","0xa694fc3a","0x77f61403","0x4515cef3","0xb6b55f25","0xb384abef","0x2cefff96","0x7891c043","0x3d18b912","0x029b2f34","0xbb7e70ef","0x1aa3a008","0x86a50535","0x53fa2eb7","0x0e752702","0x75d9aa1a","0x38ed1739","0xf305d719","0xe8e33700","0x5c19a95c","0xe9fad8ee","0x1e83409a","0x415565b0","0xe0e90acf","0xee857b69","0x65fc3873","0xde5f6268","0xd7136328","0xa453b6cf","0xe2b39746","0x2e1a7d4d","0x4b820093","0x1e9a6950","0x46ab38f1","0x7d49d875","0x6a627842","0x4957677c","0xeff7a612","0xdf133bca","0x3df02124","0x61b69abd","0x2e7ba6ef","0x18cbafe5","0x1a4d01d2","0xae591d54","0x4e71d92d","0x8fd3ab80","0xe63d38ed","0x682356c0","0xadc9772e","0x9a99b4f0","0x7ff36ab5","0x853828b6","0x27bed8ee","0x47e7ef24","0xf3ae6c5f","0xd1058e59","0xfa09e630","0xc59203af","0x787a08a6","0xc804c39a","0xded9382a","0xe4a76726","0x05ea4671","0x21ef328f","0xae0b51df","0x90411a32","0x3049105d","0xdb0cd51d","0x0e89439b","0x2195995c","0xe2bbb158","0xd47eaa37","0x2e95b6c8","0x94bf804d","0x5915d806","0x7c025200","0x2e17de78","0x379607f5","0x9b172b35","0xc8fd6ed0","0xc04b8d59","0xf64db050","0xac9650d8","0x782ed90c","0x52bbbe29","0x7f8661a1","0x993e1c42","0xa0bd0d90","0x5ae401dc","0xd65a06b0","0x7617b389","0x372500ab","0xb77d239b","0xfb0f3ee1","0x42842e0e","0x5dfd9bc3","0xbe297476","0xefef39a1","0x3593564c","0x9db4f7aa","0x5f575529","0x630d8c63","0xd64bc331","0x5c9c18e2","0xb95cac28","0x2b630140","0xfa6e671d","0x8bdb3913","0x27f91856","0x24600fc3","0x8a10555c","0x6e553f65","0xba087652","0xcae9ca51","0xb16eb351","0x0b8c759a","0xeda6a5bc","0x441a3e70","0xa1251d75","0xf1dc3cc9","0xe8eda9df","0xa415bcad","0x573ade81","0xd3454a35","0x4db9dc97","0x69328dec","0x474cf53d","0xab9c4b5d","0xc04a8a10","0x66514c97","0x02c5fcf8","0x12aa3caf","0x617ba037","0xb38e9637","0xb4ba9e11","0x3ff9dcb1","0x7b939232","0x02751cec","0x66cb427c","0xb2267a7b","0xced78795","0x51905636","0x94ec6d78","0x7d10c9d6","0xfefe409d","0x410404b7","0x26b89ad7","0x53c43f15","0x7ba0e2e7","0x40d097c3","0x2cc4081e","0x5b7d7482","0xd7570e45","0x80500d20","0x9c4d535b","0xcfafc1c7","0xe685e541","0x236300dc","0xc002c4d6","0x126928c4","0x62915306","0xc35af429","0x65f0f5c2","0xa4d73041","0x745400c9","0x60806040","0x2f52ebb7","0x3e49fb7e","0x186aaba2","0xe84d494b","0xdcbb8e41","0x00528fbf","0x4737576e","0x3c042715","0x3d13f874","0xfb689088","0xeb1432f0","0xdeadbeef","0x4869203a","0x48692c20","0x05220422","0x1f91559b","0x546f6461","0x23526963","0x52696361","0x49276d20","0x5072696d","0xe5ae9de8","0x54796c65","0x04d65726","0x50726576","0x3e231629","0x49206265","0x54686520","0x706c6561","0x5468616e","0x146ca531","0x49207769","0xf83dd82a","0x706c7320","0x44726167","0x30787669","0x42415345","0x307861c3","0x68747470","0x49206761","0x41682066","0x3078444d","0x791ac947","0x0a492776","0x5b0d5984","0xcfd7789c","0x48656c6c","0x446f6765","0x44656172","0x486f7065","0x506c6561","0x49732053","0x41205761","0x49207375","0x434f4e47","0x436f6f6b","0x56622067","0x30783431","0x49207761","0x41206e65","0x57652061","0x62656962","0x29b82bb8","0x048692c2","0x68696166","0x76122903","0x46657720","0x4b482041","0x74686973","0xe2809457","0x48657920","0x416e6420","0x49742773","0x596f7572","0xb478d000","0x58525020","0xa22cb465","0x46697273","0x42444c43","0x48692056","0x33342e36","0x34664e4f","0x48692042","0x56420a0a","0x58585858","0x63616e63","0x1c196aaa","0x20202020","0x446f6c70","0x456e6f75","0x0ae3818b","0x644b617a","0x336e6420","0x49206c65","0x2e2e2e49","0x746f206d","0x41207472","0x57687920","0x41726520","0x57656c63","0x7468616e","0x536f2050","0x56697461","0x48617070","0x4c6f6f6b","0x22544845","0x596f7520","0x2450454e","0x64617920","0x30783638","0x74686520","0x54616b65","0x596f2056","0x4c657427","0x562e2057","0x68696969","0x50555420","0x436f6e67","0x24544845","0x57452041","0x536f6d65","0x57652077","0x57652068","0x57656273","0x4f6e6520","0x4c61756e","0x4d657272","0x43727970","0xf09f94b4","0xf09f9fa2","0x73757a75","0x56495441","0x45544845","0x5768656e","0x23464146","0x42534320","0x48692065","0x69206e65","0x89afcb44","0x4e656564","0x322bba21","0x6675636b","0xe6ada3e6","0x796f7520","0x536f6c61","0x78323320","0x72796f73","0x4f4c4420","0x49206665","0x61251af2","0xac7cc948","0x57652772","0xe29aa120","0x42756c6c","0x49207265","0x4b74756c","0x416c6c20","0x4a757374","0x24534849","0x68692e20","0x41207375","0x43686572","0x434f4e53","0x4578706c","0x0b86a4c1","0x42616279","0x6c697374","0x576f756c","0x54686973","0x76697461","0x556e6265","0x676d2076","0x24414749","0x50726976","0x4d6f726e","0x4c697474","0x466f7220","0x7662206a","0x54727920","0x20492068","0xe280a6e2","0x632a2055","0x53657667","0x596f2c20","0x4d792066","0x24454d53","0x53686f72","0x456c6f6e","0x52656164","0xb61d27f6","0x6e696767","0x466f6c6c","0x00490020","0x00490027","0x0059006f","0x43617265","0x32392e39","0x4920666f","0x41243844","0x49207365","0x5620726f","0x53686962","0x36206461","0xd9627aa4","0x496d6167","0x5368616d","0x68617070","0x75465a78","0x8af033fb","0x6865792c","0x50656570","0x70657065","0x4e6f7720","0x49206861","0x2444444f","0x62696c6c","0x3531aabc","0x30783962","0x455a4f0a","0xd0a1d0be","0x4c6f7265","0x8a6d46f0","0x4920616d","0x52656769","0x2f686f6d","0x74657374","0x0a77656c","0x53617920","0xd85d3d27","0xb510391f","0xeb672419","0xfaf039f4","0x8ae541cb","0xe6c6b7f0","0xbc67e887","0xa6f95726","0xf6d36ccb","0x6a40701c","0x5c11d795","0xed9999ca","0x0ec32977","0xfb3bdb41","0x38ef3649","0x88f56f09","0xb88a802f","0x35e4365f","0xec32ee72","0xdfcbb4a0","0xdd78d136","0xb5a4618e","0x2851ff81","0xd0febe4c","0x310f2668","0x44ddc37b","0xb6ace2fd","0x598647f8","0x8c4e7e2a","0x1071a290","0x51ed8288","0x5334e8b4","0x82c07d5d","0xcf4df16f","0x0df45469","0x2fb44d15","0x13f78a49","0xbaa2abde","0xaa7415f5","0xd7bb99ba","0xbe27b22c","0x3ce33bff","0x2e4dbe8f","0xf75e0384","0xcfc93274","0xfa021524","0xc7a50eba","0x095c9d8e","0xf2c298be","0x87260a7c","0x0000000d","0x47175878","0xad823822","0xc132e27f","0x643654d5","0xb969b4bf","0xb5d011c3","0xbb4cee01","0xc9b298f1","0x0f93d622","0x821ac41b","0xd365a377","0x5590febd","0xc83980dd","0x9a98f01b","0x39bf70d1","0x8cd6944a","0xbeebc5da","0xb48951e4","0x6af8e7eb","0x24904cb3","0x5c833bfd","0x79433d8b","0xac7b22dc","0x0df96f55","0xb9d2d7ed","0x23b872dd","0x0c01a2fd","0x5b713eb3","0xd96a094a","0x18a13086","0x9caf2b97","0x353766c6","0xdb6b5246","0x84a7f3dd","0x64617461","0xfd74537f","0x7b2151e5","0xef171686","0x39f47693","0xeeaa0e21","0xc47f0027","0x07ed2379","0x83bd37f9","0xed6e45c8","0xd9883315","0x917905da","0xe9125120","0x2646478b","0x6b634a62","0x3f6dc453","0xf7f3f2fd","0xf5c358c6","0x24856bc3"

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




