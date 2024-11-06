"""Pegaxy Protocol Functions for all versions"""

PEGAXY_V1_FUNCTIONS = {
    'RACING': {
        'startRace': {
            'direction': 'OUTGOING',
            'description': 'Starts racing event',
            'method': '0x1698ee82'
        },
        'claimVIS': {
            'direction': 'INCOMING',
            'description': 'Claims VIS rewards',
            'method': '0x4e71d92d'
        },
        'breedPega': {
            'direction': 'OUTGOING',
            'description': 'Breeds new Pega',
            'method': '0x8f38249c'
        },
        'rentPega': {
            'direction': 'BOTH',
            'description': 'Rents Pega to/from others',
            'method': '0x7c025200'
        }
    },
    'MARKETPLACE': {
        'listPega': {
            'direction': 'OUTGOING',
            'description': 'Lists Pega for sale',
            'method': '0x6c1aaf13'
        },
        'buyPega': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed Pega',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels Pega listing',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on Pega',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakePGX': {
            'direction': 'OUTGOING',
            'description': 'Stakes PGX tokens',
            'method': '0xa694fc3a'
        },
        'unstakePGX': {
            'direction': 'INCOMING',
            'description': 'Unstakes PGX tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
PEGAXY_FUNCTIONS = {
    'V1': PEGAXY_V1_FUNCTIONS
}