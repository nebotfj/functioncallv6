"""Pocket Network Protocol Functions for all versions"""

POCKET_V1_FUNCTIONS = {
    'NODES': {
        'stakeNode': {
            'direction': 'OUTGOING',
            'description': 'Stakes POKT for node',
            'method': '0xa694fc3a'
        },
        'unstakeNode': {
            'direction': 'INCOMING',
            'description': 'Unstakes node POKT',
            'method': '0x2e1a7d4d'
        },
        'unjailNode': {
            'direction': 'OUTGOING',
            'description': 'Unjails slashed node',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims node rewards',
            'method': '0x4e71d92d'
        }
    },
    'APPS': {
        'stakeApp': {
            'direction': 'OUTGOING',
            'description': 'Stakes app POKT',
            'method': '0xa694fc3a'
        },
        'unstakeApp': {
            'direction': 'INCOMING',
            'description': 'Unstakes app POKT',
            'method': '0x2e1a7d4d'
        },
        'createApp': {
            'direction': 'OUTGOING',
            'description': 'Creates new application',
            'method': '0x1698ee82'
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
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims governance rewards',
            'method': '0x4e71d92d'
        }
    },
    'RELAY': {
        'submitRelay': {
            'direction': 'OUTGOING',
            'description': 'Submits relay proof',
            'method': '0x9b3d47b4'
        },
        'challengeRelay': {
            'direction': 'OUTGOING',
            'description': 'Challenges invalid relay',
            'method': '0x2f4f5cc5'
        },
        'claimRelayRewards': {
            'direction': 'INCOMING',
            'description': 'Claims relay rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
POCKET_FUNCTIONS = {
    'V1': POCKET_V1_FUNCTIONS
}