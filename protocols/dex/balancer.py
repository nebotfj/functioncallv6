"""Balancer Protocol Functions for all versions"""

BALANCER_V1_FUNCTIONS = {
    'SWAP': {
        'swapExactAmountIn': {
            'direction': 'BOTH',
            'description': 'Swaps exact amount of tokens in',
            'method': '0x8201aa3f'
        },
        'swapExactAmountOut': {
            'direction': 'BOTH',
            'description': 'Swaps for exact amount of tokens out',
            'method': '0x7c5e9ea4'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Executes batch of swaps',
            'method': '0x945bcec9'
        }
    },
    'LIQUIDITY': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0x4f69c0d4'
        },
        'exitPool': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0x8bdb3913'
        },
        'joinswapExternAmountIn': {
            'direction': 'OUTGOING',
            'description': 'Joins pool with exact token amount',
            'method': '0x5db34277'
        },
        'exitswapExternAmountOut': {
            'direction': 'INCOMING',
            'description': 'Exits pool for exact token amount',
            'method': '0x02c1a3b4'
        }
    }
}

BALANCER_V2_FUNCTIONS = {
    'VAULT': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Performs single swap',
            'method': '0x52bbbe29'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Performs multiple swaps',
            'method': '0x945bcec9'
        },
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xb95cac28'
        },
        'exitPool': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0x8bdb3913'
        },
        'flashLoan': {
            'direction': 'BOTH',
            'description': 'Executes flash loan',
            'method': '0x5c38449e'
        }
    },
    'WEIGHTED_POOL': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes weighted pool',
            'method': '0x4cd88b76'
        },
        'updateWeightsGradually': {
            'direction': 'OUTGOING',
            'description': 'Updates pool weights over time',
            'method': '0x0ba39ecd'
        },
        'updateSwapFee': {
            'direction': 'OUTGOING',
            'description': 'Updates pool swap fee',
            'method': '0x16b1c6d8'
        }
    },
    'STABLE_POOL': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes stable pool',
            'method': '0x4cd88b76'
        },
        'updateAmplificationParameter': {
            'direction': 'OUTGOING',
            'description': 'Updates amplification parameter',
            'method': '0x1a031c8c'
        }
    },
    'LIQUIDITY_MINING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes BPT tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes BPT tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims mining rewards',
            'method': '0x372500ab'
        }
    },
    'GOVERNANCE': {
        'createProposal': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0xf8572260'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
BALANCER_FUNCTIONS = {
    'V1': BALANCER_V1_FUNCTIONS,
    'V2': BALANCER_V2_FUNCTIONS
}