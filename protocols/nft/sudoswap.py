"""Sudoswap NFT Marketplace Functions for all versions"""

SUDOSWAP_V1_FUNCTIONS = {
    'POOL': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates new NFT pool',
            'method': '0x1698ee82'
        },
        'addNFT': {
            'direction': 'OUTGOING',
            'description': 'Adds NFT to pool',
            'method': '0x47e7ef24'
        },
        'removeNFT': {
            'direction': 'INCOMING',
            'description': 'Removes NFT from pool',
            'method': '0x69328dec'
        },
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from pool',
            'method': '0xbaa2abde'
        }
    },
    'TRADING': {
        'swapNFTForToken': {
            'direction': 'BOTH',
            'description': 'Swaps NFT for tokens',
            'method': '0x128acb08'
        },
        'swapTokenForNFT': {
            'direction': 'BOTH',
            'description': 'Swaps tokens for NFT',
            'method': '0x7c025200'
        },
        'swapNFTForAnyNFT': {
            'direction': 'BOTH',
            'description': 'Swaps NFT for any other NFT',
            'method': '0x2f4f5cc5'
        },
        'robustSwapNFT': {
            'direction': 'BOTH',
            'description': 'Executes atomic NFT swap',
            'method': '0x4ce38b5f'
        }
    },
    'BONDING_CURVE': {
        'updateDelta': {
            'direction': 'OUTGOING',
            'description': 'Updates bonding curve delta',
            'method': '0x7535d246'
        },
        'updateSpotPrice': {
            'direction': 'OUTGOING',
            'description': 'Updates spot price',
            'method': '0xe74b981b'
        },
        'updateFee': {
            'direction': 'OUTGOING',
            'description': 'Updates trading fee',
            'method': '0x8293745b'
        }
    }
}

# Combined functions for all versions
SUDOSWAP_FUNCTIONS = {
    'V1': SUDOSWAP_V1_FUNCTIONS
}