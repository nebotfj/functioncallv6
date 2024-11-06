"""Polymarket Protocol Functions for all versions"""

POLYMARKET_V1_FUNCTIONS = {
    'MARKETS': {
        'createMarket': {
            'direction': 'OUTGOING',
            'description': 'Creates prediction market',
            'method': '0x1698ee82'
        },
        'buyOutcome': {
            'direction': 'OUTGOING',
            'description': 'Buys market outcome tokens',
            'method': '0x94b576de'
        },
        'sellOutcome': {
            'direction': 'INCOMING',
            'description': 'Sells market outcome tokens',
            'method': '0x454a2ab3'
        },
        'claimWinnings': {
            'direction': 'INCOMING',
            'description': 'Claims market winnings',
            'method': '0x4e71d92d'
        },
        'resolveMarket': {
            'direction': 'OUTGOING',
            'description': 'Resolves market outcome',
            'method': '0x7535d246'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to market',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from market',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims liquidity fees',
            'method': '0xd294f093'
        }
    },
    'COLLATERAL': {
        'depositCollateral': {
            'direction': 'OUTGOING',
            'description': 'Deposits trading collateral',
            'method': '0x47e7ef24'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws trading collateral',
            'method': '0x69328dec'
        },
        'bridgeAssets': {
            'direction': 'BOTH',
            'description': 'Bridges assets cross-chain',
            'method': '0x8b9e4f93'
        }
    }
}

# Combined functions for all versions
POLYMARKET_FUNCTIONS = {
    'V1': POLYMARKET_V1_FUNCTIONS
}