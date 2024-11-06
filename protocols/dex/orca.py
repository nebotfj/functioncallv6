"""Orca Protocol Functions for all versions"""

ORCA_V2_FUNCTIONS = {
    'SWAP': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'swapBaseIn': {
            'direction': 'BOTH',
            'description': 'Swaps exact input amount',
            'method': '0x9d2f32dd'
        },
        'swapBaseOut': {
            'direction': 'BOTH',
            'description': 'Swaps for exact output amount',
            'method': '0x7c025200'
        }
    },
    'WHIRLPOOLS': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new whirlpool position',
            'method': '0x88316456'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes whirlpool position',
            'method': '0x89afcb44'
        },
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies existing position',
            'method': '0x0c49ccbe'
        },
        'collectFees': {
            'direction': 'INCOMING',
            'description': 'Collects earned fees',
            'method': '0x4f1eb3d8'
        }
    },
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x441a3e70'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf69e2046'
        }
    },
    'DOUBLE_DIP': {
        'depositDD': {
            'direction': 'OUTGOING',
            'description': 'Stakes in double dip pool',
            'method': '0x6e553f65'
        },
        'withdrawDD': {
            'direction': 'INCOMING',
            'description': 'Withdraws from double dip pool',
            'method': '0x441a3e70'
        },
        'harvestDD': {
            'direction': 'INCOMING',
            'description': 'Claims double dip rewards',
            'method': '0x4641257d'
        }
    }
}

# Combined functions for all versions
ORCA_FUNCTIONS = {
    'V2': ORCA_V2_FUNCTIONS
}