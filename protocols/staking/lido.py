"""Lido Protocol Functions for all versions"""

LIDO_V1_FUNCTIONS = {
    'STAKING': {
        'submit': {
            'direction': 'OUTGOING',
            'description': 'Submits ETH for staking',
            'method': '0xa1903eab'
        },
        'requestWithdrawals': {
            'direction': 'OUTGOING',
            'description': 'Requests withdrawal of staked ETH',
            'method': '0x0c49ccbe'
        },
        'claimWithdrawals': {
            'direction': 'INCOMING',
            'description': 'Claims requested withdrawals',
            'method': '0x4e71d92d'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x2e1a7d4d'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws staked assets',
            'method': '0x69328dec'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'distributeRewards': {
            'direction': 'INCOMING',
            'description': 'Distributes protocol rewards',
            'method': '0x7535d246'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims validator rewards',
            'method': '0x4e71d92d'
        }
    },
    'GOVERNANCE': {
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        },
        'proposeVote': {
            'direction': 'OUTGOING',
            'description': 'Creates new proposal',
            'method': '0xda95691a'
        },
        'executeVote': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
LIDO_FUNCTIONS = {
    'V1': LIDO_V1_FUNCTIONS
}