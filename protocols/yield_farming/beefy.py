"""Beefy Finance Protocol Functions for all versions"""

BEEFY_V1_FUNCTIONS = {
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'depositAll': {
            'direction': 'OUTGOING',
            'description': 'Deposits all available assets',
            'method': '0x3ccfd60b'
        },
        'withdrawAll': {
            'direction': 'INCOMING',
            'description': 'Withdraws all deposited assets',
            'method': '0x853828b6'
        },
        'getPricePerFullShare': {
            'direction': 'NEUTRAL',
            'description': 'Gets vault share price',
            'method': '0x77c7b8fc'
        }
    },
    'BOOST': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes BIFI tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes BIFI tokens',
            'method': '0x2e1a7d4d'
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
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims boost rewards',
            'method': '0xe6f1daf2'
        }
    },
    'ZAPS': {
        'beefIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps tokens into vault',
            'method': '0x6d914547'
        },
        'beefOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of vault',
            'method': '0x0c2d3f2b'
        },
        'beefInETH': {
            'direction': 'OUTGOING',
            'description': 'Zaps ETH into vault',
            'method': '0x29b3d8f1'
        },
        'beefOutETH': {
            'direction': 'INCOMING',
            'description': 'Zaps vault to ETH',
            'method': '0x4c8d8528'
        }
    }
}

# Combined functions for all versions
BEEFY_FUNCTIONS = {
    'V1': BEEFY_V1_FUNCTIONS
}