"""Venus Protocol Functions for all versions"""

VENUS_V1_FUNCTIONS = {
    'LENDING': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints vTokens by supplying assets',
            'method': '0x40c10f19'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems vTokens for assets',
            'method': '0xdb006a75'
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
        'updateVenusSupplyIndex': {
            'direction': 'OUTGOING',
            'description': 'Updates supply index',
            'method': '0x7535d246'
        },
        'updateVenusBorrowIndex': {
            'direction': 'OUTGOING',
            'description': 'Updates borrow index',
            'method': '0x2f4f5cc5'
        }
    },
    'REWARDS': {
        'claimVenus': {
            'direction': 'INCOMING',
            'description': 'Claims XVS rewards',
            'method': '0xe6f1daf2'
        },
        'claimVenusAsCollateral': {
            'direction': 'INCOMING',
            'description': 'Claims XVS rewards as collateral',
            'method': '0x4e71d92d'
        },
        'distributeSupplierVenus': {
            'direction': 'INCOMING',
            'description': 'Distributes supplier rewards',
            'method': '0x9a5c32e7'
        },
        'distributeBorrowerVenus': {
            'direction': 'INCOMING',
            'description': 'Distributes borrower rewards',
            'method': '0x6d34b96e'
        }
    }
}

# Combined functions for all versions
VENUS_FUNCTIONS = {
    'V1': VENUS_V1_FUNCTIONS
}