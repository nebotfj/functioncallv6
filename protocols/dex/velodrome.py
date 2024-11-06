"""Velodrome Protocol Functions for all versions"""

VELODROME_V2_FUNCTIONS = {
    'SWAP': {
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
        'swapTokensForExactTokens': {
            'direction': 'BOTH',
            'description': 'Swaps for exact amount of tokens',
            'method': '0x8803dbee'
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
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new liquidity pool',
            'method': '0x1698ee82'
        },
        'gauge': {
            'direction': 'OUTGOING',
            'description': 'Manages gauge parameters',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes VELO tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes VELO tokens',
            'method': '0x2e1a7d4d'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x3d18b912'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes for gauge weights',
            'method': '0x15373e3d'
        }
    },
    'BRIBES': {
        'notifyRewardAmount': {
            'direction': 'OUTGOING',
            'description': 'Notifies reward distribution',
            'method': '0x3c6b16ab'
        },
        'claimBribes': {
            'direction': 'INCOMING',
            'description': 'Claims gauge bribes',
            'method': '0x4e71d92d'
        },
        'addBribe': {
            'direction': 'OUTGOING',
            'description': 'Adds bribe to gauge',
            'method': '0x3a088cd2'
        }
    }
}

# Combined functions for all versions
VELODROME_FUNCTIONS = {
    'V2': VELODROME_V2_FUNCTIONS
}