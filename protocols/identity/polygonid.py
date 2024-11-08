"""Polygon ID Protocol Functions for all versions"""

POLYGON_ID_V1_FUNCTIONS = {
    'IDENTITY': {
        'createIdentity': {
            'direction': 'OUTGOING',
            'description': 'Creates new identity',
            'method': '0x1698ee82'
        },
        'updateIdentity': {
            'direction': 'OUTGOING',
            'description': 'Updates identity information',
            'method': '0x7535d246'
        },
        'revokeIdentity': {
            'direction': 'OUTGOING',
            'description': 'Revokes existing identity',
            'method': '0x2e1a7d4d'
        },
        'verifyCredential': {
            'direction': 'NEUTRAL',
            'description': 'Verifies identity credential',
            'method': '0x9d2f32dd'
        }
    },
    'CLAIMS': {
        'issueClaim': {
            'direction': 'OUTGOING',
            'description': 'Issues new claim',
            'method': '0x3a088cd2'
        },
        'revokeClaim': {
            'direction': 'OUTGOING',
            'description': 'Revokes existing claim',
            'method': '0x5f7b8feb'
        },
        'verifyClaim': {
            'direction': 'NEUTRAL',
            'description': 'Verifies claim validity',
            'method': '0x7535d246'
        }
    },
    'SCHEMAS': {
        'createSchema': {
            'direction': 'OUTGOING',
            'description': 'Creates new schema',
            'method': '0x1698ee82'
        },
        'updateSchema': {
            'direction': 'OUTGOING',
            'description': 'Updates schema definition',
            'method': '0x7535d246'
        },
        'validateSchema': {
            'direction': 'NEUTRAL',
            'description': 'Validates schema format',
            'method': '0x9d2f32dd'
        }
    },
    'STATE': {
        'updateState': {
            'direction': 'OUTGOING',
            'description': 'Updates identity state',
            'method': '0x2f4f5cc5'
        },
        'transitionState': {
            'direction': 'OUTGOING',
            'description': 'Transitions identity state',
            'method': '0x4ce38b5f'
        },
        'verifyState': {
            'direction': 'NEUTRAL',
            'description': 'Verifies identity state',
            'method': '0x7535d246'
        }
    },
    'PROOF': {
        'generateProof': {
            'direction': 'OUTGOING',
            'description': 'Generates zero-knowledge proof',
            'method': '0x9b3d47b4'
        },
        'verifyProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies zero-knowledge proof',
            'method': '0x7c025200'
        },
        'revokeProof': {
            'direction': 'OUTGOING',
            'description': 'Revokes generated proof',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
POLYGONID_FUNCTIONS = {
    'V1': POLYGON_ID_V1_FUNCTIONS
}