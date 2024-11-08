"""Magic Eden Protocol Functions for all versions"""

MAGIC_EDEN_V1_FUNCTIONS = {
    'MARKETPLACE': {
        'listNFT': {
            'direction': 'OUTGOING',
            'description': 'Lists NFT for sale',
            'method': '0x6c1aaf13'
        },
        'buyNFT': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed NFT',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels NFT listing',
            'method': '0x2e1a7d4d'
        },
        'makeOffer': {
            'direction': 'OUTGOING',
            'description': 'Makes offer on NFT',
            'method': '0x94b576de'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts NFT offer',
            'method': '0xbc61394a'
        },
        'bulkList': {
            'direction': 'OUTGOING',
            'description': 'Lists multiple NFTs',
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
        'settleAuction': {
            'direction': 'BOTH',
            'description': 'Settles completed auction',
            'method': '0x4ce38b5f'
        },
        'claimAuction': {
            'direction': 'INCOMING',
            'description': 'Claims won auction',
            'method': '0x4e71d92d'
        }
    },
    'COLLECTIONS': {
        'createCollection': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT collection',
            'method': '0x1698ee82'
        },
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
    },
    'LAUNCHPAD': {
        'createMint': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT mint',
            'method': '0x1698ee82'
        },
        'updateMint': {
            'direction': 'OUTGOING',
            'description': 'Updates mint parameters',
            'method': '0x7535d246'
        },
        'startMint': {
            'direction': 'OUTGOING',
            'description': 'Starts NFT minting',
            'method': '0x9b3d47b4'
        },
        'pauseMint': {
            'direction': 'OUTGOING',
            'description': 'Pauses NFT minting',
            'method': '0x5f7b8feb'
        }
    }
}

MAGIC_EDEN_V2_FUNCTIONS = {
    'MARKETPLACE': {
        'listNFT': {
            'direction': 'OUTGOING',
            'description': 'Lists NFT for sale',
            'method': '0x6c1aaf13'
        },
        'buyNFT': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed NFT',
            'method': '0x94b576de'
        },
        'cancelListing': {
            'direction': 'OUTGOING',
            'description': 'Cancels NFT listing',
            'method': '0x2e1a7d4d'
        },
        'makeOffer': {
            'direction': 'OUTGOING',
            'description': 'Makes offer on NFT',
            'method': '0x94b576de'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts NFT offer',
            'method': '0xbc61394a'
        },
        'bulkList': {
            'direction': 'OUTGOING',
            'description': 'Lists multiple NFTs',
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
        'settleAuction': {
            'direction': 'BOTH',
            'description': 'Settles completed auction',
            'method': '0x4ce38b5f'
        },
        'claimAuction': {
            'direction': 'INCOMING',
            'description': 'Claims won auction',
            'method': '0x4e71d92d'
        }
    },
    'COLLECTIONS': {
        'createCollection': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT collection',
            'method': '0x1698ee82'
        },
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
    },
    'LAUNCHPAD': {
        'createMint': {
            'direction': 'OUTGOING',
            'description': 'Creates NFT mint',
            'method': '0x1698ee82'
        },
        'updateMint': {
            'direction': 'OUTGOING',
            'description': 'Updates mint parameters',
            'method': '0x7535d246'
        },
        'startMint': {
            'direction': 'OUTGOING',
            'description': 'Starts NFT minting',
            'method': '0x9b3d47b4'
        },
        'pauseMint': {
            'direction': 'OUTGOING',
            'description': 'Pauses NFT minting',
            'method': '0x5f7b8feb'
        }
    },
    'REWARDS': {
        'stakeNFT': {
            'direction': 'OUTGOING',
            'description': 'Stakes NFT for rewards',
            'method': '0xa694fc3a'
        },
        'unstakeNFT': {
            'direction': 'INCOMING',
            'description': 'Unstakes NFT',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'CROSS_CHAIN': {
        'bridgeNFT': {
            'direction': 'OUTGOING',
            'description': 'Bridges NFT to another chain',
            'method': '0x8b9e4f93'
        },
        'claimBridgedNFT': {
            'direction': 'INCOMING',
            'description': 'Claims bridged NFT',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
MAGICEDEN_FUNCTIONS = {
    'V1': MAGIC_EDEN_V1_FUNCTIONS,
    'V2': MAGIC_EDEN_V2_FUNCTIONS
}