"""Civic Protocol Functions for all versions"""

CIVIC_V1_FUNCTIONS = {
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
        'deleteIdentity': {
            'direction': 'OUTGOING',
            'description': 'Deletes existing identity',
            'method': '0x2e1a7d4d'
        },
        'verifyIdentity': {
            'direction': 'NEUTRAL',
            'description': 'Verifies identity status',
            'method': '0x9d2f32dd'
        }
    },
    'GATEKEEPER': {
        'registerGatekeeper': {
            'direction': 'OUTGOING',
            'description': 'Registers new gatekeeper',
            'method': '0x3a088cd2'
        },
        'verifyGatekeeper': {
            'direction': 'NEUTRAL',
            'description': 'Verifies gatekeeper status',
            'method': '0x7535d246'
        },
        'updateGatekeeper': {
            'direction': 'OUTGOING',
            'description': 'Updates gatekeeper parameters',
            'method': '0x2f4f5cc5'
        }
    },
    'TOKEN': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes CVC tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes CVC tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
CIVIC_FUNCTIONS = {
    'V1': CIVIC_V1_FUNCTIONS
}