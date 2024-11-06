"""DODO Protocol Functions for all versions"""

DODO_V1_FUNCTIONS = {
    'TRADING': {
        'dodoSwap': {
            'direction': 'BOTH',
            'description': 'Performs DODO swap',
            'method': '0x5e9a1a5c'
        },
        'externalSwap': {
            'direction': 'BOTH',
            'description': 'Performs external swap',
            'method': '0x52f2db69'
        },
        'dodoMultiSwap': {
            'direction': 'BOTH',
            'description': 'Performs multiple swaps',
            'method': '0x6a628d19'
        },
        'routerSwap': {
            'direction': 'BOTH',
            'description': 'Performs router swap',
            'method': '0x7c025200'
        }
    },
    'LIQUIDITY': {
        'depositBase': {
            'direction': 'OUTGOING',
            'description': 'Deposits base token',
            'method': '0x4c505d91'
        },
        'depositQuote': {
            'direction': 'OUTGOING',
            'description': 'Deposits quote token',
            'method': '0x5a45c6fc'
        },
        'withdrawBase': {
            'direction': 'INCOMING',
            'description': 'Withdraws base token',
            'method': '0xb9f3eb49'
        },
        'withdrawQuote': {
            'direction': 'INCOMING',
            'description': 'Withdraws quote token',
            'method': '0x01b7dfa5'
        },
        'buyShares': {
            'direction': 'OUTGOING',
            'description': 'Buys pool shares',
            'method': '0x8f38249c'
        },
        'sellShares': {
            'direction': 'INCOMING',
            'description': 'Sells pool shares',
            'method': '0x454a2ab3'
        }
    },
    'POOL': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new pool',
            'method': '0x1698ee82'
        },
        'resetPool': {
            'direction': 'OUTGOING',
            'description': 'Resets pool parameters',
            'method': '0x44c0bd98'
        },
        'bidPool': {
            'direction': 'OUTGOING',
            'description': 'Places bid in pool',
            'method': '0x454a2ab3'
        },
        'askPool': {
            'direction': 'OUTGOING',
            'description': 'Places ask in pool',
            'method': '0x2f4f5cc5'
        },
        'updatePool': {
            'direction': 'OUTGOING',
            'description': 'Updates pool parameters',
            'method': '0x7535d246'
        }
    },
    'VENDING_MACHINE': {
        'createVendingMachine': {
            'direction': 'OUTGOING',
            'description': 'Creates new vending machine',
            'method': '0x8a8c523c'
        },
        'buyFromVending': {
            'direction': 'OUTGOING',
            'description': 'Buys from vending machine',
            'method': '0x2c70b603'
        },
        'sellToVending': {
            'direction': 'INCOMING',
            'description': 'Sells to vending machine',
            'method': '0x3fdddaa2'
        },
        'updateVending': {
            'direction': 'OUTGOING',
            'description': 'Updates vending machine parameters',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
DODO_FUNCTIONS = {
    'V1': DODO_V1_FUNCTIONS
}