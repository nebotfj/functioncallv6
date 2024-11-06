"""Farcaster Protocol Functions for all versions"""

FARCASTER_V1_FUNCTIONS = {
    'SOCIAL': {
        'cast': {
            'direction': 'OUTGOING',
            'description': 'Creates new cast message',
            'method': '0x1698ee82'
        },
        'recast': {
            'direction': 'OUTGOING',
            'description': 'Recasts existing message',
            'method': '0x9b3d47b4'
        },
        'reply': {
            'direction': 'OUTGOING',
            'description': 'Replies to cast',
            'method': '0x7535d246'
        },
        'like': {
            'direction': 'OUTGOING',
            'description': 'Likes cast message',
            'method': '0x2f4f5cc5'
        },
        'unlike': {
            'direction': 'OUTGOING',
            'description': 'Removes cast like',
            'method': '0x5f7b8feb'
        }
    },
    'PROFILE': {
        'register': {
            'direction': 'OUTGOING',
            'description': 'Registers new FID',
            'method': '0x1698ee82'
        },
        'updateProfile': {
            'direction': 'OUTGOING',
            'description': 'Updates profile metadata',
            'method': '0x7535d246'
        },
        'follow': {
            'direction': 'OUTGOING',
            'description': 'Follows user FID',
            'method': '0x5c19a95c'
        },
        'unfollow': {
            'direction': 'OUTGOING',
            'description': 'Unfollows user FID',
            'method': '0x2e1a7d4d'
        }
    },
    'STORAGE': {
        'addStorage': {
            'direction': 'OUTGOING',
            'description': 'Adds storage provider',
            'method': '0x47e7ef24'
        },
        'removeStorage': {
            'direction': 'OUTGOING',
            'description': 'Removes storage provider',
            'method': '0x69328dec'
        },
        'updateStorage': {
            'direction': 'OUTGOING',
            'description': 'Updates storage settings',
            'method': '0x7535d246'
        }
    },
    'VERIFICATION': {
        'verifyAddress': {
            'direction': 'OUTGOING',
            'description': 'Verifies Ethereum address',
            'method': '0x9d2f32dd'
        },
        'removeVerification': {
            'direction': 'OUTGOING',
            'description': 'Removes address verification',
            'method': '0x5f7b8feb'
        }
    }
}

# Combined functions for all versions
FARCASTER_FUNCTIONS = {
    'V1': FARCASTER_V1_FUNCTIONS
}