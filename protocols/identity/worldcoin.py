"""Worldcoin Protocol Functions for all versions"""

WORLDCOIN_V1_FUNCTIONS = {
    'IDENTITY': {
        'verify': {
            'direction': 'OUTGOING',
            'description': 'Verifies unique humanity',
            'method': '0x4b8a3529'
        },
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
        }
    },
    'PROOF': {
        'generateProof': {
            'direction': 'OUTGOING',
            'description': 'Generates proof of humanity',
            'method': '0x9b3d47b4'
        },
        'verifyProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies proof of humanity',
            'method': '0x7c025200'
        },
        'revokeProof': {
            'direction': 'OUTGOING',
            'description': 'Revokes generated proof',
            'method': '0x2e1a7d4d'
        }
    },
    'CREDENTIALS': {
        'issueCredential': {
            'direction': 'OUTGOING',
            'description': 'Issues identity credential',
            'method': '0x3a088cd2'
        },
        'revokeCredential': {
            'direction': 'OUTGOING',
            'description': 'Revokes identity credential',
            'method': '0x5f7b8feb'
        },
        'verifyCredential': {
            'direction': 'NEUTRAL',
            'description': 'Verifies credential validity',
            'method': '0x7535d246'
        }
    },
    'ORBS': {
        'registerOrb': {
            'direction': 'OUTGOING',
            'description': 'Registers new Orb device',
            'method': '0x1698ee82'
        },
        'updateOrb': {
            'direction': 'OUTGOING',
            'description': 'Updates Orb parameters',
            'method': '0x7535d246'
        },
        'deactivateOrb': {
            'direction': 'OUTGOING',
            'description': 'Deactivates Orb device',
            'method': '0x2e1a7d4d'
        }
    },
    'STAKING': {
        'stakeWLD': {
            'direction': 'OUTGOING',
            'description': 'Stakes WLD tokens',
            'method': '0xa694fc3a'
        },
        'unstakeWLD': {
            'direction': 'INCOMING',
            'description': 'Unstakes WLD tokens',
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
WORLDCOIN_FUNCTIONS = {
    'V1': WORLDCOIN_V1_FUNCTIONS
}