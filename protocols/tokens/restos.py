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
    },

    'LIQUIDITY': {
        'add_liquidity': {
            'direction': 'OUTGOING',
            'description': 'Add liquidity to pool',
            'method': '0x4515cef3',
            'protocol': ['Curve V1', 'Balancer V1']
        },
        'ZapOut2PairToken': {
            'direction': 'INCOMING',
            'description': 'Remove liquidity and convert to token pair',
            'method': '0x41f13681',
            'protocol': ['Zapper.fi']
        }
    },

    'SWAPS': {
        'swapExactETHForAlpha': {
            'direction': 'OUTGOING',
            'description': 'Swap exact ETH for Alpha token',
            'method': '0x7ff36ab5',
            'protocol': ['Uniswap V2']
        },
        'swapAndDeposit': {
            'direction': 'OUTGOING',
            'description': 'Swap token and deposit in one transaction',
            'method': '0x5a0c7376',
            'protocol': ['Compound', 'Aave V2']
        },
        'swapAndRepay': {
            'direction': 'OUTGOING',
            'description': 'Swap token and repay loan',
            'method': '0x2db1e36c',
            'protocol': ['Aave V2', 'Aave V3']
        },
        'swapAndSendV2': {
            'direction': 'BOTH',
            'description': 'Swap and send tokens to recipient',
            'method': '0x985d7a89',
            'protocol': ['1inch V2', 'ParaSwap']
        },
        'mixSwap': {
            'direction': 'BOTH',
            'description': 'Aggregated token swap',
            'method': '0x13240b31',
            'protocol': ['MixSwap', '1inch']
        },
        'tradeWithHint': {
            'direction': 'BOTH',
            'description': 'Trade with routing hint',
            'method': '0x6cf68693',
            'protocol': ['KyberSwap V2']
        },
        'tradeWithHintAndFee': {
            'direction': 'BOTH',
            'description': 'Trade with hint and fee structure',
            'method': '0xae591d54',
            'protocol': ['KyberSwap V2']
        }
    },

    'STAKING': {
        'create_lock': {
            'direction': 'OUTGOING',
            'description': 'Lock tokens for voting rights',
            'method': '0x65fc3873',
            'protocol': ['Curve veCRV']
        },
        'increase_amount': {
            'direction': 'OUTGOING',
            'description': 'Increase locked amount',
            'method': '0x5ef8f675',
            'protocol': ['Curve veCRV']
        },
        'increase_unlock_time': {
            'direction': 'OUTGOING',
            'description': 'Extend lock duration',
            'method': '0xc27f24d2',
            'protocol': ['Curve veCRV']
        },
        'intendToUnstake': {
            'direction': 'OUTGOING',
            'description': 'Signal intention to unstake',
            'method': '0xc32f7f73',
            'protocol': ['Generic Staking']
        },
        'stakeRewards': {
            'direction': 'OUTGOING',
            'description': 'Stake reward tokens',
            'method': '0x8f31c7f9',
            'protocol': ['Generic Staking']
        }
    },

    'CLAIMS': {
        'claimAll': {
            'direction': 'INCOMING',
            'description': 'Claim all pending rewards',
            'method': '0x4e71d92d',
            'protocol': ['Generic Claims']
        },
        'claimBalance': {
            'direction': 'INCOMING',
            'description': 'Claim available balance',
            'method': '0x8f31c7f9',
            'protocol': ['Generic Claims']
        },
        'claimDistributions': {
            'direction': 'INCOMING',
            'description': 'Claim token distributions',
            'method': '0x9af6b617',
            'protocol': ['Generic Claims']
        },
        'claimFor': {
            'direction': 'INCOMING',
            'description': 'Claim rewards for another address',
            'method': '0x2f6c493c',
            'protocol': ['Generic Claims']
        },
        'claimStakerReward': {
            'direction': 'INCOMING',
            'description': 'Claim staking rewards',
            'method': '0x7c3b74a1',
            'protocol': ['Generic Staking']
        }
    },

    'DEPOSITS': {
        'depositPool': {
            'direction': 'OUTGOING',
            'description': 'Deposit into liquidity pool',
            'method': '0x43a0d066',
            'protocol': ['Generic Pools']
        },
        'depositSavings': {
            'direction': 'OUTGOING',
            'description': 'Deposit into savings protocol',
            'method': '0x234c0aa9',
            'protocol': ['Yield Protocols']
        },
        'depositV3': {
            'direction': 'OUTGOING',
            'description': 'Deposit assets in Aave V3',
            'method': '0xe8eda9df',
            'protocol': ['Aave V3']
        }
    },

    'WITHDRAWALS': {
        'withdrawAllBase': {
            'direction': 'INCOMING',
            'description': 'Withdraw all base tokens',
            'method': '0x1f1fcd51',
            'protocol': ['Generic Protocols']
        },
        'withdrawAllQuote': {
            'direction': 'INCOMING',
            'description': 'Withdraw all quote tokens',
            'method': '0x89b7daa9',
            'protocol': ['Generic Protocols']
        },
        'withdrawERC20For': {
            'direction': 'INCOMING',
            'description': 'Withdraw ERC20 tokens for another address',
            'method': '0x9e281a98',
            'protocol': ['Generic Protocols']
        },
        'withdrawFunds': {
            'direction': 'INCOMING',
            'description': 'Generic withdrawal function',
            'method': '0x24ed7740',
            'protocol': ['Generic Protocols']
        }
    },

    'MINTING': {
        'mintWithEther': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with ETH',
            'method': '0x90a56f37',
            'protocol': ['Generic Minting']
        },
        'mintWithToken': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with another token',
            'method': '0x8f31c7f9',
            'protocos': ['Generic Minting']
        }
    },

    'BURNING': {
        'burnToEther': {
            'direction': 'BOTH',
            'description': 'Burn tokens for ETH',
            'method': '0x3f7d753c',
            'protocol': ['Generic Burning']
        },
        'burnToToken': {
            'direction': 'BOTH',
            'description': 'Burn tokens for another token',
            'method': '0x7ebf1db5',
            'protocol': ['Generic Burning']
        }
    },

    'MIGRATION': {
        'migrateAll': {
            'direction': 'BOTH',
            'description': 'Migrate all assets',
            'method': '0x6e7cf85f',
            'protocol': ['Generic Migration']
        },
        'migrateFromLEND': {
            'direction': 'BOTH',
            'description': 'Migrate from LEND to AAVE token',
            'method': '0xd34a9e4a',
            'protocol': ['Aave V2']
        }
    },

    'GOVERNANCE': {
        'voteFor': {
            'direction': 'OUTGOING',
            'description': 'Cast vote for proposal',
            'method': '0x86a50535',
            'protocol': ['DAO Voting']
        },
        'user_checkpoint': {
            'direction': 'NEUTRAL',
            'description': 'Update user rewards checkpoint',
            'method': '0x4b820093',
            'protocol': ['Curve', 'Convex']
        }
    },

    'UTILITY': {
        'approveAndCall': {
            'direction': 'OUTGOING',
            'description': 'Approve and execute in one transaction',
            'method': '0xcae9ca51',
            'protocol': ['ERC20 Extended']
        },
        'build': {
            'direction': 'OUTGOING',
            'description': 'Build position',
            'method': '0x9d94c8b3',
            'protocol': ['Maker', 'Compound']
        },
        'disperseEther': {
            'direction': 'OUTGOING',
            'description': 'Disperse ETH to multiple addresses',
            'method': '0xe63d38ed',
            'protocol': ['Disperse.app']
        },
        'invalidateUnorderedNonces': {
            'direction': 'OUTGOING',
            'description': 'Invalidate unused nonces',
            'method': '0x9e7b8d61',
            'protocol': ['Security Protocols']
        }
    },

    'TRANSFERS': {
        'ETH transfer': {
            'direction': 'OUTGOING',
            'description': 'Native ETH transfer',
            'method': '0x',  #Native transfer has no method ID
            'protocol': ['Ethereum']
        }
    },
 
    'SUSPICIOUS': {
        'JunionYoutubeXD_dashhvetozhe': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
            'protocol': ['SUSPICIOUS']
        },
        'LetsInvest': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
            'protocol': ['SUSPICIOUS']
        }
    }
}


# Combined functions for all versions
PROTOCOL_FUNCTIONS = {
    'V1': PROTOCOL_FUNCTIONS
}