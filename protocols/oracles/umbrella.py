"""Umbrella Network Protocol Functions for all versions"""

UMBRELLA_V1_FUNCTIONS = {
    'ORACLE': {
        'submitBlock': {
            'direction': 'OUTGOING',
            'description': 'Submits oracle block',
            'method': '0x7535d246'
        },
        'validateBlock': {
            'direction': 'NEUTRAL',
            'description': 'Validates submitted block',
            'method': '0x9d2f32dd'
        },
        'getPrice': {
            'direction': 'NEUTRAL',
            'description': 'Gets price data',
            'method': '0x98f4b1b2'
        },
        'getPrices': {
            'direction': 'NEUTRAL',
            'description': 'Gets multiple prices',
            'method': '0x0a0e6b3b'
        }
    },
    'STAKING': {
        'stakeUMB': {
            'direction': 'OUTGOING',
            'description': 'Stakes UMB tokens',
            'method': '0xa694fc3a'
        },
        'unstakeUMB': {
            'direction': 'INCOMING',
            'description': 'Unstakes UMB tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'VALIDATOR': {
        'registerValidator': {
            'direction': 'OUTGOING',
            'description': 'Registers as validator',
            'method': '0x1698ee82'
        },
        'deregisterValidator': {
            'direction': 'OUTGOING',
            'description': 'Removes validator status',
            'method': '0x2e1a7d4d'
        },
        'submitReport': {
            'direction': 'OUTGOING',
            'description': 'Submits price report',
            'method': '0x9b3d47b4'
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
UMBRELLA_FUNCTIONS = {
    'V1': UMBRELLA_V1_FUNCTIONS
}