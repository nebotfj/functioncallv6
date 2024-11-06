"""StakeStone Protocol Functions for all versions"""

STAKESTONE_V1_FUNCTIONS = {
    'STAKING': {
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
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        },
        'requestWithdrawal': {
            'direction': 'OUTGOING',
            'description': 'Requests withdrawal',
            'method': '0x0c49ccbe'
        },
        'claimWithdrawal': {
            'direction': 'INCOMING',
            'description': 'Claims requested withdrawal',
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
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    },
    'POOL': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Joins liquidity pool',
            'method': '0xb95cac28'
        },
        'exitPool': {
            'direction': 'INCOMING',
            'description': 'Exits liquidity pool',
            'method': '0x8bdb3913'
        },
        'swapPoolTokens': {
            'direction': 'BOTH',
            'description': 'Swaps pool tokens',
            'method': '0x128acb08'
        }
    }
}

# Combined functions for all versions
STAKESTONE_FUNCTIONS = {
    'V1': STAKESTONE_V1_FUNCTIONS
}