"""Rook Protocol Functions for all versions"""

ROOK_V1_FUNCTIONS = {
    'TRADING': {
        'submitOrder': {
            'direction': 'OUTGOING',
            'description': 'Submits trading order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'settleOrder': {
            'direction': 'BOTH',
            'description': 'Settles matched order',
            'method': '0x4ce38b5f'
        },
        'batchSettlement': {
            'direction': 'BOTH',
            'description': 'Settles multiple orders',
            'method': '0x945bcec9'
        }
    },
    'STAKING': {
        'stakeROOK': {
            'direction': 'OUTGOING',
            'description': 'Stakes ROOK tokens',
            'method': '0xa694fc3a'
        },
        'unstakeROOK': {
            'direction': 'INCOMING',
            'description': 'Unstakes ROOK tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'KEEPER': {
        'submitSolution': {
            'direction': 'OUTGOING',
            'description': 'Submits settlement solution',
            'method': '0x7535d246'
        },
        'claimBounty': {
            'direction': 'INCOMING',
            'description': 'Claims keeper bounty',
            'method': '0x4e71d92d'
        }
    },
    'COORDINATOR': {
        'registerCoordinator': {
            'direction': 'OUTGOING',
            'description': 'Registers as MEV coordinator',
            'method': '0x1698ee82'
        },
        'updateCoordinatorConfig': {
            'direction': 'OUTGOING',
            'description': 'Updates coordinator settings',
            'method': '0x7535d246'
        },
        'claimCoordinatorFees': {
            'direction': 'INCOMING',
            'description': 'Claims coordinator fees',
            'method': '0xd294f093'
        }
    }
}

# Combined functions for all versions
ROOK_FUNCTIONS = {
    'V1': ROOK_V1_FUNCTIONS
}