"""Pickle Finance Protocol Functions for all versions"""

PICKLE_V1_FUNCTIONS = {
    'FARM': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into farm',
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
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        }
    },
    'GAUGE': {
        'depositAll': {
            'direction': 'OUTGOING',
            'description': 'Deposits all tokens',
            'method': '0x3ccfd60b'
        },
        'withdrawAll': {
            'direction': 'INCOMING',
            'description': 'Withdraws all tokens',
            'method': '0x853828b6'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims gauge rewards',
            'method': '0x3d18b912'
        },
        'exit': {
            'direction': 'INCOMING',
            'description': 'Exits gauge position',
            'method': '0xe9fad8ee'
        }
    },
    'DILL': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes PICKLE tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes PICKLE tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims DILL rewards',
            'method': '0xe6f1daf2'
        },
        'lockPICKLE': {
            'direction': 'OUTGOING',
            'description': 'Locks PICKLE for DILL',
            'method': '0x3d18b912'
        }
    }
}

# Combined functions for all versions
PICKLE_FUNCTIONS = {
    'V1': PICKLE_V1_FUNCTIONS
}