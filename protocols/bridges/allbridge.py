"""Allbridge Protocol Functions for all versions"""

ALLBRIDGE_V1_FUNCTIONS = {
    'BRIDGE': {
        'bridge': {
            'direction': 'OUTGOING',
            'description': 'Initiates bridge transfer',
            'method': '0x8b9e4f93'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps tokens across chains',
            'method': '0x128acb08'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims bridged tokens',
            'method': '0x4e71d92d'
        },
        'bridgeTokens': {
            'direction': 'OUTGOING',
            'description': 'Bridges specific tokens',
            'method': '0x8b9e4f93'
        },
        'unwrapTokens': {
            'direction': 'INCOMING',
            'description': 'Unwraps bridged tokens',
            'method': '0x39f7e493'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge pool',
            'method': '0xbaa2abde'
        },
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees',
            'method': '0xd294f093'
        }
    },
    'FARMING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in farm',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from farm',
            'method': '0x2e1a7d4d'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
ALLBRIDGE_FUNCTIONS = {
    'V1': ALLBRIDGE_V1_FUNCTIONS
}