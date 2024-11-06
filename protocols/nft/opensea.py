"""OpenSea NFT Marketplace Functions for all versions"""

OPENSEA_V1_FUNCTIONS = {
    'LISTING': {
        'createListing': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT listing',
            'method': '0x6c1aaf13'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels active listing',
            'method': '0x2e1a7d4d'
        },
        'fulfillListing': {
            'direction': 'OUTGOING',
            'description': 'Fulfills NFT listing',
            'method': '0xbc61394a'
        },
        'bulkListing': {
            'direction': 'OUTGOING',
            'description': 'Creates multiple listings',
            'method': '0x945bcec9'
        }
    },
    'OFFERS': {
        'createOffer': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT offer',
            'method': '0x94b576de'
        },
        'cancelOffer': {
            'direction': 'OUTGOING',
            'description': 'Cancels active offer',
            'method': '0x2e1a7d4d'
        },
        'fulfillOffer': {
            'direction': 'BOTH',
            'description': 'Fulfills NFT offer',
            'method': '0xbc61394a'
        },
        'bulkOffers': {
            'direction': 'OUTGOING',
            'description': 'Creates multiple offers',
            'method': '0x945bcec9'
        }
    },
    'AUCTIONS': {
        'createAuction': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'cancelAuction': {
            'direction': 'OUTGOING',
            'description': 'Cancels active auction',
            'method': '0x96b5a755'
        },
        'endAuction': {
            'direction': 'BOTH',
            'description': 'Ends NFT auction',
            'method': '0x4ce38b5f'
        },
        'claimAuction': {
            'direction': 'INCOMING',
            'description': 'Claims won auction',
            'method': '0x4e71d92d'
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
OPENSEA_FUNCTIONS = {
    'V1': OPENSEA_V1_FUNCTIONS
}