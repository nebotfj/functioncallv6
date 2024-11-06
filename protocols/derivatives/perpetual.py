"""Perpetual Protocol Functions for all versions"""

PERP_V2_FUNCTIONS = {
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
        'addMargin': {
            'direction': 'OUTGOING',
            'description': 'Adds margin to position',
            'method': '0x47e7ef24'
        },
        'removeMargin': {
            'direction': 'INCOMING',
            'description': 'Removes margin from position',
            'method': '0x69328dec'
        }
    },
    'STAKING': {
        'stakePERP': {
            'direction': 'OUTGOING',
            'description': 'Stakes PERP tokens',
            'method': '0xa694fc3a'
        },
        'unstakePERP': {
            'direction': 'INCOMING',
            'description': 'Unstakes PERP tokens',
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
    'INSURANCE': {
        'depositInsurance': {
            'direction': 'OUTGOING',
            'description': 'Deposits to insurance fund',
            'method': '0x47e7ef24'
        },
        'withdrawInsurance': {
            'direction': 'INCOMING',
            'description': 'Withdraws from insurance fund',
            'method': '0x69328dec'
        },
        'claimInsurance': {
            'direction': 'INCOMING',
            'description': 'Claims insurance payout',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
PERP_FUNCTIONS = {
    'V2': PERP_V2_FUNCTIONS
}