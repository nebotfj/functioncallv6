"""Maverick Protocol Functions for all versions"""

MAVERICK_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
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
        'addLiquidityBinning': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with binning',
            'method': '0x9b3d47b4'
        },
        'removeLiquidityBinning': {
            'direction': 'INCOMING',
            'description': 'Removes binned liquidity',
            'method': '0x5312ea8e'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

MAVERICK_V2_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
        },
        'flashSwap': {
            'direction': 'BOTH',
            'description': 'Executes flash swap',
            'method': '0x490e6cbc'
        },
        'dynamicSwap': {
            'direction': 'BOTH',
            'description': 'Executes dynamic routing swap',
            'method': '0x2b67b570'
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
        'addLiquidityBinning': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with binning',
            'method': '0x9b3d47b4'
        },
        'removeLiquidityBinning': {
            'direction': 'INCOMING',
            'description': 'Removes binned liquidity',
            'method': '0x5312ea8e'
        },
        'migrateLiquidity': {
            'direction': 'BOTH',
            'description': 'Migrates liquidity between pools',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens',
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
MAVERICK_FUNCTIONS = {
    'V1': MAVERICK_V1_FUNCTIONS,
    'V2': MAVERICK_V2_FUNCTIONS
}