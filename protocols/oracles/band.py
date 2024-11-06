"""Band Protocol Functions for all versions"""

BAND_V1_FUNCTIONS = {
    'ORACLE': {
        'relayBlock': {
            'direction': 'OUTGOING',
            'description': 'Relays oracle block',
            'method': '0x7535d246'
        },
        'getReferenceData': {
            'direction': 'NEUTRAL',
            'description': 'Gets price reference data',
            'method': '0x9d2f32dd'
        },
        'getReferenceDataBulk': {
            'direction': 'NEUTRAL',
            'description': 'Gets multiple price references',
            'method': '0x0a0e6b3b'
        },
        'requestData': {
            'direction': 'OUTGOING',
            'description': 'Requests oracle data',
            'method': '0x9b3d47b4'
        }
    },
    'STAKING': {
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates BAND tokens',
            'method': '0x5c19a95c'
        },
        'undelegate': {
            'direction': 'INCOMING',
            'description': 'Undelegates BAND tokens',
            'method': '0x2e1a7d4d'
        },
        'redelegate': {
            'direction': 'BOTH',
            'description': 'Redelegates to new validator',
            'method': '0x4ce38b5f'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

# Combined functions for all versions
BAND_FUNCTIONS = {
    'V1': BAND_V1_FUNCTIONS
}