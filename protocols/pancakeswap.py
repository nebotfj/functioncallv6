PANCAKESWAP_FUNCTIONS = {
    'V2': {
        'SWAP': {
            'swapExactTokensForTokens': {
                'direction': 'BOTH',
                'description': 'Swaps exact amount of tokens',
                'method': '0x38ed1739'
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
            }
        },
        'FARMING': {
            'deposit': {
                'direction': 'OUTGOING',
                'description': 'Stakes LP tokens in farm',
                'method': '0xe2bbb158'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Unstakes LP tokens from farm',
                'method': '0x441a3e70'
            }
        }
    },
    'V3': {
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
            }
        }
    }
}