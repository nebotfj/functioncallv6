"""Decentral Games Protocol Functions for all versions"""

DECENTRAL_V1_FUNCTIONS = {
    'CASINO': {
        'placeBet': {
            'direction': 'OUTGOING',
            'description': 'Places casino bet',
            'method': '0x8f38249c'
        },
        'claimWinnings': {
            'direction': 'INCOMING',
            'description': 'Claims bet winnings',
            'method': '0x4e71d92d'
        },
        'buyChips': {
            'direction': 'OUTGOING',
            'description': 'Purchases casino chips',
            'method': '0x94b576de'
        },
        'sellChips': {
            'direction': 'INCOMING',
            'description': 'Sells casino chips',
            'method': '0x454a2ab3'
        },
        'joinTable': {
            'direction': 'OUTGOING',
            'description': 'Joins casino table',
            'method': '0x9b3d47b4'
        },
        'leaveTable': {
            'direction': 'INCOMING',
            'description': 'Leaves casino table',
            'method': '0x2e1a7d4d'
        }
    },
    'POKER': {
        'startGame': {
            'direction': 'OUTGOING',
            'description': 'Starts poker game',
            'method': '0x1698ee82'
        },
        'placeBet': {
            'direction': 'OUTGOING',
            'description': 'Places poker bet',
            'method': '0x8f38249c'
        },
        'fold': {
            'direction': 'OUTGOING',
            'description': 'Folds poker hand',
            'method': '0x2e1a7d4d'
        },
        'call': {
            'direction': 'OUTGOING',
            'description': 'Calls current bet',
            'method': '0x9b3d47b4'
        },
        'raise': {
            'direction': 'OUTGOING',
            'description': 'Raises current bet',
            'method': '0x7535d246'
        },
        'showHand': {
            'direction': 'NEUTRAL',
            'description': 'Shows poker hand',
            'method': '0x9d2f32dd'
        }
    },
    'STAKING': {
        'stakeICE': {
            'direction': 'OUTGOING',
            'description': 'Stakes ICE tokens',
            'method': '0xa694fc3a'
        },
        'unstakeICE': {
            'direction': 'INCOMING',
            'description': 'Unstakes ICE tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
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
DECENTRAL_FUNCTIONS = {
    'V1': DECENTRAL_V1_FUNCTIONS
}