"""DIA Protocol Functions for all versions"""

DIA_V1_FUNCTIONS = {
    'ORACLE': {
        'updateValue': {
            'direction': 'OUTGOING',
            'description': 'Updates oracle value',
            'method': '0x7535d246'
        },
        'getValue': {
            'direction': 'NEUTRAL',
            'description': 'Gets oracle value',
            'method': '0x9d2f32dd'
        },
        'setBatch': {
            'direction': 'OUTGOING',
            'description': 'Updates multiple values',
            'method': '0x945bcec9'
        },
        'updateMetadata': {
            'direction': 'OUTGOING',
            'description': 'Updates value metadata',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stakeDIA': {
            'direction': 'OUTGOING',
            'description': 'Stakes DIA tokens',
            'method': '0xa694fc3a'
        },
        'unstakeDIA': {
            'direction': 'INCOMING',
            'description': 'Unstakes DIA tokens',
            'method': '0x2e1a7d4d'
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
DIA_FUNCTIONS = {
    'V1': DIA_V1_FUNCTIONS
}