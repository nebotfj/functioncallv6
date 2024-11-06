"""Kwenta Protocol Functions for all versions"""

KWENTA_V2_FUNCTIONS = {
    'TRADING': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new trading position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes existing position',
            'method': '0x82a08fcd'
        },
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies position parameters',
            'method': '0x0c49ccbe'
        },
        'submitOrder': {
            'direction': 'OUTGOING',
            'description': 'Submits trading order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels pending order',
            'method': '0x2e1a7d4d'
        }
    },
    'STAKING': {
        'stakeKWENTA': {
            'direction': 'OUTGOING',
            'description': 'Stakes KWENTA tokens',
            'method': '0xa694fc3a'
        },
        'unstakeKWENTA': {
            'direction': 'INCOMING',
            'description': 'Unstakes KWENTA tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'vestRewards': {
            'direction': 'OUTGOING',
            'description': 'Vests earned rewards',
            'method': '0x1749e1e3'
        }
    },
    'REWARDS': {
        'claimTrading': {
            'direction': 'INCOMING',
            'description': 'Claims trading rewards',
            'method': '0x4e71d92d'
        },
        'claimStaking': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
KWENTA_FUNCTIONS = {
    'V2': KWENTA_V2_FUNCTIONS
}