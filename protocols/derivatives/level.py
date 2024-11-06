"""Level Finance Protocol Functions for all versions"""

LEVEL_V1_FUNCTIONS = {
    'TRADING': {
        'openPosition': {
            'direction': 'OUTGOING',
            'description': 'Opens new trading position',
            'method': '0x969b0e0c'
        },
        'closePosition': {
            'direction': 'INCOMING',
            'description': 'Closes existing position',
            'method': '0x82a08fcd'
        },
        'increasePosition': {
            'direction': 'OUTGOING',
            'description': 'Increases position size',
            'method': '0x219f5d17'
        },
        'decreasePosition': {
            'direction': 'INCOMING',
            'description': 'Decreases position size',
            'method': '0x0c49ccbe'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stakeLVL': {
            'direction': 'OUTGOING',
            'description': 'Stakes LVL tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLVL': {
            'direction': 'INCOMING',
            'description': 'Unstakes LVL tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
LEVEL_FUNCTIONS = {
    'V1': LEVEL_V1_FUNCTIONS
}