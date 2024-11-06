"""Symbiosis Protocol Functions for all versions"""

SYMBIOSIS_V1_FUNCTIONS = {
    'BRIDGE': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps tokens across chains',
            'method': '0x128acb08'
        },
        'bridge': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens to another chain',
            'method': '0x8b9e4f93'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims bridged tokens',
            'method': '0x4e71d92d'
        },
        'revert': {
            'direction': 'INCOMING',
            'description': 'Reverts failed bridge transaction',
            'method': '0x590e1ae3'
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
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims protocol rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        },
        'harvestFees': {
            'direction': 'INCOMING',
            'description': 'Harvests accumulated fees',
            'method': '0xd294f093'
        }
    }
}

# Combined functions for all versions
SYMBIOSIS_FUNCTIONS = {
    'V1': SYMBIOSIS_V1_FUNCTIONS
}