"""Ember Sword Protocol Functions for all versions"""

EMBER_SWORD_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startQuest': {
            'direction': 'OUTGOING',
            'description': 'Starts new quest',
            'method': '0x1698ee82'
        },
        'completeQuest': {
            'direction': 'INCOMING',
            'description': 'Completes active quest',
            'method': '0x4ce38b5f'
        },
        'craftItem': {
            'direction': 'OUTGOING',
            'description': 'Crafts game item',
            'method': '0x7535d246'
        },
        'enhanceItem': {
            'direction': 'OUTGOING',
            'description': 'Enhances existing item',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims gameplay rewards',
            'method': '0x4e71d92d'
        }
    },
    'LAND': {
        'purchaseLand': {
            'direction': 'OUTGOING',
            'description': 'Purchases land plot',
            'method': '0x8f38249c'
        },
        'developLand': {
            'direction': 'OUTGOING',
            'description': 'Develops land plot',
            'method': '0x7535d246'
        },
        'collectResources': {
            'direction': 'INCOMING',
            'description': 'Collects land resources',
            'method': '0x4641257d'
        },
        'tradeLand': {
            'direction': 'BOTH',
            'description': 'Trades land plots',
            'method': '0xbc61394a'
        }
    },
    'MARKETPLACE': {
        'listItem': {
            'direction': 'OUTGOING',
            'description': 'Lists item for sale',
            'method': '0x6c1aaf13'
        },
        'buyItem': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed item',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels item listing',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on item',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
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
EMBER_SWORD_FUNCTIONS = {
    'V1': EMBER_SWORD_V1_FUNCTIONS
}