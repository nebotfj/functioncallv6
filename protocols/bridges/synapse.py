"""Synapse Protocol Functions for all versions"""

SYNAPSE_V1_FUNCTIONS = {
    'BRIDGE': {
        'bridge': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens to another chain',
            'method': '0x8b9e4f93'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems bridged tokens',
            'method': '0xdb006a75'
        },
        'swapAndBridge': {
            'direction': 'BOTH',
            'description': 'Swaps and bridges tokens',
            'method': '0x128acb08'
        },
        'bridgeAndSwap': {
            'direction': 'BOTH',
            'description': 'Bridges and swaps tokens',
            'method': '0x7c025200'
        }
    },
    'POOLS': {
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
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps between pool tokens',
            'method': '0x128acb08'
        },
        'flashLoan': {
            'direction': 'BOTH',
            'description': 'Executes flash loan',
            'method': '0x5cffe9de'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes SYN tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes SYN tokens',
            'method': '0x2e1a7d4d'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x4641257d'
        }
    }
}

# Combined functions for all versions
SYNAPSE_FUNCTIONS = {
    'V1': SYNAPSE_V1_FUNCTIONS
}