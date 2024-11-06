"""Biswap Protocol Functions for all versions"""

BISWAP_V2_FUNCTIONS = {
    'SWAP': {
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
        'swapExactBNBForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact BNB for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactBNB': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact BNB',
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
        'addLiquidityBNB': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with BNB',
            'method': '0xf305d719'
        },
        'removeLiquidityBNB': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to BNB',
            'method': '0x02751cec'
        }
    },
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens in farm',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws LP tokens from farm',
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
    },
    'LAUNCHPAD': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in launchpad event',
            'method': '0x8f38249c'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims launchpad tokens',
            'method': '0x4641257d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal from launchpad',
            'method': '0x5312ea8e'
        }
    }
}

# Combined functions for all versions
BISWAP_FUNCTIONS = {
    'V2': BISWAP_V2_FUNCTIONS
}