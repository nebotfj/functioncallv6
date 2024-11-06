"""Bancor Protocol Functions for all versions"""

BANCOR_V2_FUNCTIONS = {
    'TRADING': {
        'convertByPath': {
            'direction': 'BOTH',
            'description': 'Converts tokens through conversion path',
            'method': '0xb77d239b'
        },
        'convert': {
            'direction': 'BOTH',
            'description': 'Converts between tokens directly',
            'method': '0x0f5a5466'
        },
        'rateByPath': {
            'direction': 'NEUTRAL',
            'description': 'Gets conversion rate for path',
            'method': '0x95e2c065'
        },
        'completeXConversion': {
            'direction': 'BOTH',
            'description': 'Completes cross-chain conversion',
            'method': '0x89f9aab7'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds single-sided liquidity',
            'method': '0x0b4c7e4d'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0x32f6e3a8'
        },
        'addLiquidityFor': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity on behalf of another address',
            'method': '0x82241490'
        },
        'fundPool': {
            'direction': 'OUTGOING',
            'description': 'Funds pool with initial liquidity',
            'method': '0xf48ab19f'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims liquidity mining rewards',
            'method': '0xe6f1daf2'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes BNT in the protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes BNT from protocol',
            'method': '0x2e1a7d4d'
        },
        'restake': {
            'direction': 'OUTGOING',
            'description': 'Restakes rewards back into protocol',
            'method': '0x7b24a5fd'
        }
    }
}

BANCOR_V3_FUNCTIONS = {
    'TRADING': {
        'trade': {
            'direction': 'BOTH',
            'description': 'Executes token trade',
            'method': '0x2e26065c'
        },
        'tradeBySourceAmount': {
            'direction': 'BOTH',
            'description': 'Trades exact source token amount',
            'method': '0x9da1b973'
        },
        'tradeByTargetAmount': {
            'direction': 'BOTH',
            'description': 'Trades for exact target token amount',
            'method': '0x07f68fcd'
        },
        'completeXConversion': {
            'direction': 'BOTH',
            'description': 'Completes cross-chain conversion V3',
            'method': '0x89f9aab7'
        }
    },
    'LIQUIDITY': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens into pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws tokens from pool',
            'method': '0x441a3e70'
        },
        'depositFor': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens for another address',
            'method': '0x2929abe7'
        },
        'withdrawFor': {
            'direction': 'INCOMING',
            'description': 'Withdraws tokens for another address',
            'method': '0x9e281a98'
        },
        'fundPool': {
            'direction': 'OUTGOING',
            'description': 'Funds pool with initial liquidity V3',
            'method': '0xf48ab19f'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims trading rewards',
            'method': '0xe6f1daf2'
        },
        'claimPendingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims pending rewards for pool',
            'method': '0x44adc90e'
        }
    },
    'POOL_MANAGEMENT': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new trading pool',
            'method': '0x1698ee82'
        },
        'enableTrading': {
            'direction': 'OUTGOING',
            'description': 'Enables trading in pool',
            'method': '0x8a8c523c'
        },
        'activatePool': {
            'direction': 'OUTGOING',
            'description': 'Activates pool for trading',
            'method': '0x67118c24'
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
BANCOR_FUNCTIONS = {
    'V2': BANCOR_V2_FUNCTIONS,
    'V3': BANCOR_V3_FUNCTIONS
}