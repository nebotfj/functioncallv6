"""Drift Protocol Functions for all versions"""

DRIFT_V2_FUNCTIONS = {
    'TRADING': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new trading position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes existing position',
            'method': '0x82a08fcd'
        },
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies position parameters',
            'method': '0x0c49ccbe'
        },
        'placeTriggerOrder': {
            'direction': 'OUTGOING',
            'description': 'Places trigger/conditional order',
            'method': '0x52a9c8e6'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels pending order',
            'method': '0x2e1a7d4d'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stakeDRIFT': {
            'direction': 'OUTGOING',
            'description': 'Stakes DRIFT tokens',
            'method': '0xa694fc3a'
        },
        'unstakeDRIFT': {
            'direction': 'INCOMING',
            'description': 'Unstakes DRIFT tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'INSURANCE': {
        'depositInsurance': {
            'direction': 'OUTGOING',
            'description': 'Deposits to insurance fund',
            'method': '0x47e7ef24'
        },
        'withdrawInsurance': {
            'direction': 'INCOMING',
            'description': 'Withdraws from insurance fund',
            'method': '0x69328dec'
        },
        'claimInsurance': {
            'direction': 'INCOMING',
            'description': 'Claims insurance payout',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
DRIFT_FUNCTIONS = {
    'V2': DRIFT_V2_FUNCTIONS
}