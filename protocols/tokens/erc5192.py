"""ERC5192 Minimal Soulbound NFTs Functions"""

ERC5192_V1_FUNCTIONS = {
    'SOULBOUND': {
        'lock': {
            'direction': 'OUTGOING',
            'description': 'Locks token transfer',
            'method': '0xdd467064'
        },
        'unlock': {
            'direction': 'OUTGOING',
            'description': 'Unlocks token transfer',
            'method': '0xa69df4b5'
        },
        'locked': {
            'direction': 'NEUTRAL',
            'description': 'Checks if token is locked',
            'method': '0xcf309012'
        }
    },
    'MINT': {
        'soulMint': {
            'direction': 'OUTGOING',
            'description': 'Mints soulbound token',
            'method': '0x40c10f19'
        },
        'soulBurn': {
            'direction': 'OUTGOING',
            'description': 'Burns soulbound token',
            'method': '0x42966c68'
        }
    }
}

# Combined functions for all versions
ERC5192_FUNCTIONS = {
    'V1': ERC5192_V1_FUNCTIONS
}