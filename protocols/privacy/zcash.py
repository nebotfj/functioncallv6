"""Zcash Bridge Protocol Functions for all versions"""

ZCASH_BRIDGE_V1_FUNCTIONS = {
    'BRIDGE': {
        'bridgeToZcash': {
            'direction': 'OUTGOING',
            'description': 'Bridges to Zcash chain',
            'method': '0x8b9e4f93'
        },
        'bridgeFromZcash': {
            'direction': 'INCOMING',
            'description': 'Bridges from Zcash chain',
            'method': '0x4ce38b5f'
        },
        'generateZkProof': {
            'direction': 'NEUTRAL',
            'description': 'Generates zk-SNARK proof',
            'method': '0x9b3d47b4'
        },
        'verifyZkProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies zk-SNARK proof',
            'method': '0x7535d246'
        }
    },
    'SHIELDED': {
        'shieldedTransfer': {
            'direction': 'BOTH',
            'description': 'Executes shielded transfer',
            'method': '0x23b872dd'
        },
        'shieldedMint': {
            'direction': 'OUTGOING',
            'description': 'Mints shielded tokens',
            'method': '0x40c10f19'
        },
        'shieldedBurn': {
            'direction': 'OUTGOING',
            'description': 'Burns shielded tokens',
            'method': '0x42966c68'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds bridge liquidity',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes bridge liquidity',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims bridge fees',
            'method': '0xd294f093'
        }
    }
}

# Combined functions for all versions
ZCASH_BRIDGE_FUNCTIONS = {
    'V1': ZCASH_BRIDGE_V1_FUNCTIONS
}