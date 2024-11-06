"""Celer Bridge Protocol Functions for all versions"""

CELER_V1_FUNCTIONS = {
    'BRIDGE': {
        'send': {
            'direction': 'OUTGOING',
            'description': 'Sends tokens across bridge',
            'method': '0x9b3d47b4'
        },
        'relay': {
            'direction': 'BOTH',
            'description': 'Relays bridge message',
            'method': '0x7c025200'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws bridged tokens',
            'method': '0x2e1a7d4d'
        },
        'refund': {
            'direction': 'INCOMING',
            'description': 'Refunds failed bridge',
            'method': '0x590e1ae3'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims bridge fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stakeCELR': {
            'direction': 'OUTGOING',
            'description': 'Stakes CELR tokens',
            'method': '0xa694fc3a'
        },
        'unstakeCELR': {
            'direction': 'INCOMING',
            'description': 'Unstakes CELR tokens',
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
CELER_FUNCTIONS = {
    'V1': CELER_V1_FUNCTIONS
}