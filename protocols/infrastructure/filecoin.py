"""Filecoin Protocol Functions for all versions"""

FILECOIN_V1_FUNCTIONS = {
    'STORAGE': {
        'storeData': {
            'direction': 'OUTGOING',
            'description': 'Stores data on network',
            'method': '0x1698ee82'
        },
        'retrieveData': {
            'direction': 'INCOMING',
            'description': 'Retrieves stored data',
            'method': '0x69328dec'
        },
        'verifyStorage': {
            'direction': 'NEUTRAL',
            'description': 'Verifies data storage',
            'method': '0x7535d246'
        }
    },
    'MINING': {
        'pledgeCollateral': {
            'direction': 'OUTGOING',
            'description': 'Pledges mining collateral',
            'method': '0xa694fc3a'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws collateral',
            'method': '0x2e1a7d4d'
        },
        'submitProof': {
            'direction': 'OUTGOING',
            'description': 'Submits storage proof',
            'method': '0x9b3d47b4'
        },
        'claimReward': {
            'direction': 'INCOMING',
            'description': 'Claims mining reward',
            'method': '0x4e71d92d'
        }
    },
    'MARKET': {
        'createDeal': {
            'direction': 'OUTGOING',
            'description': 'Creates storage deal',
            'method': '0x1698ee82'
        },
        'fundDeal': {
            'direction': 'OUTGOING',
            'description': 'Funds storage deal',
            'method': '0x47e7ef24'
        },
        'activateDeal': {
            'direction': 'OUTGOING',
            'description': 'Activates storage deal',
            'method': '0x7535d246'
        },
        'terminateDeal': {
            'direction': 'OUTGOING',
            'description': 'Terminates storage deal',
            'method': '0x2e1a7d4d'
        }
    },
    'POWER': {
        'createMiner': {
            'direction': 'OUTGOING',
            'description': 'Creates storage miner',
            'method': '0x1698ee82'
        },
        'updatePower': {
            'direction': 'OUTGOING',
            'description': 'Updates storage power',
            'method': '0x7535d246'
        },
        'declareStorage': {
            'direction': 'OUTGOING',
            'description': 'Declares storage capacity',
            'method': '0x9b3d47b4'
        }
    }
}

# Combined functions for all versions
FILECOIN_FUNCTIONS = {
    'V1': FILECOIN_V1_FUNCTIONS
}