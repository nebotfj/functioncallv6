"""Hashflow Protocol Functions for all versions"""

HASHFLOW_V3_FUNCTIONS = {
    'TRADING': {
        'requestQuote': {
            'direction': 'NEUTRAL',
            'description': 'Requests trading quote',
            'method': '0x9d2f32dd'
        },
        'fillQuote': {
            'direction': 'BOTH',
            'description': 'Fills trading quote',
            'method': '0x6945b123'
        },
        'limitOrder': {
            'direction': 'OUTGOING',
            'description': 'Places limit order',
            'method': '0x52a9c8e6'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels limit order',
            'method': '0x2e1a7d4d'
        }
    },
    'RFQ': {
        'requestForQuote': {
            'direction': 'NEUTRAL',
            'description': 'Requests RFQ quote',
            'method': '0x9d2f32dd'
        },
        'provideQuote': {
            'direction': 'OUTGOING',
            'description': 'Provides RFQ quote',
            'method': '0x89f9aab7'
        },
        'acceptQuote': {
            'direction': 'BOTH',
            'description': 'Accepts RFQ quote',
            'method': '0x7c025200'
        }
    },
    'POOLS': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new liquidity pool',
            'method': '0x1698ee82'
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
    }
}

# Combined functions for all versions
HASHFLOW_FUNCTIONS = {
    'V3': HASHFLOW_V3_FUNCTIONS
}