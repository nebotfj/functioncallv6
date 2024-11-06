"""Multichain (Anyswap) Bridge Protocol Functions for all versions"""

MULTICHAIN_V3_FUNCTIONS = {
    'BRIDGE': {
        'anySwapOut': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens out',
            'method': '0x8b9e4f93'
        },
        'anySwapIn': {
            'direction': 'INCOMING',
            'description': 'Receives bridged tokens',
            'method': '0x4ce38b5f'
        },
        'anySwapOutNative': {
            'direction': 'OUTGOING',
            'description': 'Bridges native tokens out',
            'method': '0xb1a1a882'
        },
        'anySwapInNative': {
            'direction': 'INCOMING',
            'description': 'Receives bridged native tokens',
            'method': '0x32b7006d'
        }
    },
    'ROUTER': {
        'swapExactTokensForTokens': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens',
            'method': '0x38ed1739'
        },
        'swapTokensForExactTokens': {
            'direction': 'BOTH',
            'description': 'Swaps for exact amount of tokens',
            'method': '0x8803dbee'
        },
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        }
    },
    'FARMING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x3d18b912'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
MULTICHAIN_FUNCTIONS = {
    'V3': MULTICHAIN_V3_FUNCTIONS
}