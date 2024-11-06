"""Loopring Protocol Functions for all versions"""

LOOPRING_V3_FUNCTIONS = {
    'TRADING': {
        'submitOrder': {
            'direction': 'OUTGOING',
            'description': 'Submits order to orderbook',
            'method': '0x6ce8c739'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'orderbook': {
            'direction': 'NEUTRAL',
            'description': 'Gets orderbook state',
            'method': '0x859c82c4'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
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
        'joinAMM': {
            'direction': 'OUTGOING',
            'description': 'Joins AMM pool',
            'method': '0x5a0ce676'
        },
        'exitAMM': {
            'direction': 'INCOMING',
            'description': 'Exits AMM pool',
            'method': '0x8e0e6d57'
        }
    },
    'L2_OPERATIONS': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets to L2',
            'method': '0xb6b55f25'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from L2',
            'method': '0x2e1a7d4d'
        },
        'transfer': {
            'direction': 'BOTH',
            'description': 'Transfers assets on L2',
            'method': '0xa9059cbb'
        },
        'forceWithdraw': {
            'direction': 'OUTGOING',
            'description': 'Forces withdrawal from L2',
            'method': '0x4f1eb3d8'
        }
    },
    'STAKING': {
        'stakeLRC': {
            'direction': 'OUTGOING',
            'description': 'Stakes LRC tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLRC': {
            'direction': 'INCOMING',
            'description': 'Unstakes LRC tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
LOOPRING_FUNCTIONS = {
    'V3': LOOPRING_V3_FUNCTIONS
}