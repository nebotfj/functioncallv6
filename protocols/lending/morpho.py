"""Morpho Protocol Functions for all versions"""

MORPHO_V1_FUNCTIONS = {
    'LENDING': {
        'supply': {
            'direction': 'OUTGOING',
            'description': 'Supplies assets to protocol',
            'method': '0x617ba037'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws supplied assets',
            'method': '0x69328dec'
        },
        'borrow': {
            'direction': 'INCOMING',
            'description': 'Borrows assets from protocol',
            'method': '0xc5ebeaec'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed assets',
            'method': '0x573ade81'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates undercollateralized position',
            'method': '0x96cd4ddb'
        }
    },
    'P2P_MATCHING': {
        'matchLenders': {
            'direction': 'BOTH',
            'description': 'Matches lenders with borrowers',
            'method': '0x7c025200'
        },
        'matchBorrowers': {
            'direction': 'BOTH',
            'description': 'Matches borrowers with lenders',
            'method': '0x2f4f5cc5'
        },
        'updateIndexes': {
            'direction': 'OUTGOING',
            'description': 'Updates P2P indexes',
            'method': '0x7535d246'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims protocol rewards',
            'method': '0xe6f1daf2'
        },
        'claimMorpho': {
            'direction': 'INCOMING',
            'description': 'Claims MORPHO tokens',
            'method': '0x4e71d92d'
        },
        'stakeMorpho': {
            'direction': 'OUTGOING',
            'description': 'Stakes MORPHO tokens',
            'method': '0xa694fc3a'
        }
    }
}

# Combined functions for all versions
MORPHO_FUNCTIONS = {
    'V1': MORPHO_V1_FUNCTIONS
}