"""KyberSwap Protocol Functions for all versions"""

KYBERSWAP_V1_FUNCTIONS = {
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
        'swapExactETHForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact ETH for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactETH': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact ETH',
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
        'addStaticLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds static liquidity to pool',
            'method': '0x4515cef3'
        },
        'removeStaticLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes static liquidity from pool',
            'method': '0x5c11d795'
        }
    },
    'ELASTIC': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints elastic pool position',
            'method': '0x88316456'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns elastic pool position',
            'method': '0x89afcb44'
        },
        'collect': {
            'direction': 'INCOMING',
            'description': 'Collects earned fees',
            'method': '0x4f1eb3d8'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        }
    },
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x441a3e70'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal from farm',
            'method': '0x5312ea8e'
        }
    }
}

# Combined functions for all versions
KYBERSWAP_FUNCTIONS = {
    'V1': KYBERSWAP_V1_FUNCTIONS
}