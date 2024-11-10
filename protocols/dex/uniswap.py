"""Uniswap Protocol Functions for all versions"""

UNISWAP_V2_FUNCTIONS = {
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
            'direction': 'BOTH',
            'description': 'Swaps exact amount of ETH for tokens',
            'method': '0x7ff36ab5'
        },
        'swapTokensForExactETH': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact amount of ETH',
            'method': '0x4a25d94a'
        },
        'swapExactTokensForETH': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens for ETH',
            'method': '0x18cbafe5'
        },
        'swapETHForExactTokens': {
            'direction': 'BOTH',
            'description': 'Swaps ETH for exact amount of tokens',
            'method': '0xfb3bdb41'
        },
        'ethToTokenSwapInput': {
            'direction': 'BOTH',
            'description': 'Swaps ETH for tokens with input amount specified',
            'method': '0xf39b5b9b'
        },
        'ethToTokenSwapOutput': {
            'direction': 'BOTH',
            'description': 'Swaps ETH for exact token amount',
            'method': '0x6b1d4db7'
        },
        'tokenToEthSwapInput': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for ETH with input amount specified',
            'method': '0x95e3c50b'
        },
        'tokenToTokenSwapInput': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for tokens with input amount specified',
            'method': '0xddf7e1a7'
        },
        'swapExactETHForAlpha': {
            'direction': 'OUTGOING',
            'description': 'Swap exact ETH for Alpha token',
            'method': '0x7ff36ab5',
            #'protocol': ['Uniswap V2']
        },
    },
    'POSITION': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Creates new position in pool',
            'method': '0x6a627842'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns liquidity position',
            'method': '0x89afcb44'
        },
        'collect': {
            'direction': 'INCOMING',
            'description': 'Collects tokens owed to position',
            'method': '0x4f1eb3d8'
        },
        'flash': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes a new pool',
            'method': '0x1673c3c1'
        },
        'increaseObservationCardinalityNext': {
            'direction': 'OUTGOING',
            'description': 'Increases observation cardinality',
            'method': '0x32148f67'
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
        'removeLiquidityWithPermit': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity using permit',
            'method': '0x2195995c'
        },
        'removeLiquidityETHWithPermit': {
            'direction': 'INCOMING',
            'description': 'Removes ETH liquidity with permit',
            'method': '0xded9382a'
        }
    },
    'FLASH': {
        'flash': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        }
    }
}

UNISWAP_V3_FUNCTIONS = {
    'SWAP': {
        'exactInput': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens through multiple pools',
            'method': '0xc04b8d59'
        },
        'exactOutput': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output through multiple pools',
            'method': '0xf28c0498'
        },
        'exactInputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens through single pool',
            'method': '0x414bf389'
        },
        'exactOutputSingle': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for exact output through single pool',
            'method': '0xdb3e2198'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Performs swap in pool',
            'method': '0x128acb08'
        }
    },
    'LIQUIDITY': {
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
            'description': 'Collects tokens owed to position',
            'method': '0x4f1eb3d8'
        },
        'createAndInitializePoolIfNecessary': {
            'direction': 'OUTGOING',
            'description': 'Creates and initializes new pool if needed',
            'method': '0x13ead562'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Creates new position',
            'method': '0x88316456'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns liquidity position',
            'method': '0x89afcb44'
        }
    },
    'POSITION': {
        'positions': {
            'direction': 'NEUTRAL',
            'description': 'Gets position information',
            'method': '0x99fbab88'
        },
        'positions_by_ids': {
            'direction': 'NEUTRAL',
            'description': 'Gets positions by IDs',
            'method': '0x7e3235c2'
        },
        'collect_fees': {
            'direction': 'INCOMING',
            'description': 'Collects position fees',
            'method': '0x52a9c8e6'
        },
        'transfer': {
            'direction': 'BOTH',
            'description': 'Transfers position',
            'method': '0x23b872dd'
        },
        'approve': {
            'direction': 'OUTGOING',
            'description': 'Approves position transfer',
            'method': '0x095ea7b3'
        }
    },
    'FLASH': {
        'flash': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'flashCallback': {
            'direction': 'BOTH',
            'description': 'Callback for flash swap',
            'method': '0x84242c54'
        }
    },
    'ORACLE': {
        'observe': {
            'direction': 'NEUTRAL',
            'description': 'Gets price observations',
            'method': '0x883bdbfd'
        },
        'increaseObservationCardinalityNext': {
            'direction': 'OUTGOING',
            'description': 'Increases oracle observation cardinality',
            'method': '0x32148f67'
        }
    }
}

UNISWAP_V4_FUNCTIONS = {
    'SWAP': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Performs swap in pool',
            'method': '0x128acb08'
        },
        'swapWithHooks': {
            'direction': 'BOTH',
            'description': 'Performs swap with hooks',
            'method': '0x7c8e4956'
        },
        'swapWithPermit': {
            'direction': 'BOTH',
            'description': 'Performs swap with permit',
            'method': '0x2521b930'
        }
    },
    'LIQUIDITY': {
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies liquidity position',
            'method': '0x0c49ccbe'
        },
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
        'donate': {
            'direction': 'OUTGOING',
            'description': 'Donates liquidity to pool',
            'method': '0x9b3d47b4'
        }
    },
    'HOOKS': {
        'beforeInitialize': {
            'direction': 'OUTGOING',
            'description': 'Hook before pool initialization',
            'method': '0x6d4f0e36'
        },
        'afterInitialize': {
            'direction': 'OUTGOING',
            'description': 'Hook after pool initialization',
            'method': '0x91c49bf8'
        },
        'beforeModifyPosition': {
            'direction': 'OUTGOING',
            'description': 'Hook before position modification',
            'method': '0x3687b58c'
        },
        'afterModifyPosition': {
            'direction': 'OUTGOING',
            'description': 'Hook after position modification',
            'method': '0x2c5c3e56'
        },
        'beforeSwap': {
            'direction': 'OUTGOING',
            'description': 'Hook before swap',
            'method': '0x9d2f32dd'
        },
        'afterSwap': {
            'direction': 'OUTGOING',
            'description': 'Hook after swap',
            'method': '0x1c12d3b1'
        }
    },
    'FLASH': {
        'flash': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'lockAcquired': {
            'direction': 'BOTH',
            'description': 'Callback when lock is acquired',
            'method': '0x43cb3e1c'
        }
    },
    'POOLS': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes new pool',
            'method': '0x1673c3c1'
        },
        'getPool': {
            'direction': 'NEUTRAL',
            'description': 'Gets pool address',
            'method': '0x1698ee82'
        },
        'setHookFees': {
            'direction': 'OUTGOING',
            'description': 'Sets fees for hooks',
            'method': '0x2f4f5cc5'
        }
    }
}

# Combined functions for all versions
UNISWAP_FUNCTIONS = {
    'V2': UNISWAP_V2_FUNCTIONS,
    'V3': UNISWAP_V3_FUNCTIONS,
    'V4': UNISWAP_V4_FUNCTIONS
}