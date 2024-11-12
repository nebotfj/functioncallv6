from web3 import Web3

# Establece la conexión con la red de Ethereum
web3 = Web3()

# ABI de ejemplo (deberías reemplazar esto con el ABI real de tu contrato)
# En este caso solo es una lista de ejemplos de las firmas de las funciones
contract_abi = [
    {
        "constant": True,
        "inputs": [{"name": "to", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    # Aquí puedes añadir más funciones de tu ABI
]

# Lista de method_ids que deseas decodificar
method_ids = [
    "0xc9b298f1", "0x0f93d622", "0x821ac41b", "0xd365a377", "0x5590febd",
    "0xc83980dd", "0x9a98f01b", "0x39bf70d1", "0x8cd6944a", "0xbeebc5da",
    "0xb48951e4", "0x6af8e7eb", "0x24904cb3", "0x5c833bfd", "0x79433d8b",
    "0xac7b22dc", "0x0df96f55", "0xb9d2d7ed", "0x23b872dd", "0x0c01a2fd",
    "0x5b713eb3", "0xd96a094a", "0x18a13086", "0x9caf2b97", "0x353766c6",
    "0xdb6b5246", "0x84a7f3dd", "0x64617461", "0xfd74537f", "0x7b2151e5",
    "0xef171686", "0x39f47693", "0xeeaa0e21", "0xc47f0027", "0x07ed2379",
    "0x83bd37f9", "0xed6e45c8", "0xd9883315", "0x917905da", "0xe9125120",
    "0x2646478b", "0x6b634a62", "0x3f6dc453", "0xf7f3f2fd", "0xf5c358c6",
    "0x24856bc3"
]

# Función para encontrar la función correspondiente a un method_id
def find_function_for_method_id(method_id):
    for item in contract_abi:
        # Obtenemos el selector (method_id) de la firma de la función
        function_signature = f"{item['name']}({','.join([i['type'] for i in item['inputs']])})"
        encoded_signature = web3.keccak(text=function_signature).hex()[:10]  # Los primeros 4 bytes son el method_id
        if encoded_signature == method_id.lower():
            return item['name']
    return None

# Decodificar todos los method_ids
for method_id in method_ids:
    function_name = find_function_for_method_id(method_id)
    if function_name:
        print(f"El method_id {method_id} corresponde a la función: {function_name}")
    else:
        print(f"El method_id {method_id} no se pudo identificar.")
