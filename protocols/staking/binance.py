"""Binance Staking Protocol Functions for all versions"""

BINANCE_V1_FUNCTIONS = {
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
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'redelegateStake': {
            'direction': 'BOTH',
            'description': 'Redelegates stake to new validator',
            'method': '0x4ce38b5f'
        },
        'lockStake': {
            'direction': 'OUTGOING',
            'description': 'Locks stake for extended period',
            'method': '0x3d18b912'
        }
    },
    'VALIDATOR': {
        'registerValidator': {
            'direction': 'OUTGOING',
            'description': 'Registers as validator',
            'method': '0x1698ee82'
        },
        'updateValidator': {
            'direction': 'OUTGOING',
            'description': 'Updates validator info',
            'method': '0x7535d246'
        },
        'unjailValidator': {
            'direction': 'OUTGOING',
            'description': 'Removes validator from jail',
            'method': '0x2f4f5cc5'
        }
    },
    'DELEGATION': {
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates to validator',
            'method': '0x5c19a95c'
        },
        'undelegate': {
            'direction': 'OUTGOING',
            'description': 'Removes delegation',
            'method': '0x2e1a7d4d'
        },
        'redelegate': {
            'direction': 'BOTH',
            'description': 'Changes delegation',
            'method': '0x4ce38b5f'
        }
    },
    'GOVERNANCE': {
        'submitProposal': {
            'direction': 'OUTGOING',
            'description': 'Submits governance proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits for proposal',
            'method': '0x47e7ef24'
        }
    }
}

# Combined functions for all versions
BINANCE_FUNCTIONS = {
    'V1': BINANCE_V1_FUNCTIONS
}