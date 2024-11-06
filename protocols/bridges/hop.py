"""Hop Protocol Bridge Functions for all versions"""

HOP_V1_FUNCTIONS = {
    'BRIDGE': {
        'send': {
            'direction': 'OUTGOING',
            'description': 'Sends tokens across bridge',
            'method': '0x9b3d47b4'
        },
        'sendToL2': {
            'direction': 'OUTGOING',
            'description': 'Sends tokens to L2',
            'method': '0x7c025200'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws bridged tokens',
            'method': '0x2e1a7d4d'
        },
        'swapAndSend': {
            'direction': 'BOTH',
            'description': 'Swaps and bridges tokens',
            'method': '0x128acb08'
        },
        'bonderFee': {
            'direction': 'OUTGOING',
            'description': 'Pays bonder fee',
            'method': '0x4ce38b5f'
        }
    },
    'AMM': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge pool',
            'method': '0xbaa2abde'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps between bridge tokens',
            'method': '0x128acb08'
        }
    },
    'REWARDS': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes HOP tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes HOP tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

HOP_V2_FUNCTIONS = {
    'BRIDGE': {
        'send': {
            'direction': 'OUTGOING',
            'description': 'Sends tokens across bridge V2',
            'method': '0x9b3d47b4'
        },
        'sendToL2': {
            'direction': 'OUTGOING',
            'description': 'Sends tokens to L2 V2',
            'method': '0x7c025200'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws bridged tokens V2',
            'method': '0x2e1a7d4d'
        },
        'swapAndSend': {
            'direction': 'BOTH',
            'description': 'Swaps and bridges tokens V2',
            'method': '0x128acb08'
        },
        'fastWithdraw': {
            'direction': 'INCOMING',
            'description': 'Fast withdraws bridged tokens',
            'method': '0x2f4f5cc5'
        }
    },
    'AMM': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge pool V2',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge pool V2',
            'method': '0xbaa2abde'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps between bridge tokens V2',
            'method': '0x128acb08'
        },
        'flashLoan': {
            'direction': 'BOTH',
            'description': 'Executes flash loan',
            'method': '0x5cffe9de'
        }
    },
    'REWARDS': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes HOP tokens V2',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes HOP tokens V2',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards V2',
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
HOP_FUNCTIONS = {
    'V1': HOP_V1_FUNCTIONS,
    'V2': HOP_V2_FUNCTIONS
}