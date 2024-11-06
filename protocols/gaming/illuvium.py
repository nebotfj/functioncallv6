"""Illuvium Protocol Functions for all versions"""

ILLUVIUM_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'captureIlluvial': {
            'direction': 'OUTGOING',
            'description': 'Captures wild Illuvial',
            'method': '0x8f38249c'
        },
        'fightBattle': {
            'direction': 'BOTH',
            'description': 'Participates in battle',
            'method': '0x7c025200'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims gameplay rewards',
            'method': '0x4e71d92d'
        },
        'upgradeIlluvial': {
            'direction': 'OUTGOING',
            'description': 'Upgrades Illuvial stats',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stakeILV': {
            'direction': 'OUTGOING',
            'description': 'Stakes ILV tokens',
            'method': '0xa694fc3a'
        },
        'unstakeILV': {
            'direction': 'INCOMING',
            'description': 'Unstakes ILV tokens',
            'method': '0x2e1a7d4d'
        },
        'claimYield': {
            'direction': 'INCOMING',
            'description': 'Claims staking yield',
            'method': '0xe6f1daf2'
        },
        'lockStake': {
            'direction': 'OUTGOING',
            'description': 'Locks staked tokens',
            'method': '0x3d18b912'
        }
    },
    'LAND': {
        'purchaseLand': {
            'direction': 'OUTGOING',
            'description': 'Purchases land plot',
            'method': '0x8f38249c'
        },
        'buildOnLand': {
            'direction': 'OUTGOING',
            'description': 'Constructs on land',
            'method': '0x7535d246'
        },
        'harvestResources': {
            'direction': 'INCOMING',
            'description': 'Harvests land resources',
            'method': '0x4641257d'
        },
        'tradeLand': {
            'direction': 'BOTH',
            'description': 'Trades land plots',
            'method': '0xbc61394a'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

ILLUVIUM_V2_FUNCTIONS = {
    'GAMEPLAY': {
        'startQuest': {
            'direction': 'OUTGOING',
            'description': 'Initiates new quest',
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
        'fightBattle': {
            'direction': 'BOTH',
            'description': 'Participates in battle',
            'method': '0x7c025200'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims gameplay rewards',
            'method': '0x4e71d92d'
        }
    },
    'LAND': {
        'buildOnLand': {
            'direction': 'OUTGOING',
            'description': 'Constructs on land',
            'method': '0x7535d246'
        },
        'harvestResources': {
            'direction': 'INCOMING',
            'description': 'Harvests land resources',
            'method': '0x4641257d'
        },
        'upgradeLand': {
            'direction': 'OUTGOING',
            'description': 'Upgrades land plot',
            'method': '0x7535d246'
        },
        'tradeLand': {
            'direction': 'BOTH',
            'description': 'Trades land plots',
            'method': '0xbc61394a'
        }
    },
    'STAKING': {
        'stakeILV': {
            'direction': 'OUTGOING',
            'description': 'Stakes ILV tokens',
            'method': '0xa694fc3a'
        },
        'unstakeILV': {
            'direction': 'INCOMING',
            'description': 'Unstakes ILV tokens',
            'method': '0x2e1a7d4d'
        },
        'claimYield': {
            'direction': 'INCOMING',
            'description': 'Claims staking yield',
            'method': '0xe6f1daf2'
        },
        'lockStake': {
            'direction': 'OUTGOING',
            'description': 'Locks staked tokens',
            'method': '0x3d18b912'
        }
    }
}

# Combined functions for all versions
ILLUVIUM_FUNCTIONS = {
    'V1': ILLUVIUM_V1_FUNCTIONS,
    'V2': ILLUVIUM_V2_FUNCTIONS
}