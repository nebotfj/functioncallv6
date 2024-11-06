import protocols

from protocols.bridges import across, allbridge, arbitrum, celer, hop, layerzero, multichain, optimism, orbiter, polygon, portal, stargate, symbiosis, synapse, wormhole
from protocols.derivatives import drift, dydx, gains, gmx, hubble, kwenta, level, mycelium, perpetual, polynomial, ribbon, synthetix, vela
from protocols.dex import balancer, bancor, beethoven, biswap, camelot, chronos, curve, dodo, dystopia, gmx, gnosis, hashflow, kyberswap, loopring, maverick, meshswap, mixswap, oneinch, orca, pancakeswap, paraswap, platypus, quickswap, ramses, raydium, solidly, spiritswap, spookyswap, sushiswap, traderjoe, uniswap, velodrome, vulpefi, wombat, zapper, zerion, zeroex, zyberswap
from protocols. gaming import 
from protocols.identity import brightid, civic, polygonid, worldcoin
from protocols.infrastructure import arweave, filecoin, ipfs, pocket, the_graph
from protocols.insurance import insurace, nexus_mutual, unslashed
from protocols. launchpad import bullperks, gamefi, gamestarter, launchpad_repasar
from protocols.lending import aave, benqi, compound, cream, euler, frax, geist, granary, hundred, ironbank, maple, maker, morpho, radiant, venus
from protocols.mev import 
from protocols.nft import 
from protocols.options import 
from protocols.oracles import 
from protocols.privacy import 
from protocols.rwa import centrifuge, goldfinch, maple, truefi
from protocols.social_media import farcaster, friend_tech, lens
from protocols.staking import 
from protocols.tokens import erc1155, erc20, erc2981, erc3525, erc4626, erc5192, erc721
from protocols.yield_farming import

from aave import AAVE_FUNCTIONS

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