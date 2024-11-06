"""Iron Bank Protocol Functions for all versions"""

IRONBANK_V1_FUNCTIONS = {
    'LENDING': {
        'supply': {
            'direction': 'OUTGOING',
            'description': 'Supplies assets to protocol',
            'method': '0x617ba037'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws supplied assets',
            'method': '0x69328dec'
        },
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows assets from protocol',
            'method': '0xc5ebeaec'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed assets',
            'method': '0x573ade81'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        }
    },
    'MARKETS': {
        'enterMarkets': {
            'direction': 'OUTGOING',
            'description': 'Enters markets as collateral',
            'method': '0xc2998238'
        },
        'exitMarket': {
            'direction': 'INCOMING',
            'description': 'Exits market',
            'method': '0xede4edd0'
        },
        'updateInterest': {
            'direction': 'NEUTRAL',
            'description': 'Updates market interest rates',
            'method': '0x6c540baf'
        }
    },
    'COLLATERAL': {
        'postCollateral': {
            'direction': 'OUTGOING',
            'description': 'Posts collateral to protocol',
            'method': '0x47e7ef24'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws posted collateral',
            'method': '0x69328dec'
        },
        'seizeCollateral': {
            'direction': 'BOTH',
            'description': 'Seizes collateral in liquidation',
            'method': '0x96cd4ddb'
        }
    }
}

# Combined functions for all versions
IRONBANK_FUNCTIONS = {
    'V1': IRONBANK_V1_FUNCTIONS
}