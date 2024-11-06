"""CoW Swap Protocol Functions for all versions"""

COWSWAP_V1_FUNCTIONS = {
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
        'settleOrder': {
            'direction': 'BOTH',
            'description': 'Settles matched order',
            'method': '0x4ce38b5f'
        },
        'batchTrade': {
            'direction': 'BOTH',
            'description': 'Executes batch of trades',
            'method': '0x945bcec9'
        }
    },
    'SURPLUS': {
        'claimTraderSurplus': {
            'direction': 'INCOMING',
            'description': 'Claims trader price improvement',
            'method': '0x4e71d92d'
        },
        'claimSolverSurplus': {
            'direction': 'INCOMING',
            'description': 'Claims solver rewards',
            'method': '0xe6f1daf2'
        }
    },
    'SOLVER': {
        'registerSolver': {
            'direction': 'OUTGOING',
            'description': 'Registers as solver',
            'method': '0x1698ee82'
        },
        'submitSolution': {
            'direction': 'OUTGOING',
            'description': 'Submits settlement solution',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims solver rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
COWSWAP_FUNCTIONS = {
    'V1': COWSWAP_V1_FUNCTIONS
}