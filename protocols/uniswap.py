UNISWAP_FUNCTIONS = {
    'V2': {
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
            'addLiquidity': {
                'direction': 'OUTGOING',
                'description': 'Adds liquidity to token pair',
                'method': '0xe8e33700'
            },
            'removeLiquidity': {
                'direction': 'INCOMING',
                'description': 'Removes liquidity from token pair',
                'method': '0xbaa2abde'
            }
        }
    },
    'V3': {
        'SWAP': {
            'exactInputSingle': {
                'direction': 'BOTH',
                'description': 'Swaps exact tokens for another via single pool',
                'method': '0x414bf389'
            },
            'exactInput': {
                'direction': 'BOTH',
                'description': 'Swaps exact tokens for another via multiple pools',
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
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Creates a new position in a V3 pool',
                'method': '0x88316456'
            },
            'increaseLiquidity': {
                'direction': 'OUTGOING',
                'description': 'Increases liquidity in an existing position',
                'method': '0x219f5d17'
            },
            'decreaseLiquidity': {
                'direction': 'INCOMING',
                'description': 'Decreases liquidity in a position',
                'method': '0x0c49ccbe'
            }
        }
    }
}