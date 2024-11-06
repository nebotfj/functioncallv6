"""ParaSwap Protocol Functions for all versions"""

PARASWAP_V5_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'multiSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        },
        'megaSwap': {
            'direction': 'BOTH',
            'description': 'Executes optimized mega swap',
            'method': '0x46c67b6d'
        },
        'swapOnUniswap': {
            'direction': 'BOTH',
            'description': 'Executes swap via Uniswap',
            'method': '0x7c025200'
        }
    },
    'LIMIT_ORDERS': {
        'createLimitOrder': {
            'direction': 'OUTGOING',
            'description': 'Creates new limit order',
            'method': '0x94b576de'
        },
        'cancelLimitOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing limit order',
            'method': '0x2e1a7d4d'
        },
        'fillLimitOrder': {
            'direction': 'BOTH',
            'description': 'Fills limit order',
            'method': '0xbc61394a'
        }
    },
    'NFT': {
        'swapNFTs': {
            'direction': 'BOTH',
            'description': 'Swaps NFT tokens',
            'method': '0x96cd4ddb'
        },
        'wrapNFTs': {
            'direction': 'BOTH',
            'description': 'Wraps/unwraps NFTs',
            'method': '0x4c4a82f8'
        }
    }
}

# Combined functions for all versions
PARASWAP_FUNCTIONS = {
    'V5': PARASWAP_V5_FUNCTIONS
}