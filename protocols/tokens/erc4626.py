"""ERC4626 Tokenized Vault Protocol Functions"""

ERC4626_V1_FUNCTIONS = {
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0x6e553f65'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints vault shares',
            'method': '0x40c10f19'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x2e1a7d4d'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems vault shares',
            'method': '0xdb006a75'
        }
    },
    'CONVERSION': {
        'convertToShares': {
            'direction': 'NEUTRAL',
            'description': 'Converts assets to shares',
            'method': '0x7162a8c4'
        },
        'convertToAssets': {
            'direction': 'NEUTRAL',
            'description': 'Converts shares to assets',
            'method': '0x07a2d13a'
        },
        'previewDeposit': {
            'direction': 'NEUTRAL',
            'description': 'Simulates deposit',
            'method': '0xef8b30f7'
        },
        'previewMint': {
            'direction': 'NEUTRAL',
            'description': 'Simulates mint',
            'method': '0xb3d7f6b9'
        },
        'previewWithdraw': {
            'direction': 'NEUTRAL',
            'description': 'Simulates withdrawal',
            'method': '0x0a28a477'
        },
        'previewRedeem': {
            'direction': 'NEUTRAL',
            'description': 'Simulates redemption',
            'method': '0x4cdad506'
        }
    },
    'LIMITS': {
        'maxDeposit': {
            'direction': 'NEUTRAL',
            'description': 'Gets max deposit amount',
            'method': '0x402d267d'
        },
        'maxMint': {
            'direction': 'NEUTRAL',
            'description': 'Gets max mint amount',
            'method': '0xc63d75b6'
        },
        'maxWithdraw': {
            'direction': 'NEUTRAL',
            'description': 'Gets max withdrawal amount',
            'method': '0xce96cb77'
        },
        'maxRedeem': {
            'direction': 'NEUTRAL',
            'description': 'Gets max redemption amount',
            'method': '0xd905777e'
        }
    }
}

# Combined functions for all versions
ERC4626_FUNCTIONS = {
    'V1': ERC4626_V1_FUNCTIONS
}