"""Concentrator Protocol Functions for all versions"""

CONCENTRATOR_V1_FUNCTIONS = {
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Harvests vault rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds vault rewards',
            'method': '0xf69e2046'
        }
    },
    'STRATEGY': {
        'setStrategy': {
            'direction': 'OUTGOING',
            'description': 'Sets vault strategy',
            'method': '0x7535d246'
        },
        'migrateStrategy': {
            'direction': 'BOTH',
            'description': 'Migrates to new strategy',
            'method': '0x4ce38b5f'
        },
        'updateStrategyDebtRatio': {
            'direction': 'OUTGOING',
            'description': 'Updates strategy debt ratio',
            'method': '0x7535d246'
        }
    },
    'REWARDS': {
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims vault rewards',
            'method': '0x3d18b912'
        },
        'notifyRewardAmount': {
            'direction': 'OUTGOING',
            'description': 'Updates reward amount',
            'method': '0x3c6b16ab'
        },
        'addReward': {
            'direction': 'OUTGOING',
            'description': 'Adds new reward token',
            'method': '0x3a088cd2'
        }
    }
}

# Combined functions for all versions
CONCENTRATOR_FUNCTIONS = {
    'V1': CONCENTRATOR_V1_FUNCTIONS
}