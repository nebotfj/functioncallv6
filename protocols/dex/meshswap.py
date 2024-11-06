"""Meshswap Protocol Functions for all versions"""

MESHSWAP_V1_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens',
            'method': '0x38ed1739'
        },
        'swapTokensForExactTokens': {
            'direction': 'BOTH',
            'description': 'Swaps for exact amount of tokens',
            'method': '0x8803dbee'
        },
        'swapExactMATICForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact MATIC for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactMATIC': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact MATIC',
            'method': '0x4a25d94a'
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
        'addLiquidityMATIC': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with MATIC',
            'method': '0xf305d719'
        },
        'removeLiquidityMATIC': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to MATIC',
            'method': '0x02751cec'
        },
        'mintLPToken': {
            'direction': 'OUTGOING',
            'description': 'Mints LP tokens',
            'method': '0x6a627842'
        },
        'burnLPToken': {
            'direction': 'INCOMING',
            'description': 'Burns LP tokens',
            'method': '0x89afcb44'
        }
    },
    'FARMING': {
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
        'harvestRewards': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
MESHSWAP_FUNCTIONS = {
    'V1': MESHSWAP_V1_FUNCTIONS
}