"""Redacted Protocol Functions for all versions"""

REDACTED_V1_FUNCTIONS = {
    'STAKING': {
        'stakeBTRFLY': {
            'direction': 'OUTGOING',
            'description': 'Stakes BTRFLY tokens',
            'method': '0xa694fc3a'
        },
        'unstakeBTRFLY': {
            'direction': 'INCOMING',
            'description': 'Unstakes BTRFLY tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        }
    },
    'HIDDEN_HAND': {
        'claimBribes': {
            'direction': 'INCOMING',
            'description': 'Claims bribe rewards',
            'method': '0x4e71d92d'
        },
        'voteBribes': {
            'direction': 'OUTGOING',
            'description': 'Votes for bribe allocation',
            'method': '0x15373e3d'
        },
        'proposeBribe': {
            'direction': 'OUTGOING',
            'description': 'Creates new bribe',
            'method': '0xda95691a'
        }
    },
    'TREASURY': {
        'proposePurchase': {
            'direction': 'OUTGOING',
            'description': 'Proposes asset purchase',
            'method': '0xda95691a'
        },
        'executePurchase': {
            'direction': 'OUTGOING',
            'description': 'Executes asset purchase',
            'method': '0xfe0d94c1'
        },
        'harvestYield': {
            'direction': 'INCOMING',
            'description': 'Harvests treasury yield',
            'method': '0x4641257d'
        }
    }
}

# Combined functions for all versions
REDACTED_FUNCTIONS = {
    'V1': REDACTED_V1_FUNCTIONS
}