"""Gains Network Protocol Functions for all versions"""

GAINS_V6_FUNCTIONS = {
    'TRADING': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new trading position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes entire position',
            'method': '0x82a08fcd'
        },
        'addToPosition': {
            'direction': 'OUTGOING',
            'description': 'Increases position size',
            'method': '0x219f5d17'
        },
        'partialClosePosition': {
            'direction': 'INCOMING',
            'description': 'Closes portion of position',
            'method': '0x0c49ccbe'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        }
    },
    'STAKING': {
        'stakeGNS': {
            'direction': 'OUTGOING',
            'description': 'Stakes GNS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGNS': {
            'direction': 'INCOMING',
            'description': 'Unstakes GNS tokens',
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
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets to vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'rebalanceVault': {
            'direction': 'BOTH',
            'description': 'Rebalances vault assets',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
GAINS_FUNCTIONS = {
    'V6': GAINS_V6_FUNCTIONS
}