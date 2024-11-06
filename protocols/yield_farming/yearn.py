"""Yearn Protocol Functions for all versions"""

YEARN_V1_FUNCTIONS = {
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
        'earn': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0x4f1eb3d8'
        }
    },
    'STRATEGIES': {
        'migrate': {
            'direction': 'BOTH',
            'description': 'Migrates to new strategy',
            'method': '0x4ce38b5f'
        },
        'withdrawToVault': {
            'direction': 'INCOMING',
            'description': 'Withdraws to vault',
            'method': '0x69328dec'
        },
        'estimatedTotalAssets': {
            'direction': 'BOTH',
            'description': 'Gets strategy assets',
            'method': '0x7535d246'
        },
        'tend': {
            'direction': 'OUTGOING',
            'description': 'Performs strategy upkeep',
            'method': '0x2f4f5cc5'
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
        'queue': {
            'direction': 'OUTGOING',
            'description': 'Queues proposal',
            'method': '0xddf0b009'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

YEARN_V2_FUNCTIONS = {
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
        'migrate': {
            'direction': 'BOTH',
            'description': 'Migrates vault assets',
            'method': '0x4ce38b5f'
        }
    },
    'STRATEGIES': {
        'addStrategy': {
            'direction': 'OUTGOING',
            'description': 'Adds new strategy',
            'method': '0x1698ee82'
        },
        'removeStrategy': {
            'direction': 'OUTGOING',
            'description': 'Removes strategy',
            'method': '0x2e1a7d4d'
        },
        'updateStrategyDebtRatio': {
            'direction': 'OUTGOING',
            'description': 'Updates strategy allocation',
            'method': '0x7535d246'
        },
        'migrateStrategy': {
            'direction': 'BOTH',
            'description': 'Migrates strategy',
            'method': '0x4ce38b5f'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims vault rewards',
            'method': '0xe6f1daf2'
        },
        'gaugeDeposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into gauge',
            'method': '0x47e7ef24'
        },
        'gaugeWithdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from gauge',
            'method': '0x69328dec'
        }
    }
}

YEARN_V3_FUNCTIONS = {
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
        'migrate': {
            'direction': 'BOTH',
            'description': 'Migrates vault assets',
            'method': '0x4ce38b5f'
        }
    },
    'STRATEGIES': {
        'addStrategy': {
            'direction': 'OUTGOING',
            'description': 'Adds new strategy',
            'method': '0x1698ee82'
        },
        'removeStrategy': {
            'direction': 'OUTGOING',
            'description': 'Removes strategy',
            'method': '0x2e1a7d4d'
        },
        'updateStrategyDebtRatio': {
            'direction': 'OUTGOING',
            'description': 'Updates strategy allocation',
            'method': '0x7535d246'
        },
        'migrateStrategy': {
            'direction': 'BOTH',
            'description': 'Migrates strategy',
            'method': '0x4ce38b5f'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims vault rewards',
            'method': '0xe6f1daf2'
        },
        'gaugeDeposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into gauge',
            'method': '0x47e7ef24'
        },
        'gaugeWithdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from gauge',
            'method': '0x69328dec'
        }
    }
}

# Combined functions for all versions
YEARN_FUNCTIONS = {
    'V1': YEARN_V1_FUNCTIONS,
    'V2': YEARN_V2_FUNCTIONS,
    'V3': YEARN_V3_FUNCTIONS
}