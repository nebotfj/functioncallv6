"""Yield Yak Protocol Functions for all versions"""

YIELD_YAK_V1_FUNCTIONS = {
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets for farming',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws farmed assets',
            'method': '0x69328dec'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Harvests farming rewards',
            'method': '0x4641257d'
        },
        'reinvest': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
        }
    },
    'ROUTER': {
        'findBestPath': {
            'direction': 'NEUTRAL',
            'description': 'Finds optimal swap path',
            'method': '0x9d2f32dd'
        },
        'swapNoSplit': {
            'direction': 'BOTH',
            'description': 'Executes direct swap',
            'method': '0x128acb08'
        },
        'swapMulti': {
            'direction': 'BOTH',
            'description': 'Executes multi-hop swap',
            'method': '0x945bcec9'
        }
    },
    'STAKING': {
        'stakeYAK': {
            'direction': 'OUTGOING',
            'description': 'Stakes YAK tokens',
            'method': '0xa694fc3a'
        },
        'unstakeYAK': {
            'direction': 'INCOMING',
            'description': 'Unstakes YAK tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
YIELD_YAK_FUNCTIONS = {
    'V1': YIELD_YAK_V1_FUNCTIONS
}