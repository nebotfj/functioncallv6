"""1inch Protocol Functions for all versions"""

ONEINCH_V5_FUNCTIONS = {
    'SWAP': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'unoswap': {
            'direction': 'BOTH',
            'description': 'Executes optimized swap',
            'method': '0x0502b1c5'
        },
        'clipperSwap': {
            'direction': 'BOTH',
            'description': 'Executes Clipper swap',
            'method': '0x84bd6d29'
        },
        'fillOrder': {
            'direction': 'BOTH',
            'description': 'Fills limit order',
            'method': '0xbc61394a'
        },
        'swapWithPermit': {
            'direction': 'BOTH',
            'description': 'Swaps with permit signature',
            'method': '0x2521b930'
        }
    },
    'LIMIT_ORDER': {
        'placeLimitOrder': {
            'direction': 'OUTGOING',
            'description': 'Places limit order',
            'method': '0x94b576de'
        },
        'cancelLimitOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels limit order',
            'method': '0x2e1a7d4d'
        },
        'fillLimitOrder': {
            'direction': 'BOTH',
            'description': 'Fills limit order',
            'method': '0xbc61394a'
        }
    },
    'AGGREGATION': {
        'discountedSwap': {
            'direction': 'BOTH',
            'description': 'Executes discounted swap',
            'method': '0x2f4f5cc5'
        },
        'multiSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        },
        'megaSwap': {
            'direction': 'BOTH',
            'description': 'Executes mega swap',
            'method': '0x46c67b6d'
        }
    },
    'FARMING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens',
            'method': '0x2e1a7d4d'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4e71d92d'
        },
        'exit': {
            'direction': 'INCOMING',
            'description': 'Exits farming position',
            'method': '0xe9fad8ee'
        }
    }
}

# Combined functions for all versions
ONEINCH_FUNCTIONS = {
    'V5': ONEINCH_V5_FUNCTIONS
}