"""Flashbots Protocol Functions for all versions"""

FLASHBOTS_V1_FUNCTIONS = {
    'BUNDLE': {
        'sendBundle': {
            'direction': 'OUTGOING',
            'description': 'Sends transaction bundle',
            'method': '0x7535d246'
        },
        'cancelBundle': {
            'direction': 'OUTGOING',
            'description': 'Cancels pending bundle',
            'method': '0x2e1a7d4d'
        },
        'simulateBundle': {
            'direction': 'NEUTRAL',
            'description': 'Simulates bundle execution',
            'method': '0x9d2f32dd'
        }
    },
    'BUILDER': {
        'registerBuilder': {
            'direction': 'OUTGOING',
            'description': 'Registers as block builder',
            'method': '0x1698ee82'
        },
        'submitBlock': {
            'direction': 'OUTGOING',
            'description': 'Submits built block',
            'method': '0x7535d246'
        },
        'updateBuilderPreferences': {
            'direction': 'OUTGOING',
            'description': 'Updates builder settings',
            'method': '0x4ce38b5f'
        }
    },
    'PROTECTION': {
        'enableFrontrunProtection': {
            'direction': 'OUTGOING',
            'description': 'Enables MEV protection',
            'method': '0x3a088cd2'
        },
        'disableProtection': {
            'direction': 'OUTGOING',
            'description': 'Disables MEV protection',
            'method': '0x5f7b8feb'
        }
    },
    'REWARDS': {
        'claimBuilderRewards': {
            'direction': 'INCOMING',
            'description': 'Claims builder rewards',
            'method': '0x4e71d92d'
        },
        'distributeRewards': {
            'direction': 'OUTGOING',
            'description': 'Distributes MEV rewards',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
FLASHBOTS_FUNCTIONS = {
    'V1': FLASHBOTS_V1_FUNCTIONS
}