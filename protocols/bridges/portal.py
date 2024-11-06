"""Portal (Wormhole) Bridge Functions for all versions"""

PORTAL_V2_FUNCTIONS = {
    'BRIDGE': {
        'transferTokens': {
            'direction': 'OUTGOING',
            'description': 'Transfers tokens across chains',
            'method': '0x8b9e4f93'
        },
        'completeTransfer': {
            'direction': 'INCOMING',
            'description': 'Completes token transfer',
            'method': '0x4ce38b5f'
        },
        'transferNFT': {
            'direction': 'OUTGOING',
            'description': 'Transfers NFT across chains',
            'method': '0x96cd4ddb'
        },
        'redeemNFT': {
            'direction': 'INCOMING',
            'description': 'Redeems bridged NFT',
            'method': '0x4c4a82f8'
        }
    },
    'GOVERNANCE': {
        'registerChain': {
            'direction': 'OUTGOING',
            'description': 'Registers new chain',
            'method': '0x3a088cd2'
        },
        'upgradeContract': {
            'direction': 'OUTGOING',
            'description': 'Upgrades contract implementation',
            'method': '0x99a88ec4'
        },
        'setGuardian': {
            'direction': 'OUTGOING',
            'description': 'Sets guardian address',
            'method': '0x8a742e9c'
        }
    },
    'RELAYER': {
        'submitVAA': {
            'direction': 'OUTGOING',
            'description': 'Submits verified action approval',
            'method': '0x9b3d47b4'
        },
        'redeemOnEth': {
            'direction': 'INCOMING',
            'description': 'Redeems on Ethereum',
            'method': '0x7c025200'
        },
        'createWrapped': {
            'direction': 'OUTGOING',
            'description': 'Creates wrapped token',
            'method': '0x1698ee82'
        }
    }
}

# Combined functions for all versions
PORTAL_FUNCTIONS = {
    'V2': PORTAL_V2_FUNCTIONS
}