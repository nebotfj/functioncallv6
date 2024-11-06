"""Beethoven Protocol Functions for all versions"""

BEETHOVEN_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Performs single token swap',
            'method': '0x52bbbe29'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Performs multiple token swaps',
            'method': '0x945bcec9'
        },
        'smartSwap': {
            'direction': 'BOTH',
            'description': 'Performs optimized smart swap',
            'method': '0x7c025200'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        }
    },
    'LIQUIDITY': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xb95cac28'
        },
        'exitPool': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0x8bdb3913'
        },
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to specific pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from specific pool',
            'method': '0xbaa2abde'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x2e1a7d4d'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x3d18b912'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'GAUGE': {
        'depositLP': {
            'direction': 'OUTGOING',
            'description': 'Deposits LP tokens in gauge',
            'method': '0x6e553f65'
        },
        'withdrawLP': {
            'direction': 'INCOMING',
            'description': 'Withdraws LP tokens from gauge',
            'method': '0x441a3e70'
        },
        'claimBeets': {
            'direction': 'INCOMING',
            'description': 'Claims BEETS rewards',
            'method': '0xe6f1daf2'
        },
        'boostStake': {
            'direction': 'OUTGOING',
            'description': 'Boosts staking position',
            'method': '0x9b3f3d20'
        }
    }
}

# Combined functions for all versions
BEETHOVEN_FUNCTIONS = {
    'V1': BEETHOVEN_V1_FUNCTIONS
}