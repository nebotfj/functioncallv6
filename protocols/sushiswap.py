SUSHISWAP_FUNCTIONS = {
    'V2': {
        'SWAP': {
            'swapExactTokensForTokens': {
                'direction': 'BOTH',
                'description': 'Swaps exact amount of tokens for another token',
                'method': '0x38ed1739'
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
            }
        }
    }
}