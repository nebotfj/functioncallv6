"""Crypto Unicorns Protocol Functions for all versions"""

CRYPTO_UNICORNS_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'breedUnicorns': {
            'direction': 'OUTGOING',
            'description': 'Breeds new unicorn',
            'method': '0x8f38249c'
        },
        'startRace': {
            'direction': 'OUTGOING',
            'description': 'Starts unicorn race',
            'method': '0x1698ee82'
        },
        'claimRaceRewards': {
            'direction': 'INCOMING',
            'description': 'Claims race rewards',
            'method': '0x4e71d92d'
        },
        'upgradeUnicorn': {
            'direction': 'OUTGOING',
            'description': 'Upgrades unicorn stats',
            'method': '0x7535d246'
        }
    },
    'FARMING': {
        'plantSeeds': {
            'direction': 'OUTGOING',
            'description': 'Plants resource seeds',
            'method': '0x1698ee82'
        },
        'harvestCrops': {
            'direction': 'INCOMING',
            'description': 'Harvests grown crops',
            'method': '0x4641257d'
        },
        'feedUnicorns': {
            'direction': 'OUTGOING',
            'description': 'Feeds unicorns resources',
            'method': '0x7535d246'
        },
        'collectResources': {
            'direction': 'INCOMING',
            'description': 'Collects farm resources',
            'method': '0x4e71d92d'
        }
    },
    'MARKETPLACE': {
        'listUnicorn': {
            'direction': 'OUTGOING',
            'description': 'Lists unicorn for sale',
            'method': '0x6c1aaf13'
        },
        'buyUnicorn': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed unicorn',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels unicorn listing',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts offer on unicorn',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakeRBW': {
            'direction': 'OUTGOING',
            'description': 'Stakes RBW tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRBW': {
            'direction': 'INCOMING',
            'description': 'Unstakes RBW tokens',
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
CRYPTO_UNICORNS_FUNCTIONS = {
    'V1': CRYPTO_UNICORNS_V1_FUNCTIONS
}