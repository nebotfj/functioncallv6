"""Splinterlands Protocol Functions for all versions"""

SPLINTERLANDS_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startBattle': {
            'direction': 'OUTGOING',
            'description': 'Starts card battle',
            'method': '0x1698ee82'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims battle rewards',
            'method': '0x4e71d92d'
        },
        'purchaseCards': {
            'direction': 'OUTGOING',
            'description': 'Purchases card packs',
            'method': '0x94b576de'
        },
        'combineCards': {
            'direction': 'OUTGOING',
            'description': 'Combines cards for upgrade',
            'method': '0x7535d246'
        }
    },
    'MARKETPLACE': {
        'listCard': {
            'direction': 'OUTGOING',
            'description': 'Lists card for sale',
            'method': '0x6c1aaf13'
        },
        'buyCard': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed card',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels card listing',
            'method': '0x2e1a7d4d'
        },
        'rentCard': {
            'direction': 'BOTH',
            'description': 'Rents card to/from others',
            'method': '0x7c025200'
        }
    },
    'STAKING': {
        'stakeSPS': {
            'direction': 'OUTGOING',
            'description': 'Stakes SPS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeSPS': {
            'direction': 'INCOMING',
            'description': 'Unstakes SPS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
SPLINTERLANDS_FUNCTIONS = {
    'V1': SPLINTERLANDS_V1_FUNCTIONS
}