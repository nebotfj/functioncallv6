"""Thetan Arena Protocol Functions for all versions"""

THETAN_ARENA_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startBattle': {
            'direction': 'OUTGOING',
            'description': 'Starts battle match',
            'method': '0x1698ee82'
        },
        'endBattle': {
            'direction': 'INCOMING',
            'description': 'Ends battle match',
            'method': '0x4ce38b5f'
        },
        'claimTHC': {
            'direction': 'INCOMING',
            'description': 'Claims earned THC tokens',
            'method': '0x4e71d92d'
        },
        'upgradeHero': {
            'direction': 'OUTGOING',
            'description': 'Upgrades hero NFT',
            'method': '0x7535d246'
        }
    },
    'MARKETPLACE': {
        'listHero': {
            'direction': 'OUTGOING',
            'description': 'Lists hero for sale',
            'method': '0x6c1aaf13'
        },
        'buyHero': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed hero',
            'method': '0x94b576de'
        },
        'rentHero': {
            'direction': 'BOTH',
            'description': 'Rents hero to/from others',
            'method': '0x7c025200'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels hero listing',
            'method': '0x2e1a7d4d'
        }
    },
    'STAKING': {
        'stakeTHG': {
            'direction': 'OUTGOING',
            'description': 'Stakes THG tokens',
            'method': '0xa694fc3a'
        },
        'unstakeTHG': {
            'direction': 'INCOMING',
            'description': 'Unstakes THG tokens',
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
THETAN_ARENA_FUNCTIONS = {
    'V1': THETAN_ARENA_V1_FUNCTIONS
}