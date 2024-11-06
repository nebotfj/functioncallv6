"""Tornado Cash Protocol Functions for all versions"""

TORNADO_V1_FUNCTIONS = {
    'PRIVACY': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into privacy pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from privacy pool',
            'method': '0x69328dec'
        },
        'generateNote': {
            'direction': 'NEUTRAL',
            'description': 'Generates commitment note',
            'method': '0x9b3d47b4'
        },
        'verifyNote': {
            'direction': 'NEUTRAL',
            'description': 'Verifies commitment note',
            'method': '0x7535d246'
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
    },
    'MINING': {
        'mine': {
            'direction': 'OUTGOING',
            'description': 'Mines anonymity points',
            'method': '0x1698ee82'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes TORN tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes TORN tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims mining rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
TORNADO_FUNCTIONS = {
    'V1': TORNADO_V1_FUNCTIONS
}