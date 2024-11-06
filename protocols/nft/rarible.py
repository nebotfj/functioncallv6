"""Rarible NFT Marketplace Functions for all versions"""

RARIBLE_V2_FUNCTIONS = {
    'TRADING': {
        'sell': {
            'direction': 'OUTGOING',
            'description': 'Creates sell order',
            'method': '0x6c1aaf13'
        },
        'buy': {
            'direction': 'OUTGOING',
            'description': 'Creates buy order',
            'method': '0x94b576de'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels active order',
            'method': '0x2e1a7d4d'
        },
        'acceptBid': {
            'direction': 'BOTH',
            'description': 'Accepts NFT bid',
            'method': '0xbc61394a'
        }
    },
    'CREATION': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new NFT',
            'method': '0x40c10f19'
        },
        'mintAndSell': {
            'direction': 'OUTGOING',
            'description': 'Mints and lists NFT',
            'method': '0x6e553f65'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns existing NFT',
            'method': '0x89afcb44'
        },
        'mintBatch': {
            'direction': 'OUTGOING',
            'description': 'Mints multiple NFTs',
            'method': '0x945bcec9'
        }
    },
    'LAZY_MINTING': {
        'createLazyMint': {
            'direction': 'OUTGOING',
            'description': 'Creates lazy mint',
            'method': '0x1698ee82'
        },
        'fulfillLazyMint': {
            'direction': 'BOTH',
            'description': 'Fulfills lazy mint',
            'method': '0x4ce38b5f'
        },
        'cancelLazyMint': {
            'direction': 'OUTGOING',
            'description': 'Cancels lazy mint',
            'method': '0x2e1a7d4d'
        }
    },
    'ROYALTIES': {
        'setRoyalties': {
            'direction': 'OUTGOING',
            'description': 'Sets NFT royalties',
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
RARIBLE_FUNCTIONS = {
    'V2': RARIBLE_V2_FUNCTIONS
}