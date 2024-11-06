"""SpookySwap Protocol Functions for all versions"""

SPOOKYSWAP_V2_FUNCTIONS = {
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
        'swapExactFTMForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact FTM for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactFTM': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact FTM',
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
        'addLiquidityFTM': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with FTM',
            'method': '0xf305d719'
        },
        'removeLiquidityFTM': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to FTM',
            'method': '0x02751cec'
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
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf69e2046'
        }
    },
    'STAKING': {
        'stakeBOO': {
            'direction': 'OUTGOING',
            'description': 'Stakes BOO tokens',
            'method': '0xa694fc3a'
        },
        'unstakeBOO': {
            'direction': 'INCOMING',
            'description': 'Unstakes BOO tokens',
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
SPOOKYSWAP_FUNCTIONS = {
    'V2': SPOOKYSWAP_V2_FUNCTIONS
}