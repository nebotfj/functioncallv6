"""MixSwap Protocol Functions for all versions"""

MIXSWAP_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'multiSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'routeSwap': {
            'direction': 'BOTH',
            'description': 'Executes routed swap',
            'method': '0x7c025200'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        },
        'zapIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps token into LP position',
            'method': '0x6c2a8f5d'
        },
        'zapOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of LP position',
            'method': '0x4c9bb61d'
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
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        }
    }
}

# Combined functions for all versions
MIXSWAP_FUNCTIONS = {
    'V1': MIXSWAP_V1_FUNCTIONS
}