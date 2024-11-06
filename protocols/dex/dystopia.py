"""Dystopia Protocol Functions for all versions"""

DYSTOPIA_V1_FUNCTIONS = {
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
    'STAKING': {
        'stakeDYST': {
            'direction': 'OUTGOING',
            'description': 'Stakes DYST tokens',
            'method': '0xa694fc3a'
        },
        'unstakeDYST': {
            'direction': 'INCOMING',
            'description': 'Unstakes DYST tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'stakeLPToken': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0x0c49ccbe'
        },
        'unstakeLPToken': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
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
        'getBribesForEpoch': {
            'direction': 'NEUTRAL',
            'description': 'Gets bribes for specific epoch',
            'method': '0x9d2c1b1f'
        }
    }
}

# Combined functions for all versions
DYSTOPIA_FUNCTIONS = {
    'V1': DYSTOPIA_V1_FUNCTIONS
}