"""Monero Bridge Protocol Functions for all versions"""

MONERO_BRIDGE_V1_FUNCTIONS = {
    'BRIDGE': {
        'bridgeToMonero': {
            'direction': 'OUTGOING',
            'description': 'Bridges to Monero chain',
            'method': '0x8b9e4f93'
        },
        'bridgeFromMonero': {
            'direction': 'INCOMING',
            'description': 'Bridges from Monero chain',
            'method': '0x4ce38b5f'
        },
        'generateProof': {
            'direction': 'NEUTRAL',
            'description': 'Generates bridge proof',
            'method': '0x9b3d47b4'
        },
        'verifyProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies bridge proof',
            'method': '0x7535d246'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds bridge liquidity',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes bridge liquidity',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims bridge fees',
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
MONERO_BRIDGE_FUNCTIONS = {
    'V1': MONERO_BRIDGE_V1_FUNCTIONS
}