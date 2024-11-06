"""Maple Finance Protocol Functions for all versions"""

MAPLE_V1_FUNCTIONS = {
    'LENDING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from pool',
            'method': '0x69328dec'
        },
        'drawdown': {
            'direction': 'INCOMING',
            'description': 'Draws down loan amount',
            'method': '0x9dc29fac'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays loan amount',
            'method': '0x573ade81'
        },
        'refinance': {
            'direction': 'BOTH',
            'description': 'Refinances existing loan',
            'method': '0x4ce38b5f'
        }
    },
    'POOL': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new lending pool',
            'method': '0x1698ee82'
        },
        'fundPool': {
            'direction': 'OUTGOING',
            'description': 'Funds existing pool',
            'method': '0xf48ab19f'
        },
        'closePool': {
            'direction': 'INCOMING',
            'description': 'Closes lending pool',
            'method': '0x4ce38b5f'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims pool fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes MPL tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes MPL tokens',
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
MAPLE_FUNCTIONS = {
    'V1': MAPLE_V1_FUNCTIONS
}