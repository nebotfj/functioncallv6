"""Stargate Protocol Functions for all versions"""

STARGATE_V1_FUNCTIONS = {
    'BRIDGE': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps tokens across chains',
            'method': '0x128acb08'
        },
        'sendCredits': {
            'direction': 'OUTGOING',
            'description': 'Sends bridge credits',
            'method': '0x9b3d47b4'
        },
        'redeemLocal': {
            'direction': 'INCOMING',
            'description': 'Redeems tokens locally',
            'method': '0x7c025200'
        },
        'redeemRemote': {
            'direction': 'INCOMING',
            'description': 'Redeems tokens on remote chain',
            'method': '0x4ce38b5f'
        },
        'instantRedeemLocal': {
            'direction': 'INCOMING',
            'description': 'Instantly redeems local tokens',
            'method': '0x2f4f5cc5'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        },
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new bridge pool',
            'method': '0x1698ee82'
        },
        'setFees': {
            'direction': 'OUTGOING',
            'description': 'Sets pool fee parameters',
            'method': '0xe74b981b'
        }
    },
    'STAKING': {
        'stakeLP': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLP': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
STARGATE_FUNCTIONS = {
    'V1': STARGATE_V1_FUNCTIONS
}