"""Euler Finance Protocol Functions for all versions"""

EULER_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'deposit': {
                'direction': 'OUTGOING',
                'description': 'Deposits assets',
                'method': '0x6e553f65'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws assets',
                'method': '0x69328dec'
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
            }
        },
        'MARKETS': {
            'enterMarket': {
                'direction': 'OUTGOING',
                'description': 'Enters market',
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