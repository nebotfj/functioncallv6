"""Gods Unchained Protocol Functions for all versions"""

GODS_UNCHAINED_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startMatch': {
            'direction': 'OUTGOING',
            'description': 'Starts new match',
            'method': '0x1698ee82'
        },
        'endMatch': {
            'direction': 'INCOMING',
            'description': 'Ends current match',
            'method': '0x4ce38b5f'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims match rewards',
            'method': '0x4e71d92d'
        },
        'forgeCard': {
            'direction': 'OUTGOING',
            'description': 'Forges new card',
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
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on card',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakeGODS': {
            'direction': 'OUTGOING',
            'description': 'Stakes GODS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGODS': {
            'direction': 'INCOMING',
            'description': 'Unstakes GODS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimYield': {
            'direction': 'INCOMING',
            'description': 'Claims staking yield',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'FUSION': {
        'fuseCards': {
            'direction': 'OUTGOING',
            'description': 'Fuses multiple cards',
            'method': '0x7535d246'
        },
        'splitCard': {
            'direction': 'INCOMING',
            'description': 'Splits fused card',
            'method': '0x4ce38b5f'
        },
        'upgradeCard': {
            'direction': 'OUTGOING',
            'description': 'Upgrades card quality',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
GODS_UNCHAINED_FUNCTIONS = {
    'V1': GODS_UNCHAINED_V1_FUNCTIONS
}