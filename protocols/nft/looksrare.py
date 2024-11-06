"""LooksRare NFT Marketplace Functions for all versions"""

LOOKSRARE_V1_FUNCTIONS = {
    'TRADING': {
        'createOrder': {
            'direction': 'OUTGOING',
            'description': 'Creates new order',
            'method': '0x6c1aaf13'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'matchOrder': {
            'direction': 'BOTH',
            'description': 'Matches single order',
            'method': '0xbc61394a'
        },
        'matchOrders': {
            'direction': 'BOTH',
            'description': 'Matches multiple orders',
            'method': '0x945bcec9'
        }
    },
    'REWARDS': {
        'stakeLOOKS': {
            'direction': 'OUTGOING',
            'description': 'Stakes LOOKS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLOOKS': {
            'direction': 'INCOMING',
            'description': 'Unstakes LOOKS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds staking rewards',
            'method': '0xf69e2046'
        }
    },
    'ROYALTIES': {
        'setRoyalties': {
            'direction': 'OUTGOING',
            'description': 'Sets collection royalties',
            'method': '0x8293745b'
        },
        'updateRoyalties': {
            'direction': 'OUTGOING',
            'description': 'Updates royalty parameters',
            'method': '0x7535d246'
        },
        'claimRoyalties': {
            'direction': 'INCOMING',
            'description': 'Claims earned royalties',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
LOOKSRARE_FUNCTIONS = {
    'V1': LOOKSRARE_V1_FUNCTIONS
}