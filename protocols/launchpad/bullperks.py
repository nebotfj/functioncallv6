"""BullPerks Protocol Functions for all versions"""

BULLPERKS_V1_FUNCTIONS = {
    'DEALS': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in token sale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims purchased tokens',
            'method': '0x4e71d92d'
        },
        'refund': {
            'direction': 'INCOMING',
            'description': 'Claims refund for failed sale',
            'method': '0x590e1ae3'
        }
    },
    'STAKING': {
        'stakeBLP': {
            'direction': 'OUTGOING',
            'description': 'Stakes BLP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeBLP': {
            'direction': 'INCOMING',
            'description': 'Unstakes BLP tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'GOVERNANCE': {
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
BULLPERKS_FUNCTIONS = {
    'V1': BULLPERKS_V1_FUNCTIONS
}