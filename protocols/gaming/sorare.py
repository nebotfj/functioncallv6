"""Sorare Protocol Functions for all versions"""

SORARE_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'createLineup': {
            'direction': 'OUTGOING',
            'description': 'Creates team lineup',
            'method': '0x1698ee82'
        },
        'enterTournament': {
            'direction': 'OUTGOING',
            'description': 'Enters card tournament',
            'method': '0x9b3d47b4'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims tournament rewards',
            'method': '0x4e71d92d'
        },
        'compositeCards': {
            'direction': 'OUTGOING',
            'description': 'Creates composite card',
            'method': '0x7535d246'
        }
    },
    'MARKETPLACE': {
        'listCard': {
            'direction': 'OUTGOING',
            'description': 'Lists card for sale',
            'method': '0x6c1aaf13'
        },
        'buyCard': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed card',
            'method': '0x94b576de'
        },
        'makeOffer': {
            'direction': 'OUTGOING',
            'description': 'Makes offer on card',
            'method': '0x94b576de'
        },
        'acceptOffer': {
            'direction': 'BOTH',
            'description': 'Accepts card offer',
            'method': '0xbc61394a'
        }
    },
    'AUCTIONS': {
        'createAuction': {
            'direction': 'OUTGOING',
            'description': 'Creates card auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'claimCard': {
            'direction': 'INCOMING',
            'description': 'Claims won card',
            'method': '0x4e71d92d'
        },
        'withdrawBid': {
            'direction': 'INCOMING',
            'description': 'Withdraws auction bid',
            'method': '0x69328dec'
        }
    },
    'REWARDS': {
        'claimETH': {
            'direction': 'INCOMING',
            'description': 'Claims ETH rewards',
            'method': '0x4e71d92d'
        },
        'claimCards': {
            'direction': 'INCOMING',
            'description': 'Claims reward cards',
            'method': '0x4e71d92d'
        },
        'stakeSorare': {
            'direction': 'OUTGOING',
            'description': 'Stakes Sorare tokens',
            'method': '0xa694fc3a'
        },
        'unstakeSorare': {
            'direction': 'INCOMING',
            'description': 'Unstakes Sorare tokens',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
SORARE_FUNCTIONS = {
    'V1': SORARE_V1_FUNCTIONS
}