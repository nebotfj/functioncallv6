"""Camelot Protocol Functions for all versions"""

CAMELOT_V2_FUNCTIONS = {
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
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'NFT': {
        'mintPosition': {
            'direction': 'OUTGOING',
            'description': 'Mints NFT position',
            'method': '0x88316456'
        },
        'burnPosition': {
            'direction': 'INCOMING',
            'description': 'Burns NFT position',
            'method': '0x89afcb44'
        },
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies NFT position',
            'method': '0x0c49ccbe'
        },
        'transferPosition': {
            'direction': 'BOTH',
            'description': 'Transfers NFT position',
            'method': '0x23b872dd'
        }
    }
}

# Combined functions for all versions
CAMELOT_FUNCTIONS = {
    'V2': CAMELOT_V2_FUNCTIONS
}