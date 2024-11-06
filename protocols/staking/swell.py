"""Swell Protocol Functions for all versions"""

SWELL_V1_FUNCTIONS = {
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
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
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
        'exitValidator': {
            'direction': 'OUTGOING',
            'description': 'Exits validator from network',
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
SWELL_FUNCTIONS = {
    'V1': SWELL_V1_FUNCTIONS
}