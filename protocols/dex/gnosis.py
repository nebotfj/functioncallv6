"""Gnosis Protocol Functions for all versions"""

GNOSIS_V2_FUNCTIONS = {
    'TRADING': {
        'placeOrder': {
            'direction': 'OUTGOING',
            'description': 'Places limit order',
            'method': '0xb8e3de8e'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'fulfillOrder': {
            'direction': 'BOTH',
            'description': 'Fulfills placed order',
            'method': '0x4d5f327c'
        },
        'batchTrade': {
            'direction': 'BOTH',
            'description': 'Executes batch of trades',
            'method': '0x945bcec9'
        },
        'settleOrders': {
            'direction': 'BOTH',
            'description': 'Settles batch of orders',
            'method': '0x4d5f327c'
        }
    },
    'AUCTIONS': {
        'initiateAuction': {
            'direction': 'OUTGOING',
            'description': 'Starts new auction',
            'method': '0x3b3be21a'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places bid in auction',
            'method': '0x9d2f32dd'
        },
        'claimAuction': {
            'direction': 'INCOMING',
            'description': 'Claims auction proceeds',
            'method': '0x9a756e44'
        },
        'cancelAuction': {
            'direction': 'OUTGOING',
            'description': 'Cancels active auction',
            'method': '0x96b5a755'
        }
    },
    'SAFE': {
        'createSafe': {
            'direction': 'OUTGOING',
            'description': 'Creates new Safe',
            'method': '0x0ec78d9e'
        },
        'executeTransaction': {
            'direction': 'OUTGOING',
            'description': 'Executes Safe transaction',
            'method': '0x6a761202'
        },
        'addOwner': {
            'direction': 'OUTGOING',
            'description': 'Adds Safe owner',
            'method': '0x0d582f13'
        },
        'removeOwner': {
            'direction': 'OUTGOING',
            'description': 'Removes Safe owner',
            'method': '0xf8dc5dd9'
        },
        'replaceOwner': {
            'direction': 'OUTGOING',
            'description': 'Replaces Safe owner',
            'method': '0xe20056e6'
        },
        'changeThreshold': {
            'direction': 'OUTGOING',
            'description': 'Changes Safe threshold',
            'method': '0x694e80c3'
        }
    },
    'CONDITIONAL_TOKENS': {
        'splitPosition': {
            'direction': 'OUTGOING',
            'description': 'Splits conditional token position',
            'method': '0x7c53966a'
        },
        'mergePositions': {
            'direction': 'INCOMING',
            'description': 'Merges conditional token positions',
            'method': '0x8c975e11'
        },
        'redeemPositions': {
            'direction': 'INCOMING',
            'description': 'Redeems conditional token positions',
            'method': '0xdb1ca77f'
        },
        'reportPayouts': {
            'direction': 'OUTGOING',
            'description': 'Reports condition payouts',
            'method': '0x1626ba7e'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    }
}

# Combined functions for all versions
GNOSIS_FUNCTIONS = {
    'V2': GNOSIS_V2_FUNCTIONS
}