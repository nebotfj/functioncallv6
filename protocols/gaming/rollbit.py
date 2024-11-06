"""Rollbit Protocol Functions for all versions"""

ROLLBIT_V1_FUNCTIONS = {
    'CASINO': {
        'spin': {
            'direction': 'OUTGOING',
            'description': 'Spins casino game',
            'method': '0x8f38249c'
        },
        'placeBet': {
            'direction': 'OUTGOING',
            'description': 'Places casino bet',
            'method': '0x9d2f32dd'
        },
        'claimWinnings': {
            'direction': 'INCOMING',
            'description': 'Claims casino winnings',
            'method': '0x4e71d92d'
        },
        'buyCredits': {
            'direction': 'OUTGOING',
            'description': 'Purchases casino credits',
            'method': '0x94b576de'
        },
        'withdrawCredits': {
            'direction': 'INCOMING',
            'description': 'Withdraws casino credits',
            'method': '0x69328dec'
        }
    },
    'TRADING': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens trading position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes trading position',
            'method': '0x82a08fcd'
        },
        'addMargin': {
            'direction': 'OUTGOING',
            'description': 'Adds position margin',
            'method': '0x47e7ef24'
        },
        'removeMargin': {
            'direction': 'INCOMING',
            'description': 'Removes position margin',
            'method': '0x69328dec'
        }
    },
    'STAKING': {
        'stakeRLB': {
            'direction': 'OUTGOING',
            'description': 'Stakes RLB tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRLB': {
            'direction': 'INCOMING',
            'description': 'Unstakes RLB tokens',
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
ROLLBIT_FUNCTIONS = {
    'V1': ROLLBIT_V1_FUNCTIONS
}