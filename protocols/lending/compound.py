"""Compound Protocol Functions for all versions"""

COMPOUND_FUNCTIONS = {
    'V2': {
        'LENDING': {
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Mints cTokens by supplying assets',
                'method': '0xa0712d68'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems cTokens for assets',
                'method': '0xdb006a75'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets',
                'method': '0xc5ebeaec'
            },
            'repayBorrow': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets',
                'method': '0x0e752702'
            },
            'liquidateBorrow': {
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
        },
        'GOVERNANCE': {
            'propose': {
                'direction': 'OUTGOING',
                'description': 'Creates proposal',
                'method': '0xda95691a'
            },
            'castVote': {
                'direction': 'OUTGOING',
                'description': 'Votes on proposal',
                'method': '0x56781388'
            }
        }
    },
    'V3': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to protocol',
                'method': '0x4b8a3529'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets',
                'method': '0x0babd745'
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
        }
    }
}