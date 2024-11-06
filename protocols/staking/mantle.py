"""Mantle LSP Protocol Functions for all versions"""

MANTLE_V1_FUNCTIONS = {
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes MNT tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes MNT tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'restake': {
            'direction': 'OUTGOING',
            'description': 'Restakes earned rewards',
            'method': '0x7b24a5fd'
        },
        'withdrawRewards': {
            'direction': 'INCOMING',
            'description': 'Withdraws staking rewards',
            'method': '0x69328dec'
        }
    },
    'DELEGATION': {
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates to validator',
            'method': '0x5c19a95c'
        },
        'undelegate': {
            'direction': 'INCOMING',
            'description': 'Undelegates from validator',
            'method': '0x2e1a7d4d'
        },
        'redelegate': {
            'direction': 'BOTH',
            'description': 'Redelegates to new validator',
            'method': '0x4ce38b5f'
        }
    },
    'VALIDATOR': {
        'registerValidator': {
            'direction': 'OUTGOING',
            'description': 'Registers new validator',
            'method': '0x1698ee82'
        },
        'updateValidator': {
            'direction': 'OUTGOING',
            'description': 'Updates validator info',
            'method': '0x7535d246'
        },
        'deactivateValidator': {
            'direction': 'OUTGOING',
            'description': 'Deactivates validator',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
MANTLE_FUNCTIONS = {
    'V1': MANTLE_V1_FUNCTIONS
}