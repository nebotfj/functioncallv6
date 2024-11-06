"""GameFi Protocol Functions for all versions"""

GAMEFI_V1_FUNCTIONS = {
    'IGO': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in game token sale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims purchased game tokens',
            'method': '0x4e71d92d'
        },
        'refund': {
            'direction': 'INCOMING',
            'description': 'Claims refund for failed IGO',
            'method': '0x590e1ae3'
        }
    },
    'STAKING': {
        'stakeGAFI': {
            'direction': 'OUTGOING',
            'description': 'Stakes GAFI tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGAFI': {
            'direction': 'INCOMING',
            'description': 'Unstakes GAFI tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'POOLS': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new IGO pool',
            'method': '0x1698ee82'
        },
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Joins existing IGO pool',
            'method': '0x9b3d47b4'
        },
        'leavePool': {
            'direction': 'INCOMING',
            'description': 'Exits IGO pool',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
GAMEFI_FUNCTIONS = {
    'V1': GAMEFI_V1_FUNCTIONS
}