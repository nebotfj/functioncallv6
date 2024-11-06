"""Railway Protocol Functions for all versions"""

RAILWAY_V1_FUNCTIONS = {
    'PRIVACY': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates privacy pool',
            'method': '0x1698ee82'
        },
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
        'mix': {
            'direction': 'BOTH',
            'description': 'Mixes pool assets',
            'method': '0x4ce38b5f'
        }
    },
    'RELAYER': {
        'submitProof': {
            'direction': 'OUTGOING',
            'description': 'Submits zero-knowledge proof',
            'method': '0x9b3d47b4'
        },
        'relayTransaction': {
            'direction': 'OUTGOING',
            'description': 'Relays private transaction',
            'method': '0x7535d246'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims relayer fees',
            'method': '0xd294f093'
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
RAILWAY_FUNCTIONS = {
    'V1': RAILWAY_V1_FUNCTIONS
}