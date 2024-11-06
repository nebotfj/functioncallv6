"""API3 Protocol Functions for all versions"""

API3_V1_FUNCTIONS = {
    'ORACLE': {
        'updateBeacon': {
            'direction': 'OUTGOING',
            'description': 'Updates data feed beacon',
            'method': '0x7535d246'
        },
        'readDataFeed': {
            'direction': 'NEUTRAL',
            'description': 'Reads oracle data feed',
            'method': '0x9d2f32dd'
        },
        'requestData': {
            'direction': 'OUTGOING',
            'description': 'Requests oracle data',
            'method': '0x9b3d47b4'
        },
        'fulfillRequest': {
            'direction': 'INCOMING',
            'description': 'Fulfills data request',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stakeAPI3': {
            'direction': 'OUTGOING',
            'description': 'Stakes API3 tokens',
            'method': '0xa694fc3a'
        },
        'unstakeAPI3': {
            'direction': 'INCOMING',
            'description': 'Unstakes API3 tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'DAO': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates DAO proposal',
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
API3_FUNCTIONS = {
    'V1': API3_V1_FUNCTIONS
}