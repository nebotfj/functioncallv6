"""Redstone Protocol Functions for all versions"""

REDSTONE_V1_FUNCTIONS = {
    'ORACLE': {
        'updatePrices': {
            'direction': 'OUTGOING',
            'description': 'Updates price feed data',
            'method': '0x7535d246'
        },
        'getPrices': {
            'direction': 'NEUTRAL',
            'description': 'Gets current prices',
            'method': '0x9d2f32dd'
        },
        'signData': {
            'direction': 'OUTGOING',
            'description': 'Signs oracle data',
            'method': '0x8b3a9b4a'
        },
        'verifySignatures': {
            'direction': 'NEUTRAL',
            'description': 'Verifies data signatures',
            'method': '0x6ea9676f'
        }
    },
    'CACHE': {
        'cacheValues': {
            'direction': 'OUTGOING',
            'description': 'Caches price values',
            'method': '0x4ce38b5f'
        },
        'getCachedValues': {
            'direction': 'NEUTRAL',
            'description': 'Retrieves cached values',
            'method': '0x9d2f32dd'
        },
        'updateCache': {
            'direction': 'OUTGOING',
            'description': 'Updates cache data',
            'method': '0x7535d246'
        }
    },
    'AGGREGATION': {
        'aggregateValues': {
            'direction': 'NEUTRAL',
            'description': 'Aggregates price values',
            'method': '0x98f4b1b2'
        },
        'calculateMedian': {
            'direction': 'NEUTRAL',
            'description': 'Calculates median price',
            'method': '0x3c5269a4'
        },
        'validateDataFeed': {
            'direction': 'NEUTRAL',
            'description': 'Validates data feed',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
REDSTONE_FUNCTIONS = {
    'V1': REDSTONE_V1_FUNCTIONS
}