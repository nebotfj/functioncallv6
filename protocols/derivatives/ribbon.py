"""Ribbon Finance Protocol Functions for all versions"""

RIBBON_V2_FUNCTIONS = {
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'initiateWithdraw': {
            'direction': 'OUTGOING',
            'description': 'Starts withdrawal process',
            'method': '0x0c49ccbe'
        },
        'completeWithdraw': {
            'direction': 'INCOMING',
            'description': 'Completes withdrawal process',
            'method': '0x4ce38b5f'
        }
    },
    'OPTIONS': {
        'purchaseOption': {
            'direction': 'OUTGOING',
            'description': 'Buys option contract',
            'method': '0x8f38249c'
        },
        'exerciseOption': {
            'direction': 'BOTH',
            'description': 'Exercises option contract',
            'method': '0x7c025200'
        },
        'settleOption': {
            'direction': 'INCOMING',
            'description': 'Settles expired option',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stakeRBN': {
            'direction': 'OUTGOING',
            'description': 'Stakes RBN tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRBN': {
            'direction': 'INCOMING',
            'description': 'Unstakes RBN tokens',
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
RIBBON_FUNCTIONS = {
    'V2': RIBBON_V2_FUNCTIONS
}