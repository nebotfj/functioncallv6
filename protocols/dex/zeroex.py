"""0x Protocol Functions for all versions"""

ZEROEX_V4_FUNCTIONS = {
    'TRADING': {
        'fillOrder': {
            'direction': 'BOTH',
            'description': 'Fills limit order',
            'method': '0xbc61394a'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels limit order',
            'method': '0x2e1a7d4d'
        },
        'batchFillOrders': {
            'direction': 'BOTH',
            'description': 'Fills multiple orders',
            'method': '0x945bcec9'
        },
        'matchOrders': {
            'direction': 'BOTH',
            'description': 'Matches complementary orders',
            'method': '0x88ec79fb'
        }
    },
    'RFQ': {
        'requestQuote': {
            'direction': 'NEUTRAL',
            'description': 'Requests quote for trade',
            'method': '0x9d2f32dd'
        },
        'fillRfqOrder': {
            'direction': 'BOTH',
            'description': 'Fills RFQ order',
            'method': '0x5da7810f'
        },
        'cancelRfqOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels RFQ order',
            'method': '0x5f7b8feb'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes ZRX tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes ZRX tokens',
            'method': '0x2e1a7d4d'
        },
        'withdrawDelegatorRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'BRIDGE': {
        'bridgeTransfer': {
            'direction': 'OUTGOING',
            'description': 'Transfers across bridge',
            'method': '0x8b9e4f93'
        },
        'transformERC20': {
            'direction': 'BOTH',
            'description': 'Transforms token format',
            'method': '0x415565b0'
        }
    }
}

# Combined functions for all versions
ZEROEX_FUNCTIONS = {
    'V4': ZEROEX_V4_FUNCTIONS
}