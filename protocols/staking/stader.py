"""Stader Protocol Functions for all versions"""

STADER_V1_FUNCTIONS = {
    'STAKING': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits ETH for staking',
            'method': '0x47e7ef24'
        },
        'requestWithdrawal': {
            'direction': 'OUTGOING',
            'description': 'Requests withdrawal of stake',
            'method': '0x0c49ccbe'
        },
        'claimWithdrawal': {
            'direction': 'INCOMING',
            'description': 'Claims requested withdrawal',
            'method': '0x4e71d92d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'VALIDATOR': {
        'registerValidator': {
            'direction': 'OUTGOING',
            'description': 'Registers new validator',
            'method': '0x1698ee82'
        },
        'exitValidator': {
            'direction': 'OUTGOING',
            'description': 'Exits validator from network',
            'method': '0x2e1a7d4d'
        },
        'claimValidatorRewards': {
            'direction': 'INCOMING',
            'description': 'Claims validator rewards',
            'method': '0x4e71d92d'
        }
    },
    'PERMISSIONLESS': {
        'createPermissionlessNode': {
            'direction': 'OUTGOING',
            'description': 'Creates permissionless node',
            'method': '0x1698ee82'
        },
        'operateNode': {
            'direction': 'OUTGOING',
            'description': 'Operates validator node',
            'method': '0x7535d246'
        },
        'claimNodeRewards': {
            'direction': 'INCOMING',
            'description': 'Claims node operation rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
STADER_FUNCTIONS = {
    'V1': STADER_V1_FUNCTIONS
}