"""Dopex Options Protocol Functions for all versions"""

DOPEX_V1_FUNCTIONS = {
    'OPTIONS': {
        'purchaseOption': {
            'direction': 'OUTGOING',
            'description': 'Purchases option contract',
            'method': '0x8f38249c'
        },
        'exerciseOption': {
            'direction': 'BOTH',
            'description': 'Exercises option contract',
            'method': '0x7c025200'
        },
        'sellOption': {
            'direction': 'INCOMING',
            'description': 'Sells option position',
            'method': '0x454a2ab3'
        },
        'settleOption': {
            'direction': 'INCOMING',
            'description': 'Settles expired option',
            'method': '0x4ce38b5f'
        }
    },
    'SSOV': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into SSOV vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from SSOV vault',
            'method': '0x69328dec'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims SSOV rewards',
            'method': '0xe6f1daf2'
        },
        'rollPosition': {
            'direction': 'BOTH',
            'description': 'Rolls vault position',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stakeDPX': {
            'direction': 'OUTGOING',
            'description': 'Stakes DPX tokens',
            'method': '0xa694fc3a'
        },
        'unstakeDPX': {
            'direction': 'INCOMING',
            'description': 'Unstakes DPX tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
DOPEX_FUNCTIONS = {
    'V1': DOPEX_V1_FUNCTIONS
}