"""Platypus Protocol Functions for all versions"""

PLATYPUS_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'multiSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        }
    },
    'LIQUIDITY': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens to pool',
            'method': '0xb6b55f25'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws tokens from pool',
            'method': '0x2e1a7d4d'
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
    'VESTING': {
        'lock': {
            'direction': 'OUTGOING',
            'description': 'Locks tokens for vesting',
            'method': '0x6d0a6f36'
        },
        'unlock': {
            'direction': 'INCOMING',
            'description': 'Unlocks vested tokens',
            'method': '0x2f7d5e86'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims vested tokens',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
PLATYPUS_FUNCTIONS = {
    'V1': PLATYPUS_V1_FUNCTIONS
}