"""StakeWise Protocol Functions for all versions"""

STAKEWISE_V2_FUNCTIONS = {
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes ETH in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes ETH from protocol',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds earned rewards',
            'method': '0xf69e2046'
        },
        'requestWithdrawal': {
            'direction': 'OUTGOING',
            'description': 'Requests ETH withdrawal',
            'method': '0x0c49ccbe'
        }
    },
    'POOL': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Joins liquidity pool',
            'method': '0xb95cac28'
        },
        'exitPool': {
            'direction': 'INCOMING',
            'description': 'Exits liquidity pool',
            'method': '0x8bdb3913'
        },
        'swapExactTokensForTokens': {
            'direction': 'BOTH',
            'description': 'Swaps exact tokens',
            'method': '0x38ed1739'
        },
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds pool liquidity',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes pool liquidity',
            'method': '0xbaa2abde'
        }
    },
    'MERKLE': {
        'claimMerkleRewards': {
            'direction': 'INCOMING',
            'description': 'Claims merkle rewards',
            'method': '0x4e71d92d'
        },
        'verifyProof': {
            'direction': 'NEUTRAL',
            'description': 'Verifies merkle proof',
            'method': '0x7535d246'
        },
        'updateMerkleRoot': {
            'direction': 'OUTGOING',
            'description': 'Updates merkle root',
            'method': '0x2f4f5cc5'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    }
}

# Combined functions for all versions
STAKEWISE_FUNCTIONS = {
    'V2': STAKEWISE_V2_FUNCTIONS
}