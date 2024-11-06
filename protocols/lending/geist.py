"""Geist Finance Protocol Functions for all versions"""

GEIST_V1_FUNCTIONS = {
    'LENDING': {
        'supply': {
            'direction': 'OUTGOING',
            'description': 'Supplies assets to protocol',
            'method': '0x617ba037'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws supplied assets',
            'method': '0x69328dec'
        },
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows assets from protocol',
            'method': '0xc5ebeaec'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed assets',
            'method': '0x573ade81'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        }
    },
    'STAKING': {
        'stakeGEIST': {
            'direction': 'OUTGOING',
            'description': 'Stakes GEIST tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGEIST': {
            'direction': 'INCOMING',
            'description': 'Unstakes GEIST tokens',
            'method': '0x2e1a7d4d'
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
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'VESTING': {
        'lock': {
            'direction': 'OUTGOING',
            'description': 'Locks tokens for vesting',
            'method': '0x3d18b912'
        },
        'unlock': {
            'direction': 'INCOMING',
            'description': 'Unlocks vested tokens',
            'method': '0x2e1a7d4d'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims vested tokens',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
GEIST_FUNCTIONS = {
    'V1': GEIST_V1_FUNCTIONS
}