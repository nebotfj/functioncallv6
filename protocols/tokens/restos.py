ETH_GENERIC_FUNCTIONS = {
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
    },
    'SWAPS': {
        'disperseEther': {
            'direction': 'OUTGOING',
            'description': 'Disperse ETH to multiple addresses',
            'method': '0xe63d38ed',
           # 'protocol': ['Disperse.app']
        },
    },
    'STAKING': {
        'intendToUnstake': {
            'direction': 'OUTGOING',
            'description': 'Signal intention to unstake',
            'method': '0xc32f7f73',
            #'protocol': ['Generic Staking']
        },
        'stakeRewards': {
            'direction': 'OUTGOING',
            'description': 'Stake reward tokens',
            'method': '0x8f31c7f9',
            #'protocol': ['Generic Staking']
        }
    },
    'CLAIMS': {
        'claimAll': {
            'direction': 'INCOMING',
            'description': 'Claim all pending rewards',
            'method': '0x4e71d92d',
            #'protocol': ['Generic Claims']
        },
        'claimBalance': {
            'direction': 'INCOMING',
            'description': 'Claim available balance',
            'method': '0x8f31c7f9',
            #'protocol': ['Generic Claims']
        },
        'claimDistributions': {
            'direction': 'INCOMING',
            'description': 'Claim token distributions',
            'method': '0x9af6b617',
          #  'protocol': ['Generic Claims']
        },
        'claimFor': {
            'direction': 'INCOMING',
            'description': 'Claim rewards for another address',
            'method': '0x2f6c493c',
           # 'protocol': ['Generic Claims']
        },
        'claimStakerReward': {
            'direction': 'INCOMING',
            'description': 'Claim staking rewards',
            'method': '0x7c3b74a1',
           # 'protocol': ['Generic Staking']
        }
    },
    'DEPOSITS': {
        'depositPool': {
            'direction': 'OUTGOING',
            'description': 'Deposit into liquidity pool',
            'method': '0x43a0d066',
           # 'protocol': ['Generic Pools']
        },
        'depositSavings': {
            'direction': 'OUTGOING',
            'description': 'Deposit into savings protocol',
            'method': '0x234c0aa9',
          #  'protocol': ['Generic Yield Protocols']
        },
    },
    'WITHDRAWALS': {
        'withdrawAllBase': {
            'direction': 'INCOMING',
            'description': 'Withdraw all base tokens',
            'method': '0x1f1fcd51',
         #   'protocol': ['Generic Protocols']
        },
        'withdrawAllQuote': {
            'direction': 'INCOMING',
            'description': 'Withdraw all quote tokens',
            'method': '0x89b7daa9',
            #'protocol': ['Generic Protocols']
        },
        'withdrawERC20For': {
            'direction': 'INCOMING',
            'description': 'Withdraw ERC20 tokens for another address',
            'method': '0x9e281a98',
          #  'protocol': ['Generic Protocols']
        },
        'withdrawFunds': {
            'direction': 'INCOMING',
            'description': 'Generic withdrawal function',
            'method': '0x24ed7740',
            #'protocol': ['Generic Protocols']
        }
    },
    'MINTING': {
        'mintWithEther': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with ETH',
            'method': '0x90a56f37',
            #'protocol': ['Generic Minting']
        },
        'mintWithToken': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with another token',
            'method': '0x8f31c7f9',
          #  'protocol': ['Generic Minting']
        }
    },
    'BURNING': {
        'burnToEther': {
            'direction': 'BOTH',
            'description': 'Burn tokens for ETH',
            'method': '0x3f7d753c',
         #   'protocol': ['Generic Burning']
        },
        'burnToToken': {
            'direction': 'BOTH',
            'description': 'Burn tokens for another token',
            'method': '0x7ebf1db5',
           # 'protocol': ['Generic Burning']
        }
    },
    'MIGRATION': {
        'migrateAll': {
            'direction': 'BOTH',
            'description': 'Migrate all assets',
            'method': '0x6e7cf85f',
            #'protocol': ['Generic Migration']
        },
    },
    'GOVERNANCE': {
        'voteFor': {
            'direction': 'OUTGOING',
            'description': 'Cast vote for proposal',
            'method': '0x86a50535',
           # 'protocol': ['GenericDAO Voting']
        },
        
    },
    'UTILITY': {
        'approveAndCall': {
            'direction': 'OUTGOING',
            'description': 'Approve and execute in one transaction',
            'method': '0xcae9ca51',
          #  'protocol': ['ERC20 Extended']
        },
    },
        'invalidateUnorderedNonces': {
            'direction': 'OUTGOING',
            'description': 'Invalidate unused nonces',
            'method': '0x9e7b8d61',
          #  'protocol': ['Generic Security Protocols']
        },

    'TRANSFERS': {
        'ETH transfer': {
            'direction': 'OUTGOING',
            'description': 'Native ETH transfer',
            'method': '0x'  # Native transfer has no method ID
            # 'protocol': ['Ethereum']
        },
    },
 
    'SUSPICIOUS': { #This transactions usually involved in scam transactions
        'JunionYoutubeXD_dashhvetozhe': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
          #  'protocol': ['SUSPICIOUS']
        },
        'LetsInvest': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
           # 'protocol': ['SUSPICIOUS']
        }
    }
}


# Combined functions for all versions
ETH_GENERIC = {
    'ETH_GENERIC': ETH_GENERIC_FUNCTIONS
}