"""Mycelium Protocol Functions for all versions"""

MYCELIUM_V1_FUNCTIONS = {
    'PERPETUALS': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new perpetual position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes existing position',
            'method': '0x82a08fcd'
        },
        'addToPosition': {
            'direction': 'OUTGOING',
            'description': 'Increases position size',
            'method': '0x219f5d17'
        },
        'reducePosition': {
            'direction': 'INCOMING',
            'description': 'Reduces position size',
            'method': '0x0c49ccbe'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        }
    },
    'STAKING': {
        'stakeMYC': {
            'direction': 'OUTGOING',
            'description': 'Stakes MYC tokens',
            'method': '0xa694fc3a'
        },
        'unstakeMYC': {
            'direction': 'INCOMING',
            'description': 'Unstakes MYC tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
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
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees',
            'method': '0xd294f093'
        }
    }
}

# Combined functions for all versions
MYCELIUM_FUNCTIONS = {
    'V1': MYCELIUM_V1_FUNCTIONS
}