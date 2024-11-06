"""RocketPool Protocol Functions for all versions"""

ROCKETPOOL_V1_FUNCTIONS = {
    'NODE': {
        'registerNode': {
            'direction': 'OUTGOING',
            'description': 'Registers new node',
            'method': '0x1698ee82'
        },
        'depositNode': {
            'direction': 'OUTGOING',
            'description': 'Deposits ETH to node',
            'method': '0x47e7ef24'
        },
        'stakeRPL': {
            'direction': 'OUTGOING',
            'description': 'Stakes RPL tokens',
            'method': '0xa694fc3a'
        },
        'withdrawRPL': {
            'direction': 'INCOMING',
            'description': 'Withdraws staked RPL',
            'method': '0x69328dec'
        }
    },
    'MINIPOOL': {
        'createMinipool': {
            'direction': 'OUTGOING',
            'description': 'Creates new minipool',
            'method': '0x1698ee82'
        },
        'stakeMinipool': {
            'direction': 'OUTGOING',
            'description': 'Stakes ETH in minipool',
            'method': '0xa694fc3a'
        },
        'withdrawMinipool': {
            'direction': 'INCOMING',
            'description': 'Withdraws from minipool',
            'method': '0x69328dec'
        },
        'closeMinipool': {
            'direction': 'BOTH',
            'description': 'Closes existing minipool',
            'method': '0x4ce38b5f'
        }
    },
    'REWARDS': {
        'claimNodeRewards': {
            'direction': 'INCOMING',
            'description': 'Claims node rewards',
            'method': '0xe6f1daf2'
        },
        'claimRPLRewards': {
            'direction': 'INCOMING',
            'description': 'Claims RPL rewards',
            'method': '0x4e71d92d'
        },
        'distributeRewards': {
            'direction': 'OUTGOING',
            'description': 'Distributes rewards',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
ROCKETPOOL_FUNCTIONS = {
    'V1': ROCKETPOOL_V1_FUNCTIONS
}