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
            'protocols': ['Curve V1', 'Balancer V1']
        },
        'ZapOut2PairToken': {
            'direction': 'INCOMING',
            'description': 'Remove liquidity and convert to token pair',
            'method': '0x41f13681',
            'protocols': ['Zapper.fi']
        }
    },

    'SWAPS': {
        'swapExactETHForAlpha': {
            'direction': 'OUTGOING',
            'description': 'Swap exact ETH for Alpha token',
            'method': '0x7ff36ab5',
            'protocols': ['Uniswap V2']
        },
        'swapAndDeposit': {
            'direction': 'OUTGOING',
            'description': 'Swap token and deposit in one transaction',
            'method': '0x5a0c7376',
            'protocols': ['Compound', 'Aave V2']
        },
        'swapAndRepay': {
            'direction': 'OUTGOING',
            'description': 'Swap token and repay loan',
            'method': '0x2db1e36c',
            'protocols': ['Aave V2', 'Aave V3']
        },
        'swapAndSendV2': {
            'direction': 'BOTH',
            'description': 'Swap and send tokens to recipient',
            'method': '0x985d7a89',
            'protocols': ['1inch V2', 'ParaSwap']
        },
        'mixSwap': {
            'direction': 'BOTH',
            'description': 'Aggregated token swap',
            'method': '0x13240b31',
            'protocols': ['MixSwap', '1inch']
        },
        'tradeWithHint': {
            'direction': 'BOTH',
            'description': 'Trade with routing hint',
            'method': '0x6cf68693',
            'protocols': ['KyberSwap V2']
        },
        'tradeWithHintAndFee': {
            'direction': 'BOTH',
            'description': 'Trade with hint and fee structure',
            'method': '0xae591d54',
            'protocols': ['KyberSwap V2']
        }
    },

    'STAKING': {
        'create_lock': {
            'direction': 'OUTGOING',
            'description': 'Lock tokens for voting rights',
            'method': '0x65fc3873',
            'protocols': ['Curve veCRV']
        },
        'increase_amount': {
            'direction': 'OUTGOING',
            'description': 'Increase locked amount',
            'method': '0x5ef8f675',
            'protocols': ['Curve veCRV']
        },
        'increase_unlock_time': {
            'direction': 'OUTGOING',
            'description': 'Extend lock duration',
            'method': '0xc27f24d2',
            'protocols': ['Curve veCRV']
        },
        'intendToUnstake': {
            'direction': 'OUTGOING',
            'description': 'Signal intention to unstake',
            'method': '0xc32f7f73',
            'protocols': ['Generic Staking']
        },
        'stakeRewards': {
            'direction': 'OUTGOING',
            'description': 'Stake reward tokens',
            'method': '0x8f31c7f9',
            'protocols': ['Generic Staking']
        }
    },

    'CLAIMS': {
        'claimAll': {
            'direction': 'INCOMING',
            'description': 'Claim all pending rewards',
            'method': '0x4e71d92d',
            'protocols': ['Generic Claims']
        },
        'claimBalance': {
            'direction': 'INCOMING',
            'description': 'Claim available balance',
            'method': '0x8f31c7f9',
            'protocols': ['Generic Claims']
        },
        'claimDistributions': {
            'direction': 'INCOMING',
            'description': 'Claim token distributions',
            'method': '0x9af6b617',
            'protocols': ['Generic Claims']
        },
        'claimFor': {
            'direction': 'INCOMING',
            'description': 'Claim rewards for another address',
            'method': '0x2f6c493c',
            'protocols': ['Generic Claims']
        },
        'claimStakerReward': {
            'direction': 'INCOMING',
            'description': 'Claim staking rewards',
            'method': '0x7c3b74a1',
            'protocols': ['Generic Staking']
        }
    },

    'DEPOSITS': {
        'depositPool': {
            'direction': 'OUTGOING',
            'description': 'Deposit into liquidity pool',
            'method': '0x43a0d066',
            'protocols': ['Generic Pools']
        },
        'depositSavings': {
            'direction': 'OUTGOING',
            'description': 'Deposit into savings protocol',
            'method': '0x234c0aa9',
            'protocols': ['Yield Protocols']
        },
        'depositV3': {
            'direction': 'OUTGOING',
            'description': 'Deposit assets in Aave V3',
            'method': '0xe8eda9df',
            'protocols': ['Aave V3']
        }
    },

    'WITHDRAWALS': {
        'withdrawAllBase': {
            'direction': 'INCOMING',
            'description': 'Withdraw all base tokens',
            'method': '0x1f1fcd51',
            'protocols': ['Generic Protocols']
        },
        'withdrawAllQuote': {
            'direction': 'INCOMING',
            'description': 'Withdraw all quote tokens',
            'method': '0x89b7daa9',
            'protocols': ['Generic Protocols']
        },
        'withdrawERC20For': {
            'direction': 'INCOMING',
            'description': 'Withdraw ERC20 tokens for another address',
            'method': '0x9e281a98',
            'protocols': ['Generic Protocols']
        },
        'withdrawFunds': {
            'direction': 'INCOMING',
            'description': 'Generic withdrawal function',
            'method': '0x24ed7740',
            'protocols': ['Generic Protocols']
        }
    },

    'MINTING': {
        'mintWithEther': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with ETH',
            'method': '0x90a56f37',
            'protocols': ['Generic Minting']
        },
        'mintWithToken': {
            'direction': 'OUTGOING',
            'description': 'Mint tokens with another token',
            'method': '0x8f31c7f9',
            'protocols': ['Generic Minting']
        }
    },

    'BURNING': {
        'burnToEther': {
            'direction': 'BOTH',
            'description': 'Burn tokens for ETH',
            'method': '0x3f7d753c',
            'protocols': ['Generic Burning']
        },
        'burnToToken': {
            'direction': 'BOTH',
            'description': 'Burn tokens for another token',
            'method': '0x7ebf1db5',
            'protocols': ['Generic Burning']
        }
    },

    'MIGRATION': {
        'migrateAll': {
            'direction': 'BOTH',
            'description': 'Migrate all assets',
            'method': '0x6e7cf85f',
            'protocols': ['Generic Migration']
        },
        'migrateFromLEND': {
            'direction': 'BOTH',
            'description': 'Migrate from LEND to AAVE token',
            'method': '0xd34a9e4a',
            'protocols': ['Aave V2']
        }
    },

    'GOVERNANCE': {
        'voteFor': {
            'direction': 'OUTGOING',
            'description': 'Cast vote for proposal',
            'method': '0x86a50535',
            'protocols': ['DAO Voting']
        },
        'user_checkpoint': {
            'direction': 'NEUTRAL',
            'description': 'Update user rewards checkpoint',
            'method': '0x4b820093',
            'protocols': ['Curve', 'Convex']
        }
    },

    'UTILITY': {
        'approveAndCall': {
            'direction': 'OUTGOING',
            'description': 'Approve and execute in one transaction',
            'method': '0xcae9ca51',
            'protocols': ['ERC20 Extended']
        },
        'build': {
            'direction': 'OUTGOING',
            'description': 'Build position',
            'method': '0x9d94c8b3',
            'protocols': ['Maker', 'Compound']
        },
        'disperseEther': {
            'direction': 'OUTGOING',
            'description': 'Disperse ETH to multiple addresses',
            'method': '0xe63d38ed',
            'protocols': ['Disperse.app']
        },
        'invalidateUnorderedNonces': {
            'direction': 'OUTGOING',
            'description': 'Invalidate unused nonces',
            'method': '0x9e7b8d61',
            'protocols': ['Security Protocols']
        }
    },

    'TRANSFERS': {
        'ETH transfer': {
            'direction': 'OUTGOING',
            'description': 'Native ETH transfer',
            'method': '0x',  #Native transfer has no method ID
            'protocols': ['Ethereum']
        }
    },
 
    'SUSPICIOUS': {
        'JunionYoutubeXD_dashhvetozhe': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
            'protocols': ['SUSPICIOUS']
        },
        'LetsInvest': {
            'direction': 'UNKNOWN',
            'description': 'Suspicious function - potential scam',
            'method': 'UNKNOWN',
            'protocols': ['SUSPICIOUS']
        }
    }
}


