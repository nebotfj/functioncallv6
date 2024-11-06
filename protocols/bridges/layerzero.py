"""LayerZero Protocol Functions for all versions"""

LAYERZERO_V1_FUNCTIONS = {
    'BRIDGE': {
        'send': {
            'direction': 'OUTGOING',
            'description': 'Sends message across chains',
            'method': '0x9b3d47b4'
        },
        'receive': {
            'direction': 'INCOMING',
            'description': 'Receives cross-chain message',
            'method': '0x7c025200'
        },
        'estimateFees': {
            'direction': 'NEUTRAL',
            'description': 'Estimates bridge fees',
            'method': '0x9d2f32dd'
        },
        'validateTransactionProof': {
            'direction': 'NEUTRAL',
            'description': 'Validates transaction proof',
            'method': '0x7535d246'
        }
    },
    'MESSAGING': {
        'sendMessage': {
            'direction': 'OUTGOING',
            'description': 'Sends arbitrary message',
            'method': '0x9b3d47b4'
        },
        'receiveMessage': {
            'direction': 'INCOMING',
            'description': 'Receives arbitrary message',
            'method': '0x7c025200'
        },
        'retryMessage': {
            'direction': 'OUTGOING',
            'description': 'Retries failed message',
            'method': '0x2f4f5cc5'
        },
        'clearMessage': {
            'direction': 'OUTGOING',
            'description': 'Clears stuck message',
            'method': '0x4ce38b5f'
        }
    },
    'RELAYER': {
        'registerRelayer': {
            'direction': 'OUTGOING',
            'description': 'Registers new relayer',
            'method': '0x3a088cd2'
        },
        'removeRelayer': {
            'direction': 'OUTGOING',
            'description': 'Removes existing relayer',
            'method': '0x5f7b8feb'
        },
        'setRelayerFees': {
            'direction': 'OUTGOING',
            'description': 'Sets relayer fee parameters',
            'method': '0xe74b981b'
        }
    }
}

# Combined functions for all versions
LAYERZERO_FUNCTIONS = {
    'V1': LAYERZERO_V1_FUNCTIONS
}