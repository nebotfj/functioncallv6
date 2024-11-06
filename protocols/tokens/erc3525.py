"""ERC3525 Semi-Fungible Token Functions"""

ERC3525_V1_FUNCTIONS = {
    'BASIC': {
        'transferFrom': {
            'direction': 'OUTGOING',
            'description': 'Transfers token value',
            'method': '0x23b872dd'
        },
        'transferFromValue': {
            'direction': 'OUTGOING',
            'description': 'Transfers specific value',
            'method': '0xf7f855b9'
        },
        'approve': {
            'direction': 'OUTGOING',
            'description': 'Approves value transfer',
            'method': '0x095ea7b3'
        },
        'approveValue': {
            'direction': 'OUTGOING',
            'description': 'Approves specific value',
            'method': '0x1086a9af'
        }
    },
    'MINT': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new token',
            'method': '0x40c10f19'
        },
        'mintValue': {
            'direction': 'OUTGOING',
            'description': 'Mints token with value',
            'method': '0xf7f855b9'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns token',
            'method': '0x42966c68'
        },
        'burnValue': {
            'direction': 'OUTGOING',
            'description': 'Burns token value',
            'method': '0x0c46b72a'
        }
    },
    'METADATA': {
        'setMetadata': {
            'direction': 'OUTGOING',
            'description': 'Sets token metadata',
            'method': '0xcd1c0568'
        },
        'setSlotURI': {
            'direction': 'OUTGOING',
            'description': 'Sets slot URI',
            'method': '0x9fba176a'
        }
    }
}

# Combined functions for all versions
ERC3525_FUNCTIONS = {
    'V1': ERC3525_V1_FUNCTIONS
}