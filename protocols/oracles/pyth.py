"""Pyth Network Protocol Functions for all versions"""

PYTH_V1_FUNCTIONS = {
    'ORACLE': {
        'updatePrice': {
            'direction': 'OUTGOING',
            'description': 'Updates price feed',
            'method': '0x7535d246'
        },
        'getPrice': {
            'direction': 'NEUTRAL',
            'description': 'Gets current price',
            'method': '0x9d2f32dd'
        },
        'getPriceUnsafe': {
            'direction': 'NEUTRAL',
            'description': 'Gets price without checks',
            'method': '0x8263db17'
        },
        'getEmaPrice': {
            'direction': 'NEUTRAL',
            'description': 'Gets EMA price value',
            'method': '0x98f4b1b2'
        }
    },
    'GOVERNANCE': {
        'proposeUpdate': {
            'direction': 'OUTGOING',
            'description': 'Proposes price update',
            'method': '0xda95691a'
        },
        'executeUpdate': {
            'direction': 'OUTGOING',
            'description': 'Executes price update',
            'method': '0xfe0d94c1'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims oracle rewards',
            'method': '0xe6f1daf2'
        }
    },
    'WORMHOLE': {
        'verifyPrice': {
            'direction': 'NEUTRAL',
            'description': 'Verifies cross-chain price',
            'method': '0x7535d246'
        },
        'updatePriceFeeds': {
            'direction': 'OUTGOING',
            'description': 'Updates multiple feeds',
            'method': '0x945bcec9'
        }
    }
}

# Combined functions for all versions
PYTH_FUNCTIONS = {
    'V1': PYTH_V1_FUNCTIONS
}