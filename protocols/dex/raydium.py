"""Raydium Protocol Functions for all versions"""

RAYDIUM_V3_FUNCTIONS = {
    'SWAP': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'routeSwap': {
            'direction': 'BOTH',
            'description': 'Executes routed swap',
            'method': '0x7c025200'
        },
        'swapBaseIn': {
            'direction': 'BOTH',
            'description': 'Swaps exact input amount',
            'method': '0x9d2f32dd'
        },
        'swapBaseOut': {
            'direction': 'BOTH',
            'description': 'Swaps for exact output amount',
            'method': '0x7c025200'
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
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new liquidity pool',
            'method': '0x1698ee82'
        },
        'closePool': {
            'direction': 'OUTGOING',
            'description': 'Closes existing pool',
            'method': '0x4ce38b5f'
        }
    },
    'FARMING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xe2bbb158'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x441a3e70'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal from farm',
            'method': '0x5312ea8e'
        }
    },
    'STAKING': {
        'stakeRAY': {
            'direction': 'OUTGOING',
            'description': 'Stakes RAY tokens',
            'method': '0xa694fc3a'
        },
        'unstakeRAY': {
            'direction': 'INCOMING',
            'description': 'Unstakes RAY tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
RAYDIUM_FUNCTIONS = {
    'V3': RAYDIUM_V3_FUNCTIONS
}