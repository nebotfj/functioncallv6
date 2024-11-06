"""Wallfair Protocol Functions for all versions"""

WALLFAIR_V1_FUNCTIONS = {
    'BETTING': {
        'createEvent': {
            'direction': 'OUTGOING',
            'description': 'Creates betting event',
            'method': '0x1698ee82'
        },
        'placeBet': {
            'direction': 'OUTGOING',
            'description': 'Places bet on event',
            'method': '0x8f38249c'
        },
        'claimReward': {
            'direction': 'INCOMING',
            'description': 'Claims betting rewards',
            'method': '0x4e71d92d'
        },
        'cancelBet': {
            'direction': 'INCOMING',
            'description': 'Cancels active bet',
            'method': '0x2e1a7d4d'
        }
    },
    'STAKING': {
        'stakeWFAIR': {
            'direction': 'OUTGOING',
            'description': 'Stakes WFAIR tokens',
            'method': '0xa694fc3a'
        },
        'unstakeWFAIR': {
            'direction': 'INCOMING',
            'description': 'Unstakes WFAIR tokens',
            'method': '0x2e1a7d4d'
        },
        'harvestRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x4641257d'
        }
    },
    'GOVERNANCE': {
        'createProposal': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'executeProposal': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
WALLFAIR_FUNCTIONS = {
    'V1': WALLFAIR_V1_FUNCTIONS
}