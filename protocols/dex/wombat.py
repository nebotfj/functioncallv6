"""Wombat Exchange Protocol Functions for all versions"""

WOMBAT_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
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
        'quotePotentialSwap': {
            'direction': 'NEUTRAL',
            'description': 'Gets quote for potential swap',
            'method': '0x9d2f32dd'
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
        'addLiquidityNative': {
            'direction': 'OUTGOING',
            'description': 'Adds native token liquidity',
            'method': '0xf305d719'
        },
        'removeLiquidityNative': {
            'direction': 'INCOMING',
            'description': 'Removes native token liquidity',
            'method': '0x02751cec'
        }
    },
    'STAKING': {
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
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'boostRewards': {
            'direction': 'OUTGOING',
            'description': 'Boosts reward earnings',
            'method': '0x9b3d47b4'
        },
        'lockWOM': {
            'direction': 'OUTGOING',
            'description': 'Locks WOM tokens',
            'method': '0x3d18b912'
        },
        'unlockWOM': {
            'direction': 'INCOMING',
            'description': 'Unlocks WOM tokens',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
WOMBAT_FUNCTIONS = {
    'V1': WOMBAT_V1_FUNCTIONS
}