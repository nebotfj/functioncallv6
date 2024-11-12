import os
import ast

# Ruta a la carpeta de protocolos
protocolos_path = 'protocolos'

# Lista para almacenar los method_id conocidos
known_method_ids = []

# Recorre los archivos en la carpeta de protocolos
for root, dirs, files in os.walk(protocolos_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                try:
                    # Intenta parsear el contenido del archivo como un AST
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Dict):
                            for key, value in zip(node.keys, node.values):
                                if isinstance(value, ast.Dict):
                                    for subkey, subvalue in zip(value.keys, value.values):
                                        if isinstance(subkey, ast.Str) and subkey.s == 'method':
                                            if isinstance(subvalue, ast.Str):
                                                known_method_ids.append(subvalue.s)
                except SyntaxError:
                    print(f"Error de sintaxis en el archivo: {file_path}")

# Method IDs que deseas identificar
unknown_method_ids = [
    "0x8e1a55fc","0xf39b5b9b","0x095ea7b3","0xddf7e1a7","0xc2998238","0xf3541901","0xa0712d68","0x1249c58b","0xc5ebeaec","0x852a12e3","0xdb006a75","0x4e07008d","0x546cb17e","0x4254b155","0x0bde6eb7","0x39039497","0x6b1d4db7","0xd2d0e066","0x082fef45","0xfbabdebd","0xa9059cbb","0x1cff79cd","0x29589f61","0x8f6ede1f","0x40c10f19","0x9dc29fac","0x81a6b250","0x5a3b74b9","0x95e3c50b","0x422f1043","0x03152429","0xf88bf15a","0xf88309d7","0xa67a6a45","0xab832b43","0x23440944","0xc858f5f9","0x3ccfd60b","0x5ceae9c4","0xfc6f4e16","0x0b4c7e4d","0x8059cf3b","0x48ca1300","0x02cce70b","0xd0e30db0","0x34e7a19f","0xb02f0b73","0x6cfd80c9","0x517a55a3","0xe9af0292","0xa694fc3a","0x77f61403","0x4515cef3","0xb6b55f25","0xb384abef","0x2cefff96","0x7891c043","0x3d18b912","0x029b2f34","0xbb7e70ef","0x1aa3a008","0x86a50535","0x53fa2eb7","0x0e752702","0x75d9aa1a","0x38ed1739","0xf305d719","0xe8e33700","0x5c19a95c","0xe9fad8ee","0x1e83409a","0x415565b0","0xe0e90acf","0xee857b69","0x65fc3873","0xde5f6268","0xd7136328","0xa453b6cf","0xe2b39746","0x2e1a7d4d","0x4b820093","0x1e9a6950","0x46ab38f1","0x7d49d875","0x6a627842","0x4957677c","0xeff7a612","0xdf133bca","0x3df02124","0x61b69abd","0x2e7ba6ef","0x18cbafe5","0x1a4d01d2","0xae591d54","0x4e71d92d","0x8fd3ab80","0xe63d38ed","0x682356c0","0xadc9772e","0x9a99b4f0","0x7ff36ab5","0x853828b6","0x27bed8ee","0x47e7ef24","0xf3ae6c5f","0xd1058e59","0xfa09e630","0xc59203af","0x787a08a6","0xc804c39a","0xded9382a","0xe4a76726","0x05ea4671","0x21ef328f","0xae0b51df","0x90411a32","0x3049105d","0xdb0cd51d","0x0e89439b","0x2195995c","0xe2bbb158","0xd47eaa37","0x2e95b6c8","0x94bf804d","0x5915d806","0x7c025200","0x2e17de78","0x379607f5","0x9b172b35","0xc8fd6ed0","0xc04b8d59","0xf64db050","0xac9650d8","0x782ed90c","0x52bbbe29","0x7f8661a1","0x993e1c42","0xa0bd0d90","0x5ae401dc","0xd65a06b0","0x7617b389","0x372500ab","0xb77d239b","0xfb0f3ee1","0x42842e0e","0x5dfd9bc3","0xbe297476","0xefef39a1","0x3593564c","0x9db4f7aa","0x5f575529","0x630d8c63","0xd64bc331","0x5c9c18e2","0xb95cac28","0x2b630140","0xfa6e671d","0x8bdb3913","0x27f91856","0x24600fc3","0x8a10555c","0x6e553f65","0xba087652","0xcae9ca51","0xb16eb351","0x0b8c759a","0xeda6a5bc","0x441a3e70","0xa1251d75","0xf1dc3cc9","0xe8eda9df","0xa415bcad","0x573ade81","0xd3454a35","0x4db9dc97","0x69328dec","0x474cf53d","0xab9c4b5d","0xc04a8a10","0x66514c97","0x02c5fcf8","0x12aa3caf","0x617ba037","0xb38e9637","0xb4ba9e11","0x3ff9dcb1","0x7b939232","0x02751cec","0x66cb427c","0xb2267a7b","0xced78795","0x51905636"
]

# Compara los method_id desconocidos con los conocidos
for method_id in unknown_method_ids:
    if method_id in known_method_ids:
        print(f"El method_id {method_id} se ha identificado en los archivos.")
    else:
        print(f"El method_id {method_id} no se pudo identificar.")
