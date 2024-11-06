"""Aztec Protocol Functions for all versions"""

AZTEC_V2_FUNCTIONS = {
    'SHIELD': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits public assets',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws to public',
            'method': '0x69328dec'
        },
        'transfer': {
            'direction': 'BOTH',
            'description': 'Transfers private notes',
            'method': '0x23b872dd'
        },
        'shield': {
            'direction': 'OUTGOING',
            'description': 'Shields public transaction',
            'method': '0x7535d246'
        }
    },
    'DEFI_BRIDGE': {
        'bridgeDeposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into DeFi bridge',
            'method': '0x47e7ef24'
        },
        'bridgeWithdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from DeFi bridge',
            'method': '0x69328dec'
        },
        'bridgeInteraction': {
            'direction': 'BOTH',
            'description': 'Interacts with DeFi protocol',
            'method': '0x4ce38b5f'
        }
    },
    'PROOFS': {
        'generateProof': {
            'direction': 'NEUTRAL',
            'description': 'Generates zero-knowledge proof',
            'method': '0x9b3d47b4'
        },
        'verifyProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies zero-knowledge proof',
            'method': '0x7535d246'
        },
        'processProof': {
            'direction': 'OUTGOING',
            'description': 'Processes verified proof',
            'method': '0x4ce38b5f'
        }
    },
    'ROLLUP': {
        'createProof': {
            'direction': 'OUTGOING',
            'description': 'Creates rollup proof',
            'method': '0x1698ee82'
        },
        'verifyRollup': {
            'direction': 'NEUTRAL',
            'description': 'Verifies rollup proof',
            'method': '0x7535d246'
        },
        'processRollup': {
            'direction': 'OUTGOING',
            'description': 'Processes rollup batch',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
AZTEC_FUNCTIONS = {
    'V2': AZTEC_V2_FUNCTIONS
}