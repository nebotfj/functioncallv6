PROTOCOL_FUNCTIONS = {
    'VESTING_CONTRACTS': {
        'create_lock': {
            'direction': 'OUTGOING',
            'description': 'Creates a new lock for tokens',
            'method': '0x65fc3873'
        },
        'increase_amount': {
            'direction': 'OUTGOING',
            'description': 'Increases the amount of locked tokens',
            'method': '0x4957677c'
        },
        'increase_unlock_time': {
            'direction': 'OUTGOING',
            'description': 'Extends the lock duration',
            'method': '0xc27f68a5'
        }
    },
    'STAKING_PROTOCOLS': {
        'claimStakerReward': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0x87788782'
        },
        'intendToUnstake': {
            'direction': 'OUTGOING',
            'description': 'Signals intention to unstake tokens',
            'method': '0xc32c92b1'
        },
        'stakeRewards': {
            'direction': 'OUTGOING',
            'description': 'Stakes reward tokens',
            'method': '0x93f4bcb8'
        }
    },
    'GENERIC_ERC20': {
        'approveAndCall': {
            'direction': 'OUTGOING',
            'description': 'Approves spending and calls another contract',
            'method': '0xcae9ca51'
        },
        'claimTokens': {
            'direction': 'INCOMING',
            'description': 'Claims tokens from a distribution',
            'method': '0xdf8de3e7'
        },
        'withdrawERC20For': {
            'direction': 'OUTGOING',
            'description': 'Withdraws ERC20 tokens on behalf of another address',
            'method': '0x9e281a98'
        }
    },
    'YIELD_AGGREGATOR': {
        'depositPool': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into a yield pool',
            'method': '0x5f7c6d37'
        },
        'depositSavings': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into a savings protocol',
            'method': '0x34f4fd51'
        },
        'depositV3': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets using V3 contract',
            'method': '0x9aa5d462'
        }
    },
    'NFT_MARKETPLACE': {
        'fillBounty': {
            'direction': 'OUTGOING',
            'description': 'Completes a bounty by providing required NFT',
            'method': '0x78b85579'
        },
        'purchase': {
            'direction': 'OUTGOING',
            'description': 'Purchases an NFT from the marketplace',
            'method': '0x64849142'
        }
    },

    'DISTRIBUTION': {
        'disperseEther': {
            'direction': 'OUTGOING',
            'description': 'Distributes ETH to multiple addresses',
            'method': '0xd152cd41'
        },
        'claimDistributions': {
            'direction': 'INCOMING',
            'description': 'Claims tokens from multiple distributions',
            'method': '0x89f9aab7'
        }
    }

}