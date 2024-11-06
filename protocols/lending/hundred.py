"""Hundred Finance Protocol Functions for all versions"""

HUNDRED_V1_FUNCTIONS = {
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
        'claimHND': {
            'direction': 'INCOMING',
            'description': 'Claims HND rewards',
            'method': '0xe6f1daf2'
        }
    },
    'STAKING': {
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'lockHND': {
            'direction': 'OUTGOING',
            'description': 'Locks HND tokens',
            'method': '0x3d18b912'
        }
    }
}

# Combined functions for all versions
HUNDRED_FUNCTIONS = {
    'V1': HUNDRED_V1_FUNCTIONS
}