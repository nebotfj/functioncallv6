"""DeFi Kingdoms Protocol Functions for all versions"""

DEFI_KINGDOMS_V1_FUNCTIONS = {
    'HEROES': {
        'summonHero': {
            'direction': 'OUTGOING',
            'description': 'Summons new hero',
            'method': '0x8f38249c'
        },
        'levelUpHero': {
            'direction': 'OUTGOING',
            'description': 'Increases hero level',
            'method': '0x7535d246'
        },
        'startQuest': {
            'direction': 'OUTGOING',
            'description': 'Starts hero quest',
            'method': '0x1698ee82'
        },
        'completeQuest': {
            'direction': 'INCOMING',
            'description': 'Completes hero quest',
            'method': '0x4ce38b5f'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims quest rewards',
            'method': '0x4e71d92d'
        }
    },
    'GARDENS': {
        'plantSeeds': {
            'direction': 'OUTGOING',
            'description': 'Plants seeds in garden',
            'method': '0x1698ee82'
        },
        'harvestPlants': {
            'direction': 'INCOMING',
            'description': 'Harvests grown plants',
            'method': '0x4641257d'
        },
        'waterPlants': {
            'direction': 'OUTGOING',
            'description': 'Waters garden plants',
            'method': '0x7535d246'
        },
        'collectRewards': {
            'direction': 'INCOMING',
            'description': 'Claims garden rewards',
            'method': '0x4e71d92d'
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
            'description': 'Rents hero temporarily',
            'method': '0x7c025200'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels hero listing',
            'method': '0x2e1a7d4d'
        }
    },
    'MEDITATION': {
        'startMeditation': {
            'direction': 'OUTGOING',
            'description': 'Starts hero meditation',
            'method': '0x1698ee82'
        },
        'completeMeditation': {
            'direction': 'INCOMING',
            'description': 'Completes meditation',
            'method': '0x4ce38b5f'
        },
        'claimMeditationRewards': {
            'direction': 'INCOMING',
            'description': 'Claims meditation rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
DEFI_KINGDOMS_FUNCTIONS = {
    'V1': DEFI_KINGDOMS_V1_FUNCTIONS
}