"""ERC20 Token Protocol Functions"""

ERC20_V1_FUNCTIONS = {
    'BASIC': {
        'transfer': {
            'direction': 'OUTGOING',
            'description': 'Transfers tokens to address',
            'method': '0xa9059cbb'
        },
        'transferFrom': {
            'direction': 'OUTGOING',
            'description': 'Transfers tokens from address',
            'method': '0x23b872dd'
        },
        'approve': {
            'direction': 'OUTGOING',
            'description': 'Approves token allowance',
            'method': '0x095ea7b3'
        },
        'increaseAllowance': {
            'direction': 'OUTGOING',
            'description': 'Increases token allowance',
            'method': '0x39509351'
        },
        'decreaseAllowance': {
            'direction': 'OUTGOING',
            'description': 'Decreases token allowance',
            'method': '0xa457c2d7'
        }
    },
    'MINT': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new tokens',
            'method': '0x40c10f19'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns existing tokens',
            'method': '0x42966c68'
        },
        'burnFrom': {
            'direction': 'OUTGOING',
            'description': 'Burns tokens from address',
            'method': '0x79cc6790'
        }
    },
    'PERMIT': {
        'permit': {
            'direction': 'OUTGOING',
            'description': 'Approves via signature',
            'method': '0xd505accf'
        },
        'nonces': {
            'direction': 'NEUTRAL',
            'description': 'Gets permit nonce',
            'method': '0x7ecebe00'
        },
        'DOMAIN_SEPARATOR': {
            'direction': 'NEUTRAL',
            'description': 'Gets domain separator',
            'method': '0x3644e515'
        }
    },
    'CONTROL': {
        'pause': {
            'direction': 'OUTGOING',
            'description': 'Pauses token transfers',
            'method': '0x8456cb59'
        },
        'unpause': {
            'direction': 'OUTGOING',
            'description': 'Unpauses token transfers',
            'method': '0x3f4ba83a'
        },
        'blacklist': {
            'direction': 'OUTGOING',
            'description': 'Blacklists address',
            'method': '0xf9f92be4'
        },
        'unblacklist': {
            'direction': 'OUTGOING',
            'description': 'Removes address from blacklist',
            'method': '0x1a895266'
        }
    }
}

# Combined functions for all versions
ERC20_FUNCTIONS = {
    'V1': ERC20_V1_FUNCTIONS
}