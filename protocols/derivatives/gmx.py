"""GMX Protocol Functions for all versions"""

GMX_V2_FUNCTIONS = {
    'TRADING': {
        'createOrder': {
            'direction': 'OUTGOING',
            'description': 'Creates new trading order',
            'method': '0x6c1aaf13'
        },
        'updateOrder': {
            'direction': 'OUTGOING',
            'description': 'Updates existing order',
            'method': '0x7535d246'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels pending order',
            'method': '0x2e1a7d4d'
        },
        'executeOrder': {
            'direction': 'BOTH',
            'description': 'Executes ready order',
            'method': '0xbc61394a'
        },
        'claimFunding': {
            'direction': 'INCOMING',
            'description': 'Claims funding payments',
            'method': '0xd294f093'
        }
    },
    'LIQUIDITY': {
        'createDeposit': {
            'direction': 'OUTGOING',
            'description': 'Creates deposit request',
            'method': '0x47e7ef24'
        },
        'cancelDeposit': {
            'direction': 'OUTGOING',
            'description': 'Cancels pending deposit',
            'method': '0x2e1a7d4d'
        },
        'executeDeposit': {
            'direction': 'OUTGOING',
            'description': 'Executes deposit request',
            'method': '0x47e7ef24'
        },
        'createWithdrawal': {
            'direction': 'OUTGOING',
            'description': 'Creates withdrawal request',
            'method': '0x69328dec'
        },
        'executeWithdrawal': {
            'direction': 'INCOMING',
            'description': 'Executes withdrawal request',
            'method': '0x69328dec'
        }
    },
    'REWARDS': {
        'claimableReward': {
            'direction': 'NEUTRAL',
            'description': 'Checks claimable rewards',
            'method': '0x33039b29'
        },
        'claimReward': {
            'direction': 'INCOMING',
            'description': 'Claims earned rewards',
            'method': '0xe6f1daf2'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        },
        'handleRewards': {
            'direction': 'BOTH',
            'description': 'Processes reward distribution',
            'method': '0x5c19a95c'
        }
    }
}

# Combined functions for all versions
GMX_FUNCTIONS = {
    'V2': GMX_V2_FUNCTIONS
}