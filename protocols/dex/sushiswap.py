"""SushiSwap Protocol Functions for all versions"""

SUSHISWAP_V1_FUNCTIONS = {
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
            'description': 'Swaps exact amount of ETH for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactETH': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact amount of ETH',
            'method': '0x4a25d94a'
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
            'description': 'Adds liquidity with ETH',
            'method': '0xf305d719'
        },
        'removeLiquidityETH': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity to ETH',
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
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0xddc63262'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal of LP tokens',
            'method': '0x5312ea8e'
        }
    }
}

SUSHISWAP_V2_FUNCTIONS = {
    'SWAP': {
        'exactInputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens via single pool',
            'method': '0x414bf389'
        },
        'exactInput': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens via multiple pools',
            'method': '0xc04b8d59'
        },
        'exactOutputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output via single pool',
            'method': '0xdb3e2198'
        },
        'exactOutput': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output via multiple pools',
            'method': '0xf28c0498'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds concentrated liquidity to pool',
            'method': '0x0f4f8da7'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes concentrated liquidity from pool',
            'method': '0x0c49ccbe'
        },
        'collectFees': {
            'direction': 'INCOMING',
            'description': 'Collects accumulated fees',
            'method': '0x52a9c8e6'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes SUSHI tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes SUSHI tokens',
            'method': '0x2e1a7d4d'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x3d18b912'
        }
    },
    'BENTOBOX': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens into BentoBox',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws tokens from BentoBox',
            'method': '0x441a3e70'
        },
        'transfer': {
            'direction': 'BOTH',
            'description': 'Transfers tokens within BentoBox',
            'method': '0x23b872dd'
        }
    }
}

SUSHISWAP_V3_FUNCTIONS = {
    'SWAP': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Performs swap with concentrated liquidity',
            'method': '0x128acb08'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        }
    },
    'LIQUIDITY': {
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies liquidity position',
            'method': '0x0c49ccbe'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Creates new concentrated liquidity position',
            'method': '0x88316456'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns concentrated liquidity position',
            'method': '0x89afcb44'
        }
    },
    'TRIDENT': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new Trident pool',
            'method': '0x1698ee82'
        },
        'harvestProtocolFee': {
            'direction': 'INCOMING',
            'description': 'Collects protocol fees',
            'method': '0x5325cbd5'
        }
    }
}

# Combined functions for all versions
SUSHISWAP_FUNCTIONS = {
    'V1': SUSHISWAP_V1_FUNCTIONS,
    'V2': SUSHISWAP_V2_FUNCTIONS,
    'V3': SUSHISWAP_V3_FUNCTIONS
}