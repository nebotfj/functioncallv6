"""Optimism Bridge Protocol Functions for all versions"""

OPTIMISM_V1_FUNCTIONS = {
    'BRIDGE': {
        'depositTransaction': {
            'direction': 'OUTGOING',
            'description': 'Deposits transaction to L2',
            'method': '0xb1a1a882'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from L2',
            'method': '0x2e1a7d4d'
        },
        'proveWithdrawal': {
            'direction': 'BOTH',
            'description': 'Proves withdrawal validity',
            'method': '0x7c025200'
        },
        'finalizeWithdrawal': {
            'direction': 'INCOMING',
            'description': 'Finalizes proven withdrawal',
            'method': '0x4ce38b5f'
        }
    },
    'L1_CROSS_DOMAIN': {
        'sendMessage': {
            'direction': 'OUTGOING',
            'description': 'Sends message to L2',
            'method': '0x9b3d47b4'
        },
        'relayMessage': {
            'direction': 'BOTH',
            'description': 'Relays message between layers',
            'method': '0x7c025200'
        },
        'replayMessage': {
            'direction': 'OUTGOING',
            'description': 'Replays failed message',
            'method': '0x2f4f5cc5'
        }
    },
    'GATEWAY': {
        'depositERC20': {
            'direction': 'OUTGOING',
            'description': 'Deposits ERC20 to L2',
            'method': '0x8b9e4f93'
        },
        'withdrawERC20': {
            'direction': 'INCOMING',
            'description': 'Withdraws ERC20 from L2',
            'method': '0x32b7006d'
        },
        'finalizeERC20Withdrawal': {
            'direction': 'INCOMING',
            'description': 'Finalizes ERC20 withdrawal',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
OPTIMISM_FUNCTIONS = {
    'V1': OPTIMISM_V1_FUNCTIONS
}