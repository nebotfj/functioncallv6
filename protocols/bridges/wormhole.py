"""Wormhole Protocol Functions for all versions"""

WORMHOLE_V2_FUNCTIONS = {
    'BRIDGE': {
        'transferTokens': {
            'direction': 'OUTGOING',
            'description': 'Transfers tokens across chains',
            'method': '0x8b9e4f93'
        },
        'completeTransfer': {
            'direction': 'INCOMING',
            'description': 'Completes cross-chain transfer',
            'method': '0x4ce38b5f'
        },
        'attestToken': {
            'direction': 'OUTGOING',
            'description': 'Attests token for bridging',
            'method': '0x3a088cd2'
        },
        'createWrapped': {
            'direction': 'OUTGOING',
            'description': 'Creates wrapped token version',
            'method': '0x1698ee82'
        }
    },
    'MESSAGING': {
        'publishMessage': {
            'direction': 'OUTGOING',
            'description': 'Publishes cross-chain message',
            'method': '0x9b3d47b4'
        },
        'receiveMessage': {
            'direction': 'INCOMING',
            'description': 'Receives cross-chain message',
            'method': '0x7c025200'
        },
        'verifyMessage': {
            'direction': 'NEUTRAL',
            'description': 'Verifies message validity',
            'method': '0x7535d246'
        }
    },
    'NFT': {
        'transferNFT': {
            'direction': 'OUTGOING',
            'description': 'Transfers NFT across chains',
            'method': '0x96cd4ddb'
        },
        'completeNFTTransfer': {
            'direction': 'INCOMING',
            'description': 'Completes NFT transfer',
            'method': '0x4c4a82f8'
        },
        'createWrappedNFT': {
            'direction': 'OUTGOING',
            'description': 'Creates wrapped NFT version',
            'method': '0x88316456'
        }
    },
    'GOVERNANCE': {
        'submitProposal': {
            'direction': 'OUTGOING',
            'description': 'Submits governance proposal',
            'method': '0xda95691a'
        },
        'executeProposal': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        },
        'upgradeContract': {
            'direction': 'OUTGOING',
            'description': 'Upgrades contract implementation',
            'method': '0x99a88ec4'
        }
    }
}

# Combined functions for all versions
WORMHOLE_FUNCTIONS = {
    'V2': WORMHOLE_V2_FUNCTIONS
}