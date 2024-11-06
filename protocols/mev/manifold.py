"""Manifold Protocol Functions for all versions"""

MANIFOLD_V1_FUNCTIONS = {
    'TRADING': {
        'submitOrder': {
            'direction': 'OUTGOING',
            'description': 'Submits trading order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'settleOrder': {
            'direction': 'BOTH',
            'description': 'Settles matched order',
            'method': '0x4ce38b5f'
        }
    },
    'SEARCHER': {
        'registerSearcher': {
            'direction': 'OUTGOING',
            'description': 'Registers as MEV searcher',
            'method': '0x1698ee82'
        },
        'submitBackrun': {
            'direction': 'OUTGOING',
            'description': 'Submits backrun transaction',
            'method': '0x7535d246'
        },
        'claimSearcherRewards': {
            'direction': 'INCOMING',
            'description': 'Claims searcher rewards',
            'method': '0x4e71d92d'
        }
    },
    'AUCTION': {
        'startAuction': {
            'direction': 'OUTGOING',
            'description': 'Starts MEV auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'settleAuction': {
            'direction': 'BOTH',
            'description': 'Settles completed auction',
            'method': '0x4ce38b5f'
        }
    },
    'PROTECTION': {
        'enableSandwich': {
            'direction': 'OUTGOING',
            'description': 'Enables sandwich protection',
            'method': '0x3a088cd2'
        },
        'disableSandwich': {
            'direction': 'OUTGOING',
            'description': 'Disables sandwich protection',
            'method': '0x5f7b8feb'
        }
    }
}

# Combined functions for all versions
MANIFOLD_FUNCTIONS = {
    'V1': MANIFOLD_V1_FUNCTIONS
}