"""Big Time Protocol Functions for all versions"""

BIGTIME_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startMission': {
            'direction': 'OUTGOING',
            'description': 'Starts new mission',
            'method': '0x1698ee82'
        },
        'completeMission': {
            'direction': 'INCOMING',
            'description': 'Completes active mission',
            'method': '0x4ce38b5f'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims mission rewards',
            'method': '0x4e71d92d'
        },
        'upgradeGear': {
            'direction': 'OUTGOING',
            'description': 'Upgrades equipment',
            'method': '0x7535d246'
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
    'CRAFTING': {
        'craftItem': {
            'direction': 'OUTGOING',
            'description': 'Crafts new item',
            'method': '0x1698ee82'
        },
        'enhanceItem': {
            'direction': 'OUTGOING',
            'description': 'Enhances existing item',
            'method': '0x7535d246'
        },
        'salvageItem': {
            'direction': 'BOTH',
            'description': 'Salvages item for materials',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
BIGTIME_FUNCTIONS = {
    'V1': BIGTIME_V1_FUNCTIONS
}