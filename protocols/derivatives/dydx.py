"""dYdX Protocol Functions for all versions"""

DYDX_V3_FUNCTIONS = {
    'PERPETUALS': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens perpetual position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes perpetual position',
            'method': '0x82a08fcd'
        },
        'modifyPosition': {
            'direction': 'BOTH',
            'description': 'Modifies position parameters',
            'method': '0x0c49ccbe'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        },
        'withdrawPnl': {
            'direction': 'INCOMING',
            'description': 'Withdraws realized PnL',
            'method': '0x69328dec'
        }
    },
    'MARGIN': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits collateral',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws collateral',
            'method': '0x69328dec'
        },
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows from margin pool',
            'method': '0xc858f5ba'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays margin loan',
            'method': '0x573ade81'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates margin position',
            'method': '0x96cd4ddb'
        }
    },
    'ORDERS': {
        'placeOrder': {
            'direction': 'OUTGOING',
            'description': 'Places new order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'fillOrder': {
            'direction': 'BOTH',
            'description': 'Fills matching order',
            'method': '0xbc61394a'
        },
        'placeStopOrder': {
            'direction': 'OUTGOING',
            'description': 'Places stop loss order',
            'method': '0x52a9c8e6'
        },
        'placeTakeProfitOrder': {
            'direction': 'OUTGOING',
            'description': 'Places take profit order',
            'method': '0x94b576de'
        }
    },
    'STAKING': {
        'stakeDYDX': {
            'direction': 'OUTGOING',
            'description': 'Stakes DYDX tokens',
            'method': '0xa694fc3a'
        },
        'unstakeDYDX': {
            'direction': 'INCOMING',
            'description': 'Unstakes DYDX tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'delegateStake': {
            'direction': 'OUTGOING',
            'description': 'Delegates staking power',
            'method': '0x5c19a95c'
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
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
DYDX_FUNCTIONS = {
    'V3': DYDX_V3_FUNCTIONS
}