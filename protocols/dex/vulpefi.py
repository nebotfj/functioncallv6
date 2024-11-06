"""VulpeFi Protocol Functions for all versions"""

VULPEFI_V1_FUNCTIONS = {
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        },
        'limitOrder': {
            'direction': 'OUTGOING',
            'description': 'Places limit order',
            'method': '0x94b576de'
        },
        'marketOrder': {
            'direction': 'BOTH',
            'description': 'Places market order',
            'method': '0x7c025200'
        },
        'batchSwap': {
            'direction': 'BOTH',
            'description': 'Executes multiple swaps',
            'method': '0x945bcec9'
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
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        }
    },
    'YIELD': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets for yield',
            'method': '0xb6b55f25'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws yielded assets',
            'method': '0x2e1a7d4d'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Claims yield rewards',
            'method': '0x4641257d'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds yield rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
VULPEFI_FUNCTIONS = {
    'V1': VULPEFI_V1_FUNCTIONS
}