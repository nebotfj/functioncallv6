"""Vela Exchange Protocol Functions for all versions"""

VELA_V1_FUNCTIONS = {
    'TRADING': {
        'placeOrder': {
            'direction': 'OUTGOING',
            'description': 'Places new trading order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'executeOrder': {
            'direction': 'BOTH',
            'description': 'Executes ready order',
            'method': '0xbc61394a'
        },
        'updateOrder': {
            'direction': 'OUTGOING',
            'description': 'Updates order parameters',
            'method': '0x7535d246'
        },
        'claimFunding': {
            'direction': 'INCOMING',
            'description': 'Claims funding payments',
            'method': '0xd294f093'
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
        'stakeVELA': {
            'direction': 'OUTGOING',
            'description': 'Stakes VELA tokens',
            'method': '0xa694fc3a'
        },
        'unstakeVELA': {
            'direction': 'INCOMING',
            'description': 'Unstakes VELA tokens',
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
VELA_FUNCTIONS = {
    'V1': VELA_V1_FUNCTIONS
}