"""Ankr Protocol Functions for all versions"""

ANKR_V1_FUNCTIONS = {
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'restake': {
            'direction': 'OUTGOING',
            'description': 'Restakes earned rewards',
            'method': '0x7b24a5fd'
        },
        'flashUnstake': {
            'direction': 'BOTH',
            'description': 'Performs instant unstake',
            'method': '0x4ce38b5f'
        }
    },
    'LIQUID_STAKING': {
        'mintAETH': {
            'direction': 'OUTGOING',
            'description': 'Mints aETH tokens',
            'method': '0x40c10f19'
        },
        'burnAETH': {
            'direction': 'INCOMING',
            'description': 'Burns aETH tokens',
            'method': '0x89afcb44'
        },
        'convertToShares': {
            'direction': 'BOTH',
            'description': 'Converts assets to shares',
            'method': '0x7c025200'
        },
        'convertToAssets': {
            'direction': 'BOTH',
            'description': 'Converts shares to assets',
            'method': '0x2f4f5cc5'
        }
    },
    'BRIDGE': {
        'bridgeAssets': {
            'direction': 'OUTGOING',
            'description': 'Bridges assets cross-chain',
            'method': '0x8b9e4f93'
        },
        'claimBridged': {
            'direction': 'INCOMING',
            'description': 'Claims bridged assets',
            'method': '0x4e71d92d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal',
            'method': '0x5312ea8e'
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

# Combined functions for all versions
ANKR_FUNCTIONS = {
    'V1': ANKR_V1_FUNCTIONS
}