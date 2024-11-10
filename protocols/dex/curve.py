"""Curve Protocol Functions for all versions"""

CURVE_V1_FUNCTIONS = {
    'POOL': {
        'add_liquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0x0b4c7e4d'
        },
        'remove_liquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity proportionally',
            'method': '0x5b36389c'
        },
        'remove_liquidity_one_coin': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity in single token',
            'method': '0x1a4d01d2'
        },
        'exchange': {
            'direction': 'BOTH',
            'description': 'Swaps between tokens in pool',
            'method': '0x3df02124'
        },
        'exchange_underlying': {
            'direction': 'BOTH',
            'description': 'Swaps between underlying tokens',
            'method': '0xa6417ed6'
        },
        'exchange_multiple': {
            'direction': 'OUTGOING',
            'description': 'Performs multiple token swaps in a single transaction',
            'method': '0x353ca424'
        }
    },
    'GAUGE': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens in gauge',
            'method': '0xb6b55f25'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws LP tokens from gauge',
            'method': '0x2e1a7d4d'
        },
        'claim_rewards': {
            'direction': 'INCOMING',
            'description': 'Claims gauge rewards',
            'method': '0xe6f1daf2'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints CRV tokens',
            'method': '0x40c10f19'
        },
        'mint_many': {
            'direction': 'OUTGOING',
            'description': 'Mints CRV tokens for multiple gauges',
            'method': '0x13c36c92'
        },
        'user_checkpoint': {
            'direction': 'NEUTRAL',
            'description': 'Update user rewards checkpoint',
            'method': '0x4b820093',
            #'protocol': ['Curve', 'Convex']
        }
    }
}

CURVE_V2_FUNCTIONS = {
    'POOL': {
        'add_liquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0x0b4c7e4d'
        },
        'remove_liquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0x5b36389c'
        },
        'exchange': {
            'direction': 'BOTH',
            'description': 'Swaps between tokens in pool',
            'method': '0x3df02124'
        },
        'exchange_underlying': {
            'direction': 'BOTH',
            'description': 'Swaps between underlying tokens',
            'method': '0xa6417ed6'
        },
        'add_liquidity_one_coin': {
            'direction': 'OUTGOING',
            'description': 'Adds single token liquidity',
            'method': '0x9f69b6d1'
        },
        'remove_liquidity_one_coin': {
            'direction': 'INCOMING',
            'description': 'Removes single token liquidity',
            'method': '0x1a4d01d2'
        }
    },
    'TRICRYPTO': {
        'exchange': {
            'direction': 'BOTH',
            'description': 'Swaps in tricrypto pool',
            'method': '0x3df02124'
        },
        'exchange_underlying': {
            'direction': 'BOTH',
            'description': 'Swaps underlying in tricrypto',
            'method': '0xa6417ed6'
        },
        'add_liquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to tricrypto',
            'method': '0x0b4c7e4d'
        },
        'remove_liquidity_one_coin': {
            'direction': 'INCOMING',
            'description': 'Removes single token from tricrypto',
            'method': '0x1a4d01d2'
        }
    },
    'FACTORY': {
        'deploy_pool': {
            'direction': 'OUTGOING',
            'description': 'Deploys new pool',
            'method': '0x6623fc46'
        },
        'deploy_metapool': {
            'direction': 'OUTGOING',
            'description': 'Deploys new metapool',
            'method': '0x9d2c1b1f'
        },
        'set_fee_receiver': {
            'direction': 'OUTGOING',
            'description': 'Sets fee receiver address',
            'method': '0xe74b981b'
        }
    }
}

CURVE_COMMON_FUNCTIONS = {
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes CRV tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes CRV tokens',
            'method': '0x2e1a7d4d'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x4e71d92d'
        },
        'vote_for_gauge_weights': {
            'direction': 'OUTGOING',
            'description': 'Votes for gauge weights',
            'method': '0x6d46e987'
        },
        'deposit_reward_token': {
            'direction': 'OUTGOING',
            'description': 'Deposits reward token',
            'method': '0x3f6bc68b'
        },
        'create_lock': {
            'direction': 'OUTGOING',
            'description': 'Lock tokens for voting rights',
            'method': '0x65fc3873',
            'protocol': ['Curve veCRV']
        },
        'increase_amount': {
            'direction': 'OUTGOING',
            'description': 'Increase locked amount',
            'method': '0x5ef8f675',
            'protocol': ['Curve veCRV']
        },
        'increase_unlock_time': {
            'direction': 'OUTGOING',
            'description': 'Extend lock duration',
            'method': '0xc27f24d2',
            'protocol': ['Curve veCRV']
        },
    }
}

# Combined functions for all versions
CURVE_FUNCTIONS = {
    'V1': CURVE_V1_FUNCTIONS,
    'V2': CURVE_V2_FUNCTIONS,
    'COMMON': CURVE_COMMON_FUNCTIONS
}