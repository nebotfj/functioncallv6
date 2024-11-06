"""Frax Protocol Functions for all versions"""

FRAX_V1_FUNCTIONS = {
    'AMO': {
        'mintFrax': {
            'direction': 'OUTGOING',
            'description': 'Mints new FRAX tokens',
            'method': '0x40c10f19'
        },
        'burnFrax': {
            'direction': 'INCOMING',
            'description': 'Burns FRAX tokens',
            'method': '0x89afcb44'
        },
        'recollateralize': {
            'direction': 'OUTGOING',
            'description': 'Adds collateral to protocol',
            'method': '0x47e7ef24'
        },
        'buybackFrax': {
            'direction': 'OUTGOING',
            'description': 'Buys back FRAX from market',
            'method': '0x8a8c523c'
        }
    },
    'STAKING': {
        'stakeFxs': {
            'direction': 'OUTGOING',
            'description': 'Stakes FXS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeFxs': {
            'direction': 'INCOMING',
            'description': 'Unstakes FXS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'lockStake': {
            'direction': 'OUTGOING',
            'description': 'Locks staked tokens',
            'method': '0x3d18b912'
        },
        'withdrawLocked': {
            'direction': 'INCOMING',
            'description': 'Withdraws locked tokens',
            'method': '0x2e1a7d4d'
        }
    },
    'LENDING': {
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows FRAX tokens',
            'method': '0xc5ebeaec'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed FRAX',
            'method': '0x573ade81'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        },
        'addCollateral': {
            'direction': 'OUTGOING',
            'description': 'Adds collateral to position',
            'method': '0x47e7ef24'
        },
        'removeCollateral': {
            'direction': 'INCOMING',
            'description': 'Removes collateral from position',
            'method': '0x69328dec'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    }
}

# Combined functions for all versions
FRAX_FUNCTIONS = {
    'V1': FRAX_V1_FUNCTIONS
}