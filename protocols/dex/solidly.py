"""Solidly Protocol Functions for all versions"""

SOLIDLY_V1_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens',
            'method': '0x38ed1739'
        },
        'swapExactETHForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact ETH for tokens',
            'method': '0x7ff36ab5'
        },
        'swapExactTokensForETH': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens for ETH',
            'method': '0x18cbafe5'
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
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints LP tokens',
            'method': '0x6a627842'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns LP tokens',
            'method': '0x89afcb44'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x3d18b912'
        },
        'compoundReward': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'VOTING': {
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes for gauge weights',
            'method': '0x15373e3d'
        },
        'reset': {
            'direction': 'OUTGOING',
            'description': 'Resets vote weights',
            'method': '0xd826f88f'
        },
        'poke': {
            'direction': 'OUTGOING',
            'description': 'Updates vote weights',
            'method': '0x32145f90'
        }
    }
}

# Combined functions for all versions
SOLIDLY_FUNCTIONS = {
    'V1': SOLIDLY_V1_FUNCTIONS
}