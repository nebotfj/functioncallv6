"""Orbiter Finance Bridge Functions for all versions"""

ORBITER_V1_FUNCTIONS = {
    'BRIDGE': {
        'bridge': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens across chains',
            'method': '0x8b9e4f93'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws bridged tokens',
            'method': '0x2e1a7d4d'
        },
        'bridgeETH': {
            'direction': 'OUTGOING',
            'description': 'Bridges ETH across chains',
            'method': '0xb1a1a882'
        },
        'bridgeTokens': {
            'direction': 'OUTGOING',
            'description': 'Bridges specific tokens',
            'method': '0x8b9e4f93'
        }
    },
    'MAKER': {
        'provideLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Provides bridge liquidity',
            'method': '0xe8e33700'
        },
        'withdrawLiquidity': {
            'direction': 'INCOMING',
            'description': 'Withdraws bridge liquidity',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims maker fees',
            'method': '0xd294f093'
        }
    }
}

# Combined functions for all versions
ORBITER_FUNCTIONS = {
    'V1': ORBITER_V1_FUNCTIONS
}