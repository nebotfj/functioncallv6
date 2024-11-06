"""Hegic Options Protocol Functions for all versions"""

HEGIC_V1_FUNCTIONS = {
    'OPTIONS': {
        'createOption': {
            'direction': 'OUTGOING',
            'description': 'Creates new option',
            'method': '0x1698ee82'
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
    'LIQUIDITY': {
        'provideLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Provides pool liquidity',
            'method': '0xe8e33700'
        },
        'withdrawLiquidity': {
            'direction': 'INCOMING',
            'description': 'Withdraws pool liquidity',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims liquidity fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stakeHEGIC': {
            'direction': 'OUTGOING',
            'description': 'Stakes HEGIC tokens',
            'method': '0xa694fc3a'
        },
        'unstakeHEGIC': {
            'direction': 'INCOMING',
            'description': 'Unstakes HEGIC tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
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
HEGIC_FUNCTIONS = {
    'V1': HEGIC_V1_FUNCTIONS
}