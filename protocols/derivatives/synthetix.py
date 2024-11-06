"""Synthetix Protocol Functions for all versions"""

SYNTHETIX_V2_FUNCTIONS = {
    'TRADING': {
        'exchange': {
            'direction': 'BOTH',
            'description': 'Exchanges synths directly',
            'method': '0x128acb08'
        },
        'exchangeWithTracking': {
            'direction': 'BOTH',
            'description': 'Exchanges with fee tracking',
            'method': '0x30d54d8f'
        },
        'exchangeWithVirtual': {
            'direction': 'BOTH',
            'description': 'Exchanges with virtual synths',
            'method': '0x0e30a9cf'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes SNX tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes SNX tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints sUSD with SNX',
            'method': '0x40c10f19'
        },
        'burn': {
            'direction': 'INCOMING',
            'description': 'Burns sUSD for SNX',
            'method': '0x89afcb44'
        }
    },
    'COLLATERAL': {
        'addCollateral': {
            'direction': 'OUTGOING',
            'description': 'Adds SNX collateral',
            'method': '0x47e7ef24'
        },
        'removeCollateral': {
            'direction': 'INCOMING',
            'description': 'Removes SNX collateral',
            'method': '0x69328dec'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        }
    }
}

# Combined functions for all versions
SYNTHETIX_FUNCTIONS = {
    'V2': SYNTHETIX_V2_FUNCTIONS
}