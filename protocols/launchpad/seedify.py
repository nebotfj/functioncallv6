"""ICO/IDO Platform Functions for all versions"""

SEEDIFY_V1_FUNCTIONS = {
    'SEEDIFY': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes SFUND tokens',
            'method': '0xa694fc3a'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in IGO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims IGO tokens',
            'method': '0x4e71d92d'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes SFUND tokens',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
SEEDIFY_FUNCTIONS = {
    'V1': SEEDIFY_V1_FUNCTIONS
}