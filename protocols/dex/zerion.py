"""Zerion Protocol Functions for all versions"""

ZERION_V1_FUNCTIONS = {
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
        'limitOrder': {
            'direction': 'OUTGOING',
            'description': 'Places limit order',
            'method': '0x94b576de'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Executes batch of swaps',
            'method': '0x945bcec9'
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
        'zapIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps token into LP position',
            'method': '0x6d914547'
        },
        'zapOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of LP position',
            'method': '0x0c2d3f2b'
        }
    },
    'PORTFOLIO': {
        'track': {
            'direction': 'NEUTRAL',
            'description': 'Tracks portfolio performance',
            'method': '0x9d2f32dd'
        },
        'analyze': {
            'direction': 'NEUTRAL',
            'description': 'Analyzes portfolio metrics',
            'method': '0x7535d246'
        },
        'optimize': {
            'direction': 'NEUTRAL',
            'description': 'Optimizes portfolio allocation',
            'method': '0x2f4f5cc5'
        }
    }
}

# Combined functions for all versions
ZERION_FUNCTIONS = {
    'V1': ZERION_V1_FUNCTIONS
}