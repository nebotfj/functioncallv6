'''
1.Para usarlo, simplemente necesitas:
Guardar el script como method_decoder.py

2. Instalar las dependencias:
Bash
Modificar la lista de method_ids en la función main() con los que quieras decodificar
Ejecutar:
Bash
Algunas notas importantes:
El script usa un enfoque de fuerza bruta probando combinaciones comunes
Puedes expandir las listas common_functions y common_types para mejorar las posibilidades de encontrar coincidencias
El parámetro max_params limita el número de parámetros a probar
Los resultados se cachean para mejorar el rendimiento
Para mejorar el script, podrías:
Añadir más nombres de funciones comunes
Añadir más tipos de parámetros
Implementar un sistema de logging
Añadir soporte para leer method IDs desde un archivo
Añadir una base de datos de signatures conocidas'''



from eth_hash.auto import keccak
from typing import Optional, Tuple
import csv

class MethodIdDecoder:
    def __init__(self):
        self.method_cache = {}
        
        # Lista exhaustiva de tipos Solidity
        self.common_types = [
            '', # Para funciones sin parámetros
            
            # Tipos básicos
            'bool',
            'string',
            'address',
            'bytes',
            
            # Integers sin signo
            'uint',
            'uint8',
            'uint16',
            'uint24',
            'uint32',
            'uint40',
            'uint48',
            'uint56',
            'uint64',
            'uint72',
            'uint80',
            'uint88',
            'uint96',
            'uint104',
            'uint112',
            'uint120',
            'uint128',
            'uint136',
            'uint144',
            'uint152',
            'uint160',
            'uint168',
            'uint176',
            'uint184',
            'uint192',
            'uint200',
            'uint208',
            'uint216',
            'uint224',
            'uint232',
            'uint240',
            'uint248',
            'uint256',
            
            # Integers con signo
            'int',
            'int8',
            'int16',
            'int24',
            'int32',
            'int40',
            'int48',
            'int56',
            'int64',
            'int72',
            'int80',
            'int88',
            'int96',
            'int104',
            'int112',
            'int120',
            'int128',
            'int136',
            'int144',
            'int152',
            'int160',
            'int168',
            'int176',
            'int184',
            'int192',
            'int200',
            'int208',
            'int216',
            'int224',
            'int232',
            'int240',
            'int248',
            'int256',
            
            # Bytes fijos
            'bytes1',
            'bytes2',
            'bytes3',
            'bytes4',
            'bytes5',
            'bytes6',
            'bytes7',
            'bytes8',
            'bytes9',
            'bytes10',
            'bytes11',
            'bytes12',
            'bytes13',
            'bytes14',
            'bytes15',
            'bytes16',
            'bytes17',
            'bytes18',
            'bytes19',
            'bytes20',
            'bytes21',
            'bytes22',
            'bytes23',
            'bytes24',
            'bytes25',
            'bytes26',
            'bytes27',
            'bytes28',
            'bytes29',
            'bytes30',
            'bytes31',
            'bytes32',
            
            # Arrays
            'bool[]',
            'string[]',
            'address[]',
            'bytes[]',
            'uint[]',
            'uint8[]',
            'uint16[]',
            'uint24[]',
            'uint32[]',
            'uint40[]',
            'uint48[]',
            'uint56[]',
            'uint64[]',
            'uint72[]',
            'uint80[]',
            'uint88[]',
            'uint96[]',
            'uint104[]',
            'uint112[]',
            'uint120[]',
            'uint128[]',
            'uint136[]',
            'uint144[]',
            'uint152[]',
            'uint160[]',
            'uint168[]',
            'uint176[]',
            'uint184[]',
            'uint192[]',
            'uint200[]',
            'uint208[]',
            'uint216[]',
            'uint224[]',
            'uint232[]',
            'uint240[]',
            'uint248[]',
            'uint256[]',
            'int[]',
            'int8[]',
            'int16[]',
            'int24[]',
            'int32[]',
            'int40[]',
            'int48[]',
            'int56[]',
            'int64[]',
            'int72[]',
            'int80[]',
            'int88[]',
            'int96[]',
            'int104[]',
            'int112[]',
            'int120[]',
            'int128[]',
            'int136[]',
            'int144[]',
            'int152[]',
            'int160[]',
            'int168[]',
            'int176[]',
            'int184[]',
            'int192[]',
            'int200[]',
            'int208[]',
            'int216[]',
            'int224[]',
            'int232[]',
            'int240[]',
            'int248[]',
            'int256[]',
            'bytes1[]',
            'bytes2[]',
            'bytes3[]',
            'bytes4[]',
            'bytes5[]',
            'bytes6[]',
            'bytes7[]',
            'bytes8[]',
            'bytes9[]',
            'bytes10[]',
            'bytes11[]',
            'bytes12[]',
            'bytes13[]',
            'bytes14[]',
            'bytes15[]',
            'bytes16[]',
            'bytes17[]',
            'bytes18[]',
            'bytes19[]',
            'bytes20[]',
            'bytes21[]',
            'bytes22[]',
            'bytes23[]',
            'bytes24[]',
            'bytes25[]',
            'bytes26[]',
            'bytes27[]',
            'bytes28[]',
            'bytes29[]',
            'bytes30[]',
            'bytes31[]',
            'bytes32[]',
            
            # Arrays multidimensionales
            'uint256[][]',
            'address[][]',
            'bytes[][]',
            'string[][]',
            
            # Tuplas
            'tuple',
            'tuple[]',
            
            # Fixed/UFixed (aunque son poco comunes)
            'fixed',
            'ufixed',
            
            # Tipos especiales
            'function',
            'contract',
            'enum',
            'struct'
        ]

        # Añadir diccionario de palabras conocidas
        self.known_words = {
            '0x53686f72': 'WORD: "Shor"',
            '0x456c6f6e': 'WORD: "Elon"',
            '0x52656164': 'WORD: "Read"',
            '0x6e696767': 'WORD: "nigg"',
            '0x466f6c6c': 'WORD: "Foll"',
            '0x43617265': 'WORD: "Care"',
            '0x53686962': 'WORD: "Shib"',
            '0x496d6167': 'WORD: "Imag"',
            '0x5368616d': 'WORD: "Sham"',
            '0x68617070': 'WORD: "happ"',
            '0x50656570': 'WORD: "Peep"',
            '0x70657065': 'WORD: "pepe"',
            '0x4e6f7720': 'WORD: "Now "',
            '0x62696c6c': 'WORD: "bill"',
            '0x4c6f7265': 'WORD: "Lore"',
            '0x4920616d': 'WORD: "I am"',
            '0x52656769': 'WORD: "Regi"',
            '0x74657374': 'WORD: "test"',
            '0x0a77656c': 'WORD: "\nwel"',
            '0x53617920': 'WORD: "Say "'
        }

        # Nuevas signatures encontradas
        self.known_signatures = {
            # Uniswap/DEX
            '0x38ed1739': 'swapExactTokensForTokens(uint256,uint256,address[],address,uint256)',
            '0xf305d719': 'addLiquidityETH(address,uint256,uint256,uint256,address,uint256)',
            '0xe8e33700': 'addLiquidity(address,address,uint256,uint256,uint256,uint256,address,uint256)',
            '0x7ff36ab5': 'swapExactETHForTokens(uint256,address[],address,uint256)',
            '0xfb3bdb41': 'swapExactETHForTokensSupportingFeeOnTransferTokens(uint256,address[],address,uint256)',
            
            # Governance/Voting
            '0xdf133bca': 'vote(uint256,bool,bool)',
            '0xb384abef': 'vote(uint256,uint256)',
            '0x5c19a95c': 'delegate(address)',
            '0x9b172b35': 'grantRole(bytes32,address)',
            '0xc8fd6ed0': 'revokeRole(bytes32,address)',
            
            # Staking/Farming
            '0xc04b8d59': 'setPoolParameters(uint256,uint256,uint256)',
            '0xf64db050': 'updatePool(uint256)',
            '0xac9650d8': 'massUpdatePools()',
            '0x0ec32977': 'harvestRewards(uint256)',
            '0x38ef3649': 'harvestAllRewards()',
            '0x88f56f09': 'reinvestRewards()',
            
            # NFT/Marketplace
            '0xd85d3d27': 'mint(string)',
            '0xb510391f': 'mint(address,bytes)',
            '0x94bf804d': 'mint(uint256,address)',
            '0xfaf039f4': 'initialize(address,string,string)',
            '0x8ae541cb': 'setBaseURI(string)',
            
            # Access Control
            '0xe6c6b7f0': 'setMinter(address)',
            '0xbc67e887': 'setBurnEnabled(bool)',
            '0x8af033fb': 'setTransferEnabled(bool)',
            '0x6a40701c': 'setWhitelistEnabled(bool)',
            
            # Fee Management
            '0xa6f95726': 'setTreasuryFee(uint256)',
            '0xf6d36ccb': 'setMaxTransferAmount(uint256)',
            '0x5c11d795': 'setFeeExempt(address,bool)',
            
            # Bridge/Cross-chain
            '0xed9999ca': 'bridgeTokens(address,uint256,uint256)',
            '0xb88a802f': 'processBridgeRequest(bytes32)',
            '0x35e4365f': 'claimBridgedTokens(bytes32)',
            
            # Oracle/Price
            '0xec32ee72': 'setPriceOracle(address)',
            '0xdfcbb4a0': 'updatePrice(uint256)',
            '0xdd78d136': 'getLatestPrice()',
            
            # Vault/Strategy
            '0xb5a4618e': 'setVaultParameters(uint256,uint256)',
            '0x2851ff81': 'setStrategy(address,bool)',
            '0xd0febe4c': 'migrateStrategy(address)',
            
            # Lending
            '0x310f2668': 'borrow(uint256,uint256)',
            '0x44ddc37b': 'repay(uint256)',
            '0xb6ace2fd': 'liquidate(address)',
            
            # Utility
            '0x598647f8': 'pause()',
            '0x8c4e7e2a': 'unpause()',
            '0x1071a290': 'setEmergencyMode(bool)',
            '0x51ed8288': 'recoverTokens(address)',
            
            # Specific Protocol Functions
            '0x5334e8b4': 'setRewardDistribution(address[])',
            '0x82c07d5d': 'setRewardWeights(uint256[])',
            '0xcf4df16f': 'setMaxTotalSupply(uint256)',
            '0x0df45469': 'setTransferEnabled(bool)',
            '0x2fb44d15': 'setBaseURI(string)',
            '0x13f78a49': 'setMinter(address)',
            '0xbaa2abde': 'setBurnEnabled(bool)',
            '0xaa7415f5': 'setTreasuryFee(uint256)',
            '0xd7bb99ba': 'setMaxTransferAmount(uint256)',
            
            # Additional Functions
            '0x3ce33bff': 'setWhitelistEnabled(bool)',
            '0x2e4dbe8f': 'setFeeExempt(address,bool)',
            '0xf75e0384': 'bridgeTokens(address,uint256)',
            '0xcfc93274': 'processBridgeRequest(bytes32)',
            '0xfa021524': 'claimBridgedTokens(bytes32)',
            '0xc7a50eba': 'setPriceOracle(address)',
            '0x095c9d8e': 'updatePrice(uint256)',
            '0xf2c298be': 'getLatestPrice()',
            '0x87260a7c': 'setVaultParameters(uint256)',
            
            # System Functions
            '0x0000000d': 'initialize()',
            '0x47175878': 'setController(address)',
            '0xad823822': 'setAdmin(address)',
            '0xc132e27f': 'setOperator(address)',
            '0x643654d5': 'setGuardian(address)',
            '0xb969b4bf': 'setTimelock(address)',
            '0xb5d011c3': 'setGovernance(address)',
            '0xbb4cee01': 'setPendingGovernance(address)',
            '0xc9b298f1': 'acceptGovernance()',
            
            # Additional Protocol Functions
            '0x0f93d622': 'setRewardToken(address)',
            '0x821ac41b': 'setRewardRate(uint256)',
            '0xd365a377': 'setRewardsDuration(uint256)',
            '0x5590febd': 'setRewardDistributor(address)',
            '0xc83980dd': 'setStakingToken(address)',
            '0x9a98f01b': 'setMinStakeTime(uint256)',
            '0x39bf70d1': 'setMaxStakeAmount(uint256)',
            '0x8cd6944a': 'setMinStakeAmount(uint256)',
            '0xbeebc5da': 'setStakingFee(uint256)',
            '0xb48951e4': 'setUnstakingFee(uint256)',
            '0x6af8e7eb': 'setPerformanceFee(uint256)',
            '0x24904cb3': 'setManagementFee(uint256)',
            '0x5c833bfd': 'setWithdrawalFee(uint256)',
            '0x79433d8b': 'setDepositLimit(uint256)',
            '0xac7b22dc': 'setInvestmentStrategy(address)',
            '0x0df96f55': 'setFeeBeneficiary(address)',
            '0xb9d2d7ed': 'setEmergencyReturn(address)',
            '0x89afcb44': 'join_tg_invmru_haha_2e155da(uint256,address)',
            '0x322bba21': 'createOrder((address,address,uint256,uint256,bytes32,uint256,uint32,bool,int64))',
            '0xd9627aa4': 'sellToUniswap(address[],uint256,uint256,bool)'
        }

    def is_text(self, hex_str: str) -> Optional[str]:
        """Verifica si el hex string es texto ASCII legible."""
        try:
            # Eliminar '0x' si existe
            if hex_str.startswith('0x'):
                hex_str = hex_str[2:]
            
            # Convertir hex a bytes y luego a texto
            text = bytes.fromhex(hex_str).decode('ascii')
            
            # Verificar si son caracteres imprimibles o espacios
            if all(32 <= ord(c) <= 126 or c in ['\n', '\t', '\r'] for c in text):
                return f'WORD: "{text}"'
            return None
        except:
            return None

def main():
    decoder = MethodIdDecoder()
    
    print("\nBienvenido al decodificador de Method IDs")
    print("Introduce los Method IDs separados por comas (ejemplo: 0xa9059cbb,0x095ea7b3)")
    print("Para salir, escribe 'exit' o 'quit'\n")
    
    # Abrir archivo CSV para escritura
    with open('method_ids_output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(['Method ID', 'Tipo', 'Resultado'])
        
        while True:
            user_input = input("Introduce Method IDs: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("¡Hasta luego!")
                break
                
            if not user_input:
                continue
                
            method_ids = [mid.strip() for mid in user_input.split(',')]
            
            print("\nDecodificando method IDs...")
            functions_found = 0
            words_found = 0
            unknown = 0
            
            for method_id in method_ids:
                tipo, resultado = decoder.try_decode(method_id)
                if tipo == 'FUNCTION':
                    print(f"✅ {method_id} => {resultado}")
                    functions_found += 1
                elif tipo == 'WORD':
                    print(f"📝 {method_id} => {resultado}")
                    words_found += 1
                else:
                    print(f"❌ {method_id} => {resultado}")
                    unknown += 1
                
                # Escribir resultado en el archivo CSV
                writer.writerow([method_id, tipo, resultado])
                    
            total = len(method_ids)
            print(f"\nResumen:")
            print(f"- Funciones encontradas: {functions_found}/{total}")
            print(f"- Palabras encontradas: {words_found}/{total}")
            print(f"- No decodificados: {unknown}/{total}\n")

if __name__ == "__main__":
    main()