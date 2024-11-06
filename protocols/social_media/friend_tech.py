"""Friend.tech Protocol Functions for all versions"""

FRIEND_TECH_V1_FUNCTIONS = {
    'TRADING': {
        'buyShares': {
            'direction': 'OUTGOING',
            'description': 'Purchases user shares',
            'method': '0x6945b123'
        },
        'sellShares': {
            'direction': 'INCOMING',
            'description': 'Sells user shares',
            'method': '0x454a2ab3'
        },
        'getBuyPrice': {
            'direction': 'NEUTRAL',
            'description': 'Gets share buy price',
            'method': '0x9d2f32dd'
        },
        'getSellPrice': {
            'direction': 'NEUTRAL',
            'description': 'Gets share sell price',
            'method': '0x7535d246'
        }
    },
    'REWARDS': {
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims trading fees',
            'method': '0xd294f093'
        },
        'withdrawFees': {
            'direction': 'INCOMING',
            'description': 'Withdraws earned fees',
            'method': '0x69328dec'
        },
        'reinvestFees': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned fees',
            'method': '0xf69e2046'
        }
    },
    'SOCIAL': {
        'createProfile': {
            'direction': 'OUTGOING',
            'description': 'Creates user profile',
            'method': '0x1698ee82'
        },
        'updateProfile': {
            'direction': 'OUTGOING',
            'description': 'Updates profile info',
            'method': '0x7535d246'
        },
        'setUsername': {
            'direction': 'OUTGOING',
            'description': 'Sets profile username',
            'method': '0x3f7a5459'
        }
    },
    'MESSAGING': {
        'sendMessage': {
            'direction': 'OUTGOING',
            'description': 'Sends holder message',
            'method': '0x9b3d47b4'
        },
        'createGroup': {
            'direction': 'OUTGOING',
            'description': 'Creates holder group',
            'method': '0x1698ee82'
        }
    }
}

# Combined functions for all versions
FRIEND_TECH_FUNCTIONS = {
    'V1': FRIEND_TECH_V1_FUNCTIONS
}