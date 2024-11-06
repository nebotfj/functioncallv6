"""Polynomial Protocol Functions for all versions"""

POLYNOMIAL_V1_FUNCTIONS = {
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
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        }
    },
    'COLLATERAL': {
        'addCollateral': {
            'direction': 'OUTGOING',
            'description': 'Adds collateral to position',
            'method': '0x47e7ef24'
        },
        'removeCollateral': {
            'direction': 'INCOMING',
            'description': 'Removes collateral from position',
            'method': '0x69328dec'
        },
        'claimLiquidation': {
            'direction': 'INCOMING',
            'description': 'Claims liquidation rewards',
            'method': '0x4e71d92d'
        }
    },
    'STAKING': {
        'stakePOLY': {
            'direction': 'OUTGOING',
            'description': 'Stakes POLY tokens',
            'method': '0xa694fc3a'
        },
        'unstakePOLY': {
            'direction': 'INCOMING',
            'description': 'Unstakes POLY tokens',
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
POLYNOMIAL_FUNCTIONS = {
    'V1': POLYNOMIAL_V1_FUNCTIONS
}