"""Polygon Bridge Protocol Functions for all versions"""

POLYGON_V1_FUNCTIONS = {
    'BRIDGE': {
        'depositFor': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens to Polygon',
            'method': '0x8b9e4f93'
        },
        'exit': {
            'direction': 'INCOMING',
            'description': 'Exits assets from Polygon',
            'method': '0x32b7006d'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets to root chain',
            'method': '0x2e1a7d4d'
        },
        'depositEtherFor': {
            'direction': 'OUTGOING',
            'description': 'Deposits ETH to Polygon',
            'method': '0xb1a1a882'
        }
    },
    'CHECKPOINT': {
        'submitCheckpoint': {
            'direction': 'OUTGOING',
            'description': 'Submits state checkpoint',
            'method': '0x9b3d47b4'
        },
        'validateCheckpoint': {
            'direction': 'NEUTRAL',
            'description': 'Validates checkpoint submission',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes MATIC tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes MATIC tokens',
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
POLYGON_FUNCTIONS = {
    'V1': POLYGON_V1_FUNCTIONS
}