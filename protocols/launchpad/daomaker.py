"""ICO/IDO Platform Functions for all versions"""

DAO_MAKER_V1_FUNCTIONS = {
    'DAO_MAKER': {
        'registerSHO': {
            'direction': 'OUTGOING',
            'description': 'Registers for Strong Holder Offering',
            'method': '0x1698ee82'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in SHO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims SHO tokens',
            'method': '0x4e71d92d'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes DAO tokens',
            'method': '0xa694fc3a'
        }
    }
}

# Combined functions for all versions
DAOMAKER_FUNCTIONS = {
    'V1': DAO_MAKER_V1_FUNCTIONS
}