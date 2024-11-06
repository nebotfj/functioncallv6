"""Convex Finance Protocol Functions for all versions"""

CONVEX_V1_FUNCTIONS = {
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes CVX tokens',
            'method': '0xa694fc3a'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws staked tokens',
            'method': '0x69328dec'
        },
        'getReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x3d18b912'
        },
        'stakeAll': {
            'direction': 'OUTGOING',
            'description': 'Stakes all available tokens',
            'method': '0x3ccfd60b'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims pool rewards',
            'method': '0xe6f1daf2'
        },
        'claimableRewards': {
            'direction': 'NEUTRAL',
            'description': 'Checks claimable rewards',
            'method': '0x33039b29'
        },
        'earmarkRewards': {
            'direction': 'OUTGOING',
            'description': 'Earmarks pool rewards',
            'method': '0x7535d246'
        }
    },
    'BOOSTER': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits LP tokens',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws LP tokens',
            'method': '0x69328dec'
        },
        'withdrawAll': {
            'direction': 'INCOMING',
            'description': 'Withdraws all LP tokens',
            'method': '0x853828b6'
        },
        'depositAll': {
            'direction': 'OUTGOING',
            'description': 'Deposits all LP tokens',
            'method': '0x3ccfd60b'
        }
    },
    'LOCKER': {
        'lock': {
            'direction': 'OUTGOING',
            'description': 'Locks CVX tokens',
            'method': '0x3d18b912'
        },
        'processExpiredLocks': {
            'direction': 'INCOMING',
            'description': 'Processes expired locks',
            'method': '0x4ce38b5f'
        },
        'processExpiredLocksWithdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws expired locks',
            'method': '0x69328dec'
        }
    }
}

# Combined functions for all versions
CONVEX_FUNCTIONS = {
    'V1': CONVEX_V1_FUNCTIONS
}