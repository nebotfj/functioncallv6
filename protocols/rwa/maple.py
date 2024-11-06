"""Maple Finance Protocol Functions for all versions"""

MAPLE_V2_FUNCTIONS = {
    'LENDING': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates lending pool',
            'method': '0x1698ee82'
        },
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from pool',
            'method': '0x69328dec'
        },
        'requestLoan': {
            'direction': 'OUTGOING',
            'description': 'Requests pool loan',
            'method': '0x7535d246'
        },
        'approveLoan': {
            'direction': 'OUTGOING',
            'description': 'Approves loan request',
            'method': '0x4ce38b5f'
        },
        'drawdownLoan': {
            'direction': 'INCOMING',
            'description': 'Draws down approved loan',
            'method': '0x9dc29fac'
        },
        'repayLoan': {
            'direction': 'OUTGOING',
            'description': 'Repays active loan',
            'method': '0x573ade81'
        }
    },
    'STAKING': {
        'stakeMaple': {
            'direction': 'OUTGOING',
            'description': 'Stakes MPL tokens',
            'method': '0xa694fc3a'
        },
        'unstakeMaple': {
            'direction': 'INCOMING',
            'description': 'Unstakes MPL tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'POOL_DELEGATE': {
        'registerDelegate': {
            'direction': 'OUTGOING',
            'description': 'Registers pool delegate',
            'method': '0x1698ee82'
        },
        'setDelegateTerms': {
            'direction': 'OUTGOING',
            'description': 'Sets delegate terms',
            'method': '0x7535d246'
        },
        'removeDelegate': {
            'direction': 'OUTGOING',
            'description': 'Removes pool delegate',
            'method': '0x2e1a7d4d'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
MAPLE_FUNCTIONS = {
    'V2': MAPLE_V2_FUNCTIONS
}