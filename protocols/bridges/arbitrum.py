"""Arbitrum Bridge Protocol Functions for all versions"""

ARBITRUM_V1_FUNCTIONS = {
    'BRIDGE': {
        'sendMessage': {
            'direction': 'OUTGOING',
            'description': 'Sends message to L2',
            'method': '0x9b3d47b4'
        },
        'requestL2Transaction': {
            'direction': 'OUTGOING',
            'description': 'Requests L2 transaction execution',
            'method': '0x7c025200'
        },
        'finalizeWithdrawal': {
            'direction': 'INCOMING',
            'description': 'Finalizes L2 to L1 withdrawal',
            'method': '0x4ce38b5f'
        },
        'depositETH': {
            'direction': 'OUTGOING',
            'description': 'Deposits ETH to L2',
            'method': '0xb1a1a882'
        },
        'withdrawETH': {
            'direction': 'INCOMING',
            'description': 'Withdraws ETH from L2',
            'method': '0x2e1a7d4d'
        }
    },
    'RETRYABLE': {
        'createRetryableTicket': {
            'direction': 'OUTGOING',
            'description': 'Creates retryable ticket',
            'method': '0x679b6ded'
        },
        'redeem': {
            'direction': 'BOTH',
            'description': 'Redeems retryable ticket',
            'method': '0xdb006a75'
        },
        'cancel': {
            'direction': 'OUTGOING',
            'description': 'Cancels retryable ticket',
            'method': '0x2e1a7d4d'
        }
    },
    'GATEWAY': {
        'outboundTransfer': {
            'direction': 'OUTGOING',
            'description': 'Initiates token transfer to L2',
            'method': '0x8b9e4f93'
        },
        'finalizeInboundTransfer': {
            'direction': 'INCOMING',
            'description': 'Finalizes token transfer from L2',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
ARBITRUM_FUNCTIONS = {
    'V1': ARBITRUM_V1_FUNCTIONS
}