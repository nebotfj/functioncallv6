"""Ramses Exchange Protocol Functions for all versions"""

RAMSES_V1_FUNCTIONS = {
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
        'addLiquidityETH': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with ETH',
            'method': '0xf305d719'
        },
        'removeLiquidityETH': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to ETH',
            'method': '0x02751cec'
        }
    },
    'STAKING': {
        'stakeRAM': {
            'direction': 'OUTGOING',
            'description': 'Stakes RAM tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRAM': {
            'direction': 'INCOMING',
            'description': 'Unstakes RAM tokens',
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
    },
    'BRIBES': {
        'addBribe': {
            'direction': 'OUTGOING',
            'description': 'Adds bribe to gauge',
            'method': '0x3a088cd2'
        },
        'claimBribe': {
            'direction': 'INCOMING',
            'description': 'Claims bribe rewards',
            'method': '0x4e71d92d'
        },
        'voteBribe': {
            'direction': 'OUTGOING',
            'description': 'Votes for bribe allocation',
            'method': '0x15373e3d'
        }
    }
}

# Combined functions for all versions
RAMSES_FUNCTIONS = {
    'V1': RAMSES_V1_FUNCTIONS
}