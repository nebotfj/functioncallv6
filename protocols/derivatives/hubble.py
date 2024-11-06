"""Hubble Exchange Protocol Functions for all versions"""

HUBBLE_V1_FUNCTIONS = {
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
        'addMargin': {
            'direction': 'OUTGOING',
            'description': 'Adds margin to position',
            'method': '0x47e7ef24'
        },
        'removeMargin': {
            'direction': 'INCOMING',
            'description': 'Removes margin from position',
            'method': '0x69328dec'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        }
    },
    'CLEARING': {
        'settlePosition': {
            'direction': 'BOTH',
            'description': 'Settles trading position',
            'method': '0x4ce38b5f'
        },
        'claimInsurance': {
            'direction': 'INCOMING',
            'description': 'Claims insurance payout',
            'method': '0x4e71d92d'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws collateral',
            'method': '0x69328dec'
        }
    },
    'STAKING': {
        'stakeHBL': {
            'direction': 'OUTGOING',
            'description': 'Stakes HBL tokens',
            'method': '0xa694fc3a'
        },
        'unstakeHBL': {
            'direction': 'INCOMING',
            'description': 'Unstakes HBL tokens',
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
HUBBLE_FUNCTIONS = {
    'V1': HUBBLE_V1_FUNCTIONS
}