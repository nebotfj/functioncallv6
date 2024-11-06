"""Cream Finance Protocol Functions for all versions"""

CREAM_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Mints crTokens',
                'method': '0xa0712d68'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems underlying tokens',
                'method': '0xdb006a75'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets',
                'method': '0x0e752702'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates position',
                'method': '0xf5e3c462'
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
            }
        }
    }
}