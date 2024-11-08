"""ICO/IDO Platform Functions for all versions"""

COINLIST_V1_FUNCTIONS = {
    'COINLIST': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in token sale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims purchased tokens',
            'method': '0x4e71d92d'
        },
        'register': {
            'direction': 'OUTGOING',
            'description': 'Registers for sale whitelist',
            'method': '0x1698ee82'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from sale',
            'method': '0x69328dec'
        }
    }
}

# Combined functions for all versions
COINLIST_FUNCTIONS = {
    'V1': COINLIST_V1_FUNCTIONS
}