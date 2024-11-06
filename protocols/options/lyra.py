"""Lyra Options Protocol Functions for all versions"""

LYRA_V1_FUNCTIONS = {
    'OPTIONS': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens option position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes option position',
            'method': '0x82a08fcd'
        },
        'exerciseOption': {
            'direction': 'BOTH',
            'description': 'Exercises option contract',
            'method': '0x7c025200'
        },
        'settleExpired': {
            'direction': 'INCOMING',
            'description': 'Settles expired option',
            'method': '0x4ce38b5f'
        },
        'adjustPosition': {
            'direction': 'BOTH',
            'description': 'Adjusts position parameters',
            'method': '0x0c49ccbe'
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
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims liquidity rewards',
            'method': '0xe6f1daf2'
        },
        'reinvestRewards': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
        }
    },
    'STAKING': {
        'stakeLYRA': {
            'direction': 'OUTGOING',
            'description': 'Stakes LYRA tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLYRA': {
            'direction': 'INCOMING',
            'description': 'Unstakes LYRA tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundStaking': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
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
LYRA_FUNCTIONS = {
    'V1': LYRA_V1_FUNCTIONS
}