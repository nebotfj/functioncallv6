"""ICO/IDO Platform Functions for all versions"""

POLKASTARTER_V1_FUNCTIONS = {
    'POLKASTARTER': {
        'whitelist': {
            'direction': 'OUTGOING',
            'description': 'Joins sale whitelist',
            'method': '0x9b3d47b4'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in IDO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims IDO tokens',
            'method': '0x4e71d92d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal',
            'method': '0x5312ea8e'
        }
    }
}

# Combined functions for all versions
POLKASTARTER_FUNCTIONS = {
    'V1': POLKASTARTER_V1_FUNCTIONS
}