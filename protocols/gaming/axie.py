"""Axie Infinity Protocol Functions for all versions"""

AXIE_V2_FUNCTIONS = {
    'GAMEPLAY': {
        'startGame': {
            'direction': 'OUTGOING',
            'description': 'Starts new game session',
            'method': '0x1698ee82'
        },
        'endGame': {
            'direction': 'INCOMING',
            'description': 'Ends game session',
            'method': '0x2e1a7d4d'
        },
        'claimSLP': {
            'direction': 'INCOMING',
            'description': 'Claims earned SLP tokens',
            'method': '0x4e71d92d'
        },
        'breedAxies': {
            'direction': 'OUTGOING',
            'description': 'Breeds new Axie',
            'method': '0x8f38249c'
        }
    },
    'MARKETPLACE': {
        'listAxie': {
            'direction': 'OUTGOING',
            'description': 'Lists Axie for sale',
            'method': '0x6c1aaf13'
        },
        'buyAxie': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed Axie',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels Axie listing',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on Axie',
            'method': '0xbc61394a'
        }
    },
    'LAND': {
        'buyLand': {
            'direction': 'OUTGOING',
            'description': 'Purchases Lunacia land',
            'method': '0x8f38249c'
        },
        'sellLand': {
            'direction': 'INCOMING',
            'description': 'Sells Lunacia land',
            'method': '0x454a2ab3'
        },
        'stakeLand': {
            'direction': 'OUTGOING',
            'description': 'Stakes land plot',
            'method': '0xa694fc3a'
        },
        'harvestFromLand': {
            'direction': 'INCOMING',
            'description': 'Harvests land resources',
            'method': '0x4641257d'
        }
    },
    'STAKING': {
        'stakeAXS': {
            'direction': 'OUTGOING',
            'description': 'Stakes AXS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeAXS': {
            'direction': 'INCOMING',
            'description': 'Unstakes AXS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'restakeRewards': {
            'direction': 'OUTGOING',
            'description': 'Restakes earned rewards',
            'method': '0x7b24a5fd'
        }
    }
}

# Combined functions for all versions
AXIE_FUNCTIONS = {
    'V2': AXIE_V2_FUNCTIONS
}