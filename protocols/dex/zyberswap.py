"""ZyberSwap Protocol Functions for all versions"""

ZYBERSWAP_V1_FUNCTIONS = {
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
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'ZAPPING': {
        'zapIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps token into LP position',
            'method': '0x6d914547'
        },
        'zapOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of LP position',
            'method': '0x0c2d3f2b'
        },
        'zapInETH': {
            'direction': 'OUTGOING',
            'description': 'Zaps ETH into LP position',
            'method': '0x29b3d8f1'
        },
        'zapOutETH': {
            'direction': 'INCOMING',
            'description': 'Zaps LP position to ETH',
            'method': '0x4c8d8528'
        }
    }
}

# Combined functions for all versions
ZYBERSWAP_FUNCTIONS = {
    'V1': ZYBERSWAP_V1_FUNCTIONS
}