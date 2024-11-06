"""X2Y2 NFT Marketplace Functions for all versions"""

X2Y2_V1_FUNCTIONS = {
    'TRADING': {
        'list': {
            'direction': 'OUTGOING',
            'description': 'Lists NFT for sale',
            'method': '0x6c1aaf13'
        },
        'buy': {
            'direction': 'OUTGOING',
            'description': 'Buys listed NFT',
            'method': '0x94b576de'
        },
        'cancel': {
            'direction': 'OUTGOING',
            'description': 'Cancels NFT listing',
            'method': '0x2e1a7d4d'
        },
        'bulkList': {
            'direction': 'OUTGOING',
            'description': 'Lists multiple NFTs',
            'method': '0x945bcec9'
        },
        'bulkBuy': {
            'direction': 'OUTGOING',
            'description': 'Buys multiple NFTs',
            'method': '0x7c025200'
        }
    },
    'OFFERS': {
        'makeOffer': {
            'direction': 'OUTGOING',
            'description': 'Makes offer on NFT',
            'method': '0x94b576de'
        },
        'cancelOffer': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing offer',
            'method': '0x2e1a7d4d'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts NFT offer',
            'method': '0xbc61394a'
        }
    },
    'REWARDS': {
        'stakeX2Y2': {
            'direction': 'OUTGOING',
            'description': 'Stakes X2Y2 tokens',
            'method': '0xa694fc3a'
        },
        'unstakeX2Y2': {
            'direction': 'INCOMING',
            'description': 'Unstakes X2Y2 tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'COLLECTIONS': {
        'setRoyalties': {
            'direction': 'OUTGOING',
            'description': 'Sets collection royalties',
            'method': '0x8293745b'
        },
        'updateCollection': {
            'direction': 'OUTGOING',
            'description': 'Updates collection metadata',
            'method': '0x7535d246'
        },
        'verifyCollection': {
            'direction': 'OUTGOING',
            'description': 'Verifies collection authenticity',
            'method': '0x2f4f5cc5'
        }
    }
}

# Combined functions for all versions
X2Y2_FUNCTIONS = {
    'V1': X2Y2_V1_FUNCTIONS
}