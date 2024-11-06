"""EigenLayer Protocol Functions for all versions"""

EIGENLAYER_V1_FUNCTIONS = {
    'STAKING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets for restaking',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws restaked assets',
            'method': '0x69328dec'
        },
        'restake': {
            'direction': 'OUTGOING',
            'description': 'Restakes existing deposits',
            'method': '0x7b24a5fd'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes from protocol',
            'method': '0x2e1a7d4d'
        }
    },
    'OPERATOR': {
        'registerOperator': {
            'direction': 'OUTGOING',
            'description': 'Registers as operator',
            'method': '0x1698ee82'
        },
        'updateOperator': {
            'direction': 'OUTGOING',
            'description': 'Updates operator metadata',
            'method': '0x7535d246'
        },
        'deregisterOperator': {
            'direction': 'OUTGOING',
            'description': 'Removes operator status',
            'method': '0x2e1a7d4d'
        }
    },
    'POD': {
        'createPod': {
            'direction': 'OUTGOING',
            'description': 'Creates new staking pod',
            'method': '0x1698ee82'
        },
        'joinPod': {
            'direction': 'OUTGOING',
            'description': 'Joins existing pod',
            'method': '0x9b3d47b4'
        },
        'leavePod': {
            'direction': 'OUTGOING',
            'description': 'Exits from pod',
            'method': '0x2e1a7d4d'
        }
    },
    'DELEGATION': {
        'delegateToOperator': {
            'direction': 'OUTGOING',
            'description': 'Delegates to operator',
            'method': '0x5c19a95c'
        },
        'undelegateFromOperator': {
            'direction': 'OUTGOING',
            'description': 'Removes delegation',
            'method': '0x2e1a7d4d'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'distributeRewards': {
            'direction': 'OUTGOING',
            'description': 'Distributes operator rewards',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
EIGENLAYER_FUNCTIONS = {
    'V1': EIGENLAYER_V1_FUNCTIONS
}