"""Arweave Protocol Functions for all versions"""

ARWEAVE_V1_FUNCTIONS = {
    'STORAGE': {
        'uploadData': {
            'direction': 'OUTGOING',
            'description': 'Uploads data to network',
            'method': '0x1698ee82'
        },
        'downloadData': {
            'direction': 'INCOMING',
            'description': 'Downloads stored data',
            'method': '0x69328dec'
        },
        'createBundle': {
            'direction': 'OUTGOING',
            'description': 'Creates data bundle',
            'method': '0x7535d246'
        },
        'mintToken': {
            'direction': 'OUTGOING',
            'description': 'Mints AR tokens',
            'method': '0x40c10f19'
        }
    },
    'MINING': {
        'submitBlock': {
            'direction': 'OUTGOING',
            'description': 'Submits mined block',
            'method': '0x9b3d47b4'
        },
        'verifyBlock': {
            'direction': 'NEUTRAL',
            'description': 'Verifies block validity',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims mining rewards',
            'method': '0x4e71d92d'
        }
    },
    'PROFIT_SHARING': {
        'createCommunity': {
            'direction': 'OUTGOING',
            'description': 'Creates profit sharing token',
            'method': '0x1698ee82'
        },
        'joinCommunity': {
            'direction': 'OUTGOING',
            'description': 'Joins profit sharing community',
            'method': '0x9b3d47b4'
        },
        'distribute': {
            'direction': 'OUTGOING',
            'description': 'Distributes community profits',
            'method': '0x7535d246'
        }
    },
    'SMARTWEAVE': {
        'deployContract': {
            'direction': 'OUTGOING',
            'description': 'Deploys smart contract',
            'method': '0x1698ee82'
        },
        'interactContract': {
            'direction': 'OUTGOING',
            'description': 'Interacts with contract',
            'method': '0x7535d246'
        },
        'readContract': {
            'direction': 'NEUTRAL',
            'description': 'Reads contract state',
            'method': '0x9d2f32dd'
        }
    }
}

# Combined functions for all versions
ARWEAVE_FUNCTIONS = {
    'V1': ARWEAVE_V1_FUNCTIONS
}