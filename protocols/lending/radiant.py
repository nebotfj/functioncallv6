"""Radiant Capital Protocol Functions for all versions"""

RADIANT_V1_FUNCTIONS = {
    'LENDING': {
        'supply': {
            'direction': 'OUTGOING',
            'description': 'Supplies assets to protocol',
            'method': '0x617ba037'
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
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws supplied assets',
            'method': '0x69328dec'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        }
    },
    'STAKING': {
        'stakeRDNT': {
            'direction': 'OUTGOING',
            'description': 'Stakes RDNT tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRDNT': {
            'direction': 'INCOMING',
            'description': 'Unstakes RDNT tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'lockRDNT': {
            'direction': 'OUTGOING',
            'description': 'Locks RDNT tokens',
            'method': '0x3d18b912'
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
        }
    }
}

# Combined functions for all versions
RADIANT_FUNCTIONS = {
    'V1': RADIANT_V1_FUNCTIONS
}