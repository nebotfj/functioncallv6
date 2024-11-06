"""Pirex Protocol Functions for all versions"""

PIREX_V1_FUNCTIONS = {
    'STAKING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets for staking',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws staked assets',
            'method': '0x69328dec'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'reinvest': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
        }
    },
    'AUTOCOMPOUNDING': {
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        },
        'harvestRewards': {
            'direction': 'INCOMING',
            'description': 'Harvests protocol rewards',
            'method': '0x4641257d'
        },
        'distributeYield': {
            'direction': 'OUTGOING',
            'description': 'Distributes yield to users',
            'method': '0x7535d246'
        }
    },
    'GOVERNANCE': {
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
PIREX_FUNCTIONS = {
    'V1': PIREX_V1_FUNCTIONS
}