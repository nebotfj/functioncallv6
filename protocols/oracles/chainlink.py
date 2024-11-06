"""Chainlink Protocol Functions for all versions"""

CHAINLINK_V1_FUNCTIONS = {
    'ORACLE': {
        'latestRoundData': {
            'direction': 'NEUTRAL',
            'description': 'Gets latest price data',
            'method': '0xfeaf968c'
        },
        'getRoundData': {
            'direction': 'NEUTRAL',
            'description': 'Gets historical price data',
            'method': '0x9a6fc8f5'
        },
        'getAnswer': {
            'direction': 'NEUTRAL',
            'description': 'Gets price for round',
            'method': '0xb5ab58dc'
        },
        'getTimestamp': {
            'direction': 'NEUTRAL',
            'description': 'Gets timestamp for round',
            'method': '0xb633620c'
        }
    },
    'KEEPER': {
        'checkUpkeep': {
            'direction': 'NEUTRAL',
            'description': 'Checks if upkeep needed',
            'method': '0x6e04ff0d'
        },
        'performUpkeep': {
            'direction': 'OUTGOING',
            'description': 'Performs upkeep task',
            'method': '0x4585e33b'
        },
        'registerUpkeep': {
            'direction': 'OUTGOING',
            'description': 'Registers new upkeep',
            'method': '0x6e04ff0d'
        },
        'cancelUpkeep': {
            'direction': 'OUTGOING',
            'description': 'Cancels active upkeep',
            'method': '0x2e1a7d4d'
        }
    },
    'VRF': {
        'requestRandomness': {
            'direction': 'OUTGOING',
            'description': 'Requests random number',
            'method': '0x9b3d47b4'
        },
        'fulfillRandomness': {
            'direction': 'INCOMING',
            'description': 'Fulfills random request',
            'method': '0x4ce38b5f'
        },
        'requestRandomWords': {
            'direction': 'OUTGOING',
            'description': 'Requests multiple randoms',
            'method': '0x9b3d47b4'
        },
        'fulfillRandomWords': {
            'direction': 'INCOMING',
            'description': 'Fulfills random words',
            'method': '0x4ce38b5f'
        }
    }
}

# Combined functions for all versions
CHAINLINK_FUNCTIONS = {
    'V1': CHAINLINK_V1_FUNCTIONS
}