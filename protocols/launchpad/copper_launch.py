"""ICO/IDO Platform Functions for all versions"""

COPPER_LAUNCH_V1_FUNCTIONS = {
    'COPPER_LAUNCH': {
        'createAuction': {
            'direction': 'OUTGOING',
            'description': 'Creates token auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims won tokens',
            'method': '0x4e71d92d'
        },
        'withdrawUnsuccessful': {
            'direction': 'INCOMING',
            'description': 'Withdraws unsuccessful bid',
            'method': '0x69328dec'
        }
    }
}

# Combined functions for all versions
COPPER_LAUNCH_FUNCTIONS = {
    'V1': COPPER_LAUNCH_V1_FUNCTIONS
}