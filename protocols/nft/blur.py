"""Blur NFT Marketplace Functions for all versions"""

BLUR_V1_FUNCTIONS = {
    'TRADING': {
        'executeBid': {
            'direction': 'BOTH',
            'description': 'Executes bid on NFT',
            'method': '0xbc61394a'
        },
        'executeAsk': {
            'direction': 'BOTH',
            'description': 'Executes ask for NFT',
            'method': '0x9a802a6d'
        },
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0x2e1a7d4d'
        },
        'bulkExecute': {
            'direction': 'BOTH',
            'description': 'Executes multiple orders',
            'method': '0x945bcec9'
        }
    },
    'LENDING': {
        'lendNFT': {
            'direction': 'OUTGOING',
            'description': 'Lends NFT to borrower',
            'method': '0x47e7ef24'
        },
        'borrowNFT': {
            'direction': 'INCOMING',
            'description': 'Borrows NFT from lender',
            'method': '0xc5ebeaec'
        },
        'repayLoan': {
            'direction': 'OUTGOING',
            'description': 'Repays NFT loan',
            'method': '0x573ade81'
        },
        'claimDefaultedNFT': {
            'direction': 'INCOMING',
            'description': 'Claims defaulted NFT',
            'method': '0x4e71d92d'
        }
    },
    'STAKING': {
        'stakeBlur': {
            'direction': 'OUTGOING',
            'description': 'Stakes BLUR tokens',
            'method': '0xa694fc3a'
        },
        'unstakeBlur': {
            'direction': 'INCOMING',
            'description': 'Unstakes BLUR tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
BLUR_FUNCTIONS = {
    'V1': BLUR_V1_FUNCTIONS
}