"""STEPN Protocol Functions for all versions"""

STEPN_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startMove': {
            'direction': 'OUTGOING',
            'description': 'Starts move-to-earn session',
            'method': '0x1698ee82'
        },
        'endMove': {
            'direction': 'INCOMING',
            'description': 'Ends move-to-earn session',
            'method': '0x4ce38b5f'
        },
        'claimGST': {
            'direction': 'INCOMING',
            'description': 'Claims earned GST tokens',
            'method': '0x4e71d92d'
        },
        'levelUpShoe': {
            'direction': 'OUTGOING',
            'description': 'Upgrades NFT shoe',
            'method': '0x7535d246'
        }
    },
    'MARKETPLACE': {
        'listShoe': {
            'direction': 'OUTGOING',
            'description': 'Lists shoe NFT for sale',
            'method': '0x6c1aaf13'
        },
        'buyShoe': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed shoe',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels shoe listing',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on shoe',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakeGMT': {
            'direction': 'OUTGOING',
            'description': 'Stakes GMT tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGMT': {
            'direction': 'INCOMING',
            'description': 'Unstakes GMT tokens',
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
STEPN_FUNCTIONS = {
    'V1': STEPN_V1_FUNCTIONS
}