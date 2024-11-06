"""PancakeSwap Protocol Functions for all versions"""

PANCAKESWAP_V2_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens for another token',
            'method': '0x38ed1739'
        },
        'swapTokensForExactTokens': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact amount of another token',
            'method': '0x8803dbee'
        },
        'swapExactETHForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact amount of BNB for tokens',
            'method': '0x7ff36ab5'
        },
        'swapExactTokensForETH': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens for BNB',
            'method': '0x18cbafe5'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to token pair',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from token pair',
            'method': '0xbaa2abde'
        },
        'addLiquidityETH': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with BNB',
            'method': '0xf305d719'
        },
        'removeLiquidityETH': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to BNB',
            'method': '0x02751cec'
        }
    },
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits LP tokens for farming',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws LP tokens from farming',
            'method': '0x441a3e70'
        },
        'enterStaking': {
            'direction': 'OUTGOING',
            'description': 'Enters CAKE staking pool',
            'method': '0xdc694d6f'
        },
        'leaveStaking': {
            'direction': 'INCOMING',
            'description': 'Exits CAKE staking pool',
            'method': '0x405d8dcd'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal from farm',
            'method': '0x5312ea8e'
        }
    },
    'PREDICTION': {
        'betBull': {
            'direction': 'OUTGOING',
            'description': 'Places UP prediction bet',
            'method': '0x57fb096f'
        },
        'betBear': {
            'direction': 'OUTGOING',
            'description': 'Places DOWN prediction bet',
            'method': '0x223c3de5'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims prediction rewards',
            'method': '0x4e71d92d'
        }
    },
    'LOTTERY': {
        'buyTickets': {
            'direction': 'OUTGOING',
            'description': 'Purchases lottery tickets',
            'method': '0x88146cc4'
        },
        'claimTickets': {
            'direction': 'INCOMING',
            'description': 'Claims lottery winnings',
            'method': '0x6f4a2cd0'
        }
    }
}

PANCAKESWAP_V3_FUNCTIONS = {
    'SWAP': {
        'exactInput': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens via multiple pools',
            'method': '0xc04b8d59'
        },
        'exactOutput': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output via multiple pools',
            'method': '0xf28c0498'
        },
        'exactInputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens via single pool',
            'method': '0x414bf389'
        },
        'exactOutputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output via single pool',
            'method': '0xdb3e2198'
        }
    },
    'LIQUIDITY': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Creates new position in V3 pool',
            'method': '0x88316456'
        },
        'increaseLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Increases liquidity in position',
            'method': '0x219f5d17'
        },
        'decreaseLiquidity': {
            'direction': 'INCOMING',
            'description': 'Decreases liquidity in position',
            'method': '0x0c49ccbe'
        },
        'collect': {
            'direction': 'INCOMING',
            'description': 'Collects fees from position',
            'method': '0x4f1eb3d8'
        }
    },
    'STAKING': {
        'depositCAKE': {
            'direction': 'OUTGOING',
            'description': 'Deposits CAKE for fixed staking',
            'method': '0x127d1a8e'
        },
        'withdrawCAKE': {
            'direction': 'INCOMING',
            'description': 'Withdraws CAKE from fixed staking',
            'method': '0x38d52e0f'
        },
        'harvestRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x18fccc76'
        }
    },
    'POSITION_MANAGER': {
        'createAndInitializePoolIfNecessary': {
            'direction': 'OUTGOING',
            'description': 'Creates and initializes new pool if needed',
            'method': '0x13ead562'
        },
        'multicall': {
            'direction': 'BOTH',
            'description': 'Executes multiple position operations',
            'method': '0xac9650d8'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns liquidity position NFT',
            'method': '0x89afcb44'
        }
    }
}

# Combined functions for all versions
PANCAKESWAP_FUNCTIONS = {
    'V2': PANCAKESWAP_V2_FUNCTIONS,
    'V3': PANCAKESWAP_V3_FUNCTIONS
}