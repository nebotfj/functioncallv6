"""TraderJoe Protocol Functions for all versions"""

TRADERJOE_V1_FUNCTIONS = {
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
        'swapExactAVAXForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact AVAX for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactAVAX': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact AVAX',
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
        'addLiquidityAVAX': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with AVAX',
            'method': '0xf305d719'
        },
        'removeLiquidityAVAX': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to AVAX',
            'method': '0x02751cec'
        }
    },
    'LENDING': {
        'supply': {
            'direction': 'OUTGOING',
            'description': 'Supplies assets to lending pool',
            'method': '0x617ba037'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from lending pool',
            'method': '0x69328dec'
        },
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows assets from lending pool',
            'method': '0xc858f5ba'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed assets',
            'method': '0x573ade81'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes JOE tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes JOE tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
TRADERJOE_FUNCTIONS = {
    'V1': TRADERJOE_V1_FUNCTIONS
}