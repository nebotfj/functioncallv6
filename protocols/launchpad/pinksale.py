"""ICO/IDO Platform Functions for all versions"""

PINKSALE_V1_FUNCTIONS = {
    'PINKSALE': {
        'createPresale': {
            'direction': 'OUTGOING',
            'description': 'Creates presale pool',
            'method': '0x1698ee82'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in presale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims presale tokens',
            'method': '0x4e71d92d'
        },
        'finalize': {
            'direction': 'OUTGOING',
            'description': 'Finalizes successful presale',
            'method': '0x4ce38b5f'
        },
        'cancelPool': {
            'direction': 'BOTH',
            'description': 'Cancels presale pool',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
PINKSALE_FUNCTIONS = {
    'V1': PINKSALE_V1_FUNCTIONS
}