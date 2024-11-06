from protocols.aave import AAVE_FUNCTIONS
from protocols.compound import COMPOUND_FUNCTIONS
from protocols.cream import CREAM_FUNCTIONS
from protocols.dex.uniswap import UNISWAP_FUNCTIONS
from protocols.dex.sushiswap import SUSHISWAP_FUNCTIONS
from protocols.dex.pancakeswap import PANCAKESWAP_FUNCTIONS
from protocols.dex.balancer import BALANCER_FUNCTIONS
from protocols.dex.bancor import BANCOR_FUNCTIONS
from protocols.dex.curve import CURVE_FUNCTIONS
from protocols.dex.beethoven import BEETHOVEN_FUNCTIONS
from protocols.dex.biswap import BISWAP_FUNCTIONS
from protocols.dex.camelot import CAMELOT_FUNCTIONS
from protocols.dex.chronos import CHRONOS_FUNCTIONS
from protocols.dex.dodo import DODO_FUNCTIONS
from protocols.dex.dystopia import DYSTOPIA_FUNCTIONS
from protocols.dex.gmx import GMX_FUNCTIONS
from protocols.dex.gnosis import GNOSIS_FUNCTIONS
from protocols.dex.hashflow import HASHFLOW_FUNCTIONS
from protocols.dex.kyberswap import KYBERSWAP_FUNCTIONS

def search_function(function_name):
    protocols = {
        'AAVE': AAVE_FUNCTIONS,
        'COMPOUND': COMPOUND_FUNCTIONS,
        'CREAM': CREAM_FUNCTIONS,
        'UNISWAP': UNISWAP_FUNCTIONS,
        'SUSHISWAP': SUSHISWAP_FUNCTIONS,
        'PANCAKESWAP': PANCAKESWAP_FUNCTIONS,
        'BALANCER': BALANCER_FUNCTIONS,
        'BANCOR': BANCOR_FUNCTIONS,
        'CURVE': CURVE_FUNCTIONS,
        'BEETHOVEN': BEETHOVEN_FUNCTIONS,
        'BISWAP': BISWAP_FUNCTIONS,
        'CAMELOT': CAMELOT_FUNCTIONS,
        'CHRONOS': CHRONOS_FUNCTIONS,
        'DODO': DODO_FUNCTIONS,
        'DYSTOPIA': DYSTOPIA_FUNCTIONS,
        'GMX': GMX_FUNCTIONS,
        'GNOSIS': GNOSIS_FUNCTIONS,
        'HASHFLOW': HASHFLOW_FUNCTIONS,
        'KYBERSWAP': KYBERSWAP_FUNCTIONS
    }
    
    results = []
    
    for protocol_name, protocol_data in protocols.items():
        for version, categories in protocol_data.items():
            for category, functions in categories.items():
                if function_name in functions:
                    results.append({
                        'protocol': protocol_name,
                        'version': version,
                        'category': category,
                        'details': functions[function_name]
                    })
    
    return results

def main():
    print("Welcome to DeFi Function Analyzer")
    print("Enter function names separated by comma (or 'exit' to quit)")
    
    while True:
        user_input = input("\nEnter function name(s): ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        functions = [f.strip() for f in user_input.split(',')]
        
        for function in functions:
            results = search_function(function)
            
            if results:
                print(f"\nResults for '{function}':")
                for result in results:
                    print(f"\nProtocol: {result['protocol']} {result['version']}")
                    print(f"Category: {result['category']}")
                    print(f"Direction: {result['details']['direction']}")
                    print(f"Description: {result['details']['description']}")
                    print(f"Method ID: {result['details']['method']}")
            else:
                print(f"\nFunction '{function}' not found in any protocol")