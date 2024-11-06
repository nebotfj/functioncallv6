"""Jones DAO Protocol Functions for all versions"""

JONES_DAO_V1_FUNCTIONS = {
    'VAULTS': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Harvests vault rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds vault rewards',
            'method': '0xf69e2046'
        }
    },
    'OPTIONS': {
        'buyOption': {
            'direction': 'OUTGOING',
            'description': 'Purchases option contract',
            'method': '0x8f38249c'
        },
        'sellOption': {
            'direction': 'INCOMING',
            'description': 'Sells option contract',
            'method': '0x454a2ab3'
        },
        'exercise': {
            'direction': 'BOTH',
            'description': 'Exercises option contract',
            'method': '0x7c025200'
        },
        'settle': {
            'direction': 'INCOMING',
            'description': 'Settles expired option',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stakeJONES': {
            'direction': 'OUTGOING',
            'description': 'Stakes JONES tokens',
            'method': '0xa694fc3a'
        },
        'unstakeJONES': {
            'direction': 'INCOMING',
            'description': 'Unstakes JONES tokens',
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
JONES_DAO_FUNCTIONS = {
    'V1': JONES_DAO_V1_FUNCTIONS
}