"""NFTX NFT Marketplace Functions for all versions"""

NFTX_V2_FUNCTIONS = {
    'VAULT': {
        'createVault': {
            'direction': 'OUTGOING',
            'description': 'Creates new NFT vault',
            'method': '0x1698ee82'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints vault tokens',
            'method': '0x40c10f19'
        },
        'mintAndStake': {
            'direction': 'OUTGOING',
            'description': 'Mints and stakes tokens',
            'method': '0x6e553f65'
        },
        'redeem': {
            'direction': 'BOTH',
            'description': 'Redeems vault tokens',
            'method': '0xdb006a75'
        },
        'redeemAndRemove': {
            'direction': 'BOTH',
            'description': 'Redeems and removes liquidity',
            'method': '0x4ce38b5f'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes vault tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes vault tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'stakeLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0x0c49ccbe'
        }
    },
    'TRADING': {
        'swap': {
            'direction': 'BOTH',
            'description': 'Swaps vault tokens',
            'method': '0x128acb08'
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
        },
        'flashLoan': {
            'direction': 'BOTH',
            'description': 'Executes flash loan',
            'method': '0x5cffe9de'
        }
    }
}

# Combined functions for all versions
NFTX_FUNCTIONS = {
    'V2': NFTX_V2_FUNCTIONS
}