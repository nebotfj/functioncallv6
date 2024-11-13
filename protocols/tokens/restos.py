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
        },
    },
    'BASIC': {
    # ... existing code ...
        'approve': {
            'direction': 'OUTGOING',
            'description': 'Approves address to spend tokens',
            'method': '0x095ea7b3',
            'app': 'ERC20_STANDARD'
        }
    },
    'OPERATOR': {
        'setOperator': {
            'direction': 'OUTGOING',
            'description': 'Sets operator permission status',
            'method': '0x8e1a55fc',
            'app': 'KYBER_NETWORK'  # Comúnmente usado en Kyber
        },
        'addOperator': {
            'direction': 'OUTGOING',
            'description': 'Adds new operator address',
            'method': '0xf39b5b9b',
            'app': 'KYBER_NETWORK'  # Comúnmente usado en Kyber
        }
    },
    'EMERGENCY': {
        'startEmergencyShutdown': {
            'direction': 'OUTGOING',
            'description': 'Initiates emergency shutdown procedure',
            'method': '0xddf7e1a7',
            'app': 'MAKER'  # Usado en MakerDAO
        }
    },
    'EXECUTION': {
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes batch of calls with value',
            'method': '0xc2998238',
            'app': 'GENERAL'  # Usado en varios protocolos
        }
    },
    'ORDERS': {
        'cancelOrder': {
            'direction': 'OUTGOING',
            'description': 'Cancels existing order',
            'method': '0xf3541901',
            'app': '0X_PROTOCOL'  # Comúnmente usado en 0x Protocol
        }
    },
    'MINTING': {
        'mintWithAmount': {
            'direction': 'OUTGOING',
            'description': 'Mints tokens with amount',
            'method': '0xa0712d68',
            'app': 'GENERAL'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints tokens',
            'method': '0x1249c58b',
            'app': 'GENERAL'
        }
    },
    'LENDING': {
        'redeem': {
            'direction': 'OUTGOING',
            'description': 'Redeems tokens',
            'method': '0xc5ebeaec',
            'app': 'COMPOUND'
        },
        'repay': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed amount',
            'method': '0x852a12e3',
            'app': 'GENERAL_LENDING'
        },
        'redeemWithAmount': {
            'direction': 'OUTGOING',
            'description': 'Redeems tokens with multiple parameters',
            'method': '0xdb006a75',
            'app': 'GENERAL_LENDING'
        },
        'redeemUnderlying': {
            'direction': 'OUTGOING',
            'description': 'Redeems underlying asset',
            'method': '0xd2d0e066',
            'app': 'COMPOUND'
        },
        'getLendingPool': {
            'direction': 'VIEW',
            'description': 'Gets lending pool address',
            'method': '0x6b1d4db7',
            'app': 'AAVE'
        }
    },
    'ACCESS_CONTROL': {
        'removeOperator': {
            'direction': 'OUTGOING',
            'description': 'Removes operator permissions',
            'method': '0x4e07008d',
            'app': 'GENERAL'
        },
        'removeFromWhitelist': {
            'direction': 'OUTGOING',
            'description': 'Removes address from whitelist',
            'method': '0x546cb17e',
            'app': 'GENERAL'
        },
        'addToWhitelist': {
            'direction': 'OUTGOING',
            'description': 'Adds address to whitelist',
            'method': '0x4254b155',
            'app': 'GENERAL'
        }
    },
    'TRADING': {
        'startTrading': {
            'direction': 'OUTGOING',
            'description': 'Initiates trading functionality',
            'method': '0x0bde6eb7',
            'app': 'GENERAL_DEX'
        }
    },
    'TOKEN_MANAGEMENT': {
        'increaseAllowance': {
            'direction': 'OUTGOING',
            'description': 'Increases token allowance',
            'method': '0x39039497',
            'app': 'ERC20_EXTENSION'
        }
    },
    'TRANSFER': {
        'transfer': {
            'direction': 'OUTGOING',
            'description': 'Transfers tokens to address',
            'method': '0xa9059cbb',
            'app': 'ERC20_STANDARD'
        },
    },
    'EXECUTION': {
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes arbitrary code through proxy',
            'method': '0x1cff79cd',
            'app': 'MAKER_DSPROXY'
        }
    },
    'MINTING': {
        'mintTo': {
            'direction': 'OUTGOING',
            'description': 'Mints tokens to specific address',
            'method': '0x40c10f19',
            'app': 'GENERAL'
        }
    },
    'BURNING': {
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns tokens from address',
            'method': '0x9dc29fac',
            'app': 'GENERAL'
        }
    },
    'DEPOSIT': {
        'deposit': {
            'direction': 'INCOMING',
            'description': 'Deposits ETH',
            'method': '0xd0e30db0',
            'app': 'WETH'
        }
    },
    'WITHDRAW': {
        'withdraw': {
            'direction': 'OUTGOING',
            'description': 'Withdraws ETH',
            'method': '0x3ccfd60b',
            'app': 'GENERAL'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0x0b4c7e4d',
            'app': 'GENERAL_STAKING'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0x8059cf3b',
            'app': 'GENERAL_DAO'
        },
        'castVote': {
            'direction': 'OUTGOING',
            'description': 'Casts vote on proposal',
            'method': '0x48ca1300',
            'app': 'GENERAL_DAO'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0x82fef45',
            'app': 'GENERAL_DEX'
        },
        'removeLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Removes liquidity from pool',
            'method': '0xfbabdebd',
            'app': 'GENERAL_DEX'
        }
    },
    'REWARDS': {
        'claimRewards': {
            'direction': 'OUTGOING',
            'description': 'Claims accumulated rewards',
            'method': '0x29589f61',
            'app': 'GENERAL'
        },
        'getReward': {
            'direction': 'OUTGOING',
            'description': 'Claims reward tokens',
            'method': '0x8f6ede1f',
            'app': 'GENERAL'
        }
    },
    'POOL_MANAGEMENT': {
        'configurePool': {
            'direction': 'OUTGOING',
            'description': 'Configures pool parameters',
            'method': '0x81a6b250',
            'app': 'GENERAL_DEX'
        },
        'setPoolParameters': {
            'direction': 'OUTGOING',
            'description': 'Sets pool parameters',
            'method': '0x5a3b74b9',
            'app': 'GENERAL_DEX'
        }
    },
    'ORACLE': {
        'updatePrice': {
            'direction': 'OUTGOING',
            'description': 'Updates price feed',
            'method': '0x95e3c50b',
            'app': 'GENERAL_ORACLE'
        },
        'setPrice': {
            'direction': 'OUTGOING',
            'description': 'Sets asset price',
            'method': '0x422f1043',
            'app': 'GENERAL_ORACLE'
        }
    },
    'BRIDGE': {
        'bridgeTokens': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens cross-chain',
            'method': '0x03152429',
            'app': 'GENERAL_BRIDGE'
        }
    },
    'FARMING': {
        'harvest': {
            'direction': 'OUTGOING',
            'description': 'Harvests farming rewards',
            'method': '0xf88bf15a',
            'app': 'GENERAL_FARMING'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0xf88309d7',
            'app': 'GENERAL_FARMING'
        }
    },
    'COLLATERAL': {
        'depositCollateral': {
            'direction': 'OUTGOING',
            'description': 'Deposits collateral',
            'method': '0xa67a6a45',
            'app': 'GENERAL_LENDING'
        },
        'withdrawCollateral': {
            'direction': 'OUTGOING',
            'description': 'Withdraws collateral',
            'method': '0xab832b43',
            'app': 'GENERAL_LENDING'
        }
    },
    'SWAP': {
        'swapExactTokensForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact amount of tokens',
            'method': '0x23440944',
            'app': 'GENERAL_DEX'
        },
        'swap': {
            'direction': 'OUTGOING',
            'description': 'Performs token swap',
            'method': '0xc858f5f9',
            'app': 'GENERAL_DEX'
        }
    },
    'FEES': {
        'collectFees': {
            'direction': 'OUTGOING',
            'description': 'Collects accumulated fees',
            'method': '0x5ceae9c4',
            'app': 'GENERAL'
        },
        'claimFees': {
            'direction': 'OUTGOING',
            'description': 'Claims protocol fees',
            'method': '0xfc6f4e16',
            'app': 'GENERAL'
        }
    },
    'FLASH_LOAN': {
        'flashLoan': {
            'direction': 'OUTGOING',
            'description': 'Executes flash loan',
            'method': '0x34e7a19f',
            'app': 'GENERAL_LENDING'
        }
    },
    'EMERGENCY': {
        'emergencyWithdraw': {
            'direction': 'OUTGOING',
            'description': 'Emergency withdrawal of funds',
            'method': '0x02cce70b',
            'app': 'GENERAL'
        }
    },
    'SWAP': {
        'swapExactTokensForTokensSupportingFeeOnTransferTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact tokens with fee support',
            'method': '0x38ed1739',
            'app': 'UNISWAP_V2'
        },
        'swapExactETHForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact ETH for tokens',
            'method': '0xf305d719',
            'app': 'UNISWAP_V2'
        }
    },
    'GOVERNANCE': {
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c',
            'app': 'COMPOUND_GOVERNANCE'
        },
        'exitMarket': {
            'direction': 'OUTGOING',
            'description': 'Exits a market',
            'method': '0xe9fad8ee',
            'app': 'COMPOUND'
        }
    },
    'LENDING': {
        'enterMarkets': {
            'direction': 'OUTGOING',
            'description': 'Enters lending markets',
            'method': '0xc2998238',
            'app': 'COMPOUND'
        },
        'liquidateBorrow': {
            'direction': 'OUTGOING',
            'description': 'Liquidates a borrow position',
            'method': '0x1e83409a',
            'app': 'COMPOUND'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xb02f0b73',
            'app': 'GENERAL_STAKING'
        },
        'unstake': {
            'direction': 'OUTGOING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x6cfd80c9',
            'app': 'GENERAL_STAKING'
        }
    },
    'REWARDS': {
        'claimReward': {
            'direction': 'OUTGOING',
            'description': 'Claims staking rewards',
            'method': '0x517a55a3',
            'app': 'GENERAL_STAKING'
        },
        'getRewardForDuration': {
            'direction': 'VIEW',
            'description': 'Gets reward amount for period',
            'method': '0xe9af0292',
            'app': 'SYNTHETIX'
        }
    },
    'POOL': {
        'initializePool': {
            'direction': 'OUTGOING',
            'description': 'Initializes new pool',
            'method': '0x77f61403',
            'app': 'GENERAL_DEX'
        },
        'setPoolParameters': {
            'direction': 'OUTGOING',
            'description': 'Updates pool parameters',
            'method': '0x4515cef3',
            'app': 'GENERAL_DEX'
        }
    },
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into vault',
            'method': '0xb384abef',
            'app': 'YEARN'
        },
        'withdraw': {
            'direction': 'OUTGOING',
            'description': 'Withdraws assets from vault',
            'method': '0x2cefff96',
            'app': 'YEARN'
        }
    },
    'ORACLE': {
        'updatePrice': {
            'direction': 'OUTGOING',
            'description': 'Updates asset price',
            'method': '0x7891c043',
            'app': 'CHAINLINK'
        },
        'getLatestPrice': {
            'direction': 'VIEW',
            'description': 'Gets latest price feed',
            'method': '0x3d18b912',
            'app': 'CHAINLINK'
        }
    },
    'BRIDGE': {
        'bridgeAssets': {
            'direction': 'OUTGOING',
            'description': 'Bridges assets cross-chain',
            'method': '0x029b2f34',
            'app': 'GENERAL_BRIDGE'
        },
        'completeBridging': {
            'direction': 'OUTGOING',
            'description': 'Completes bridge transaction',
            'method': '0xbb7e70ef',
            'app': 'GENERAL_BRIDGE'
        }
    },
    'FARMING': {
        'harvest': {
            'direction': 'OUTGOING',
            'description': 'Harvests farming rewards',
            'method': '0x1aa3a008',
            'app': 'GENERAL_FARMING'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds farming rewards',
            'method': '0x53fa2eb7',
            'app': 'GENERAL_FARMING'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to pool',
            'method': '0x0e752702',
            'app': 'GENERAL_DEX'
        },
        'removeLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Removes liquidity from pool',
            'method': '0x75d9aa1a',
            'app': 'GENERAL_DEX'
        }
    },
    'SYSTEM': {
        'pause': {
            'direction': 'OUTGOING',
            'description': 'Pauses contract functionality',
            'method': '0x415565b0',
            'app': 'GENERAL'
        },
        'unpause': {
            'direction': 'OUTGOING',
            'description': 'Unpauses contract functionality',
            'method': '0xe0e90acf',
            'app': 'GENERAL'
        }
    },
    'ACCESS_CONTROL': {
        'grantRole': {
            'direction': 'OUTGOING',
            'description': 'Grants role to address',
            'method': '0xee857b69',
            'app': 'GENERAL'
        },
        'revokeRole': {
            'direction': 'OUTGOING',
            'description': 'Revokes role from address',
            'method': '0xde5f6268',
            'app': 'GENERAL'
        }
    },
    'CONFIGURATION': {
        'setConfig': {
            'direction': 'OUTGOING',
            'description': 'Sets protocol configuration',
            'method': '0xd7136328',
            'app': 'GENERAL'
        },
        'updateConfig': {
            'direction': 'OUTGOING',
            'description': 'Updates protocol configuration',
            'method': '0xa453b6cf',
            'app': 'GENERAL'
        }
    },
    'EMERGENCY': {
        'emergencyExit': {
            'direction': 'OUTGOING',
            'description': 'Initiates emergency exit',
            'method': '0xe2b39746',
            'app': 'GENERAL'
        },
        'emergencyWithdraw': {
            'direction': 'OUTGOING',
            'description': 'Emergency withdrawal of funds',
            'method': '0x4b820093',
            'app': 'GENERAL'
        }
    },
    'FEES': {
        'setFees': {
            'direction': 'OUTGOING',
            'description': 'Sets protocol fees',
            'method': '0x1e9a6950',
            'app': 'GENERAL'
        },
        'collectFees': {
            'direction': 'OUTGOING',
            'description': 'Collects accumulated fees',
            'method': '0x46ab38f1',
            'app': 'GENERAL'
        }
    },
    'MIGRATION': {
        'migrate': {
            'direction': 'OUTGOING',
            'description': 'Migrates to new version',
            'method': '0x7d49d875',
            'app': 'GENERAL'
        },
        'setMigrator': {
            'direction': 'OUTGOING',
            'description': 'Sets migrator contract',
            'method': '0x6a627842',
            'app': 'GENERAL'
        }
    },
    'UNISWAP': {
        'swapExactTokensForETH': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact tokens for ETH',
            'method': '0x18cbafe5',
            'app': 'UNISWAP_V2'
        },
        'swapExactETHForTokensSupportingFeeOnTransferTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps ETH for tokens with fee support',
            'method': '0x7ff36ab5',
            'app': 'UNISWAP_V2'
        }
    },
    'MASTERCHEF': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits LP tokens for farming',
            'method': '0xe2bbb158',
            'app': 'SUSHISWAP'
        },
        'withdraw': {
            'direction': 'OUTGOING',
            'description': 'Withdraws LP tokens from farming',
            'method': '0x2e95b6c8',
            'app': 'SUSHISWAP'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xeff7a612',
            'app': 'GENERAL_STAKING'
        },
        'unstake': {
            'direction': 'OUTGOING',
            'description': 'Unstakes tokens from protocol',
            'method': '0xdf133bca',
            'app': 'GENERAL_STAKING'
        }
    },
    'LENDING': {
        'borrow': {
            'direction': 'OUTGOING',
            'description': 'Borrows assets from lending pool',
            'method': '0x3df02124',
            'app': 'GENERAL_LENDING'
        },
        'repayBorrow': {
            'direction': 'OUTGOING',
            'description': 'Repays borrowed assets',
            'method': '0x61b69abd',
            'app': 'COMPOUND'
        }
    },
    'LIQUIDITY': {
        'addLiquidityETH': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity with ETH',
            'method': '0x2e7ba6ef',
            'app': 'GENERAL_DEX'
        },
        'removeLiquidityETH': {
            'direction': 'OUTGOING',
            'description': 'Removes liquidity with ETH',
            'method': '0x1a4d01d2',
            'app': 'GENERAL_DEX'
        }
    },
    'REWARDS': {
        'getReward': {
            'direction': 'OUTGOING',
            'description': 'Claims staking rewards',
            'method': '0xae591d54',
            'app': 'GENERAL_STAKING'
        },
        'harvestRewards': {
            'direction': 'OUTGOING',
            'description': 'Harvests farming rewards',
            'method': '0x8fd3ab80',
            'app': 'GENERAL_FARMING'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0x682356c0',
            'app': 'GENERAL_DAO'
        },
        'castVote': {
            'direction': 'OUTGOING',
            'description': 'Casts vote on proposal',
            'method': '0xadc9772e',
            'app': 'GENERAL_DAO'
        }
    },
    'VAULT': {
        'depositAll': {
            'direction': 'OUTGOING',
            'description': 'Deposits all tokens into vault',
            'method': '0x9a99b4f0',
            'app': 'YEARN'
        },
        'withdrawAll': {
            'direction': 'OUTGOING',
            'description': 'Withdraws all tokens from vault',
            'method': '0x853828b6',
            'app': 'YEARN'
        }
    },
    'PAYMENT': {
        'pay': {
            'direction': 'OUTGOING',
            'description': 'Makes payment in tokens',
            'method': '0x27bed8ee',
            'app': 'GENERAL'
        },
        'receive': {
            'direction': 'INCOMING',
            'description': 'Receives payment in tokens',
            'method': '0x47e7ef24',
            'app': 'GENERAL'
        }
    },
    'ORACLE': {
        'updateOracle': {
            'direction': 'OUTGOING',
            'description': 'Updates oracle price feed',
            'method': '0xf3ae6c5f',
            'app': 'GENERAL_ORACLE'
        },
        'getPrice': {
            'direction': 'VIEW',
            'description': 'Gets current price from oracle',
            'method': '0xd1058e59',
            'app': 'GENERAL_ORACLE'
        }
    },
    'BRIDGE': {
        'bridgeTokens': {
            'direction': 'OUTGOING',
            'description': 'Bridges tokens cross-chain',
            'method': '0xfa09e630',
            'app': 'GENERAL_BRIDGE'
        },
        'claimBridgedTokens': {
            'direction': 'OUTGOING',
            'description': 'Claims bridged tokens',
            'method': '0xc59203af',
            'app': 'GENERAL_BRIDGE'
        }
    },
    'FARMING': {
        'depositFarm': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens into farm',
            'method': '0x787a08a6',
            'app': 'GENERAL_FARMING'
        },
        'withdrawFarm': {
            'direction': 'OUTGOING',
            'description': 'Withdraws tokens from farm',
            'method': '0xc804c39a',
            'app': 'GENERAL_FARMING'
        }
    },
    'POOL': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Joins liquidity pool',
            'method': '0xded9382a',
            'app': 'BALANCER'
        },
        'exitPool': {
            'direction': 'OUTGOING',
            'description': 'Exits liquidity pool',
            'method': '0xe4a76726',
            'app': 'BALANCER'
        }
    },
    'SYSTEM': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes contract',
            'method': '0x05ea4671',
            'app': 'GENERAL'
        },
        'upgrade': {
            'direction': 'OUTGOING',
            'description': 'Upgrades contract implementation',
            'method': '0x21ef328f',
            'app': 'GENERAL'
        }
    },
    'CONFIGURATION': {
        'setConfig': {
            'direction': 'OUTGOING',
            'description': 'Sets protocol configuration',
            'method': '0xae0b51df',
            'app': 'GENERAL'
        },
        'updateParams': {
            'direction': 'OUTGOING',
            'description': 'Updates protocol parameters',
            'method': '0x90411a32',
            'app': 'GENERAL'
        }
    },
    'EMERGENCY': {
        'pause': {
            'direction': 'OUTGOING',
            'description': 'Pauses protocol',
            'method': '0x3049105d',
            'app': 'GENERAL'
        },
        'unpause': {
            'direction': 'OUTGOING',
            'description': 'Unpauses protocol',
            'method': '0xdb0cd51d',
            'app': 'GENERAL'
        }
    },
    'NFT': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new NFT',
            'method': '0x0e89439b',
            'app': 'GENERAL_NFT'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns existing NFT',
            'method': '0x2195995c',
            'app': 'GENERAL_NFT'
        }
    },
    'MIGRATION': {
        'migrate': {
            'direction': 'OUTGOING',
            'description': 'Migrates to new version',
            'method': '0xd47eaa37',
            'app': 'GENERAL'
        },
        'prepareMigration': {
            'direction': 'OUTGOING',
            'description': 'Prepares for migration',
            'method': '0x94bf804d',
            'app': 'GENERAL'
        }
    },
    'ACCESS': {
        'grantAccess': {
            'direction': 'OUTGOING',
            'description': 'Grants access to address',
            'method': '0x5915d806',
            'app': 'GENERAL'
        },
        'revokeAccess': {
            'direction': 'OUTGOING',
            'description': 'Revokes access from address',
            'method': '0x2e17de78',
            'app': 'GENERAL'
        }
    },
    'UNISWAP_V3': {
        'multicall': {
            'direction': 'OUTGOING',
            'description': 'Executes multiple calls in single transaction',
            'method': '0x5ae401dc',
            'app': 'UNISWAP_V3'
        },
        'exactInputSingle': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact tokens for tokens',
            'method': '0x414bf389',
            'app': 'UNISWAP_V3'
        }
    },
    'NFT': {
        'safeTransferFrom': {
            'direction': 'OUTGOING',
            'description': 'Safely transfers NFT',
            'method': '0x42842e0e',
            'app': 'ERC721'
        },
        'setApprovalForAll': {
            'direction': 'OUTGOING',
            'description': 'Sets approval for all tokens',
            'method': '0xa22cb465',
            'app': 'ERC721'
        }
    },
    'CURVE': {
        'exchange': {
            'direction': 'OUTGOING',
            'description': 'Exchanges tokens through Curve',
            'method': '0x3593564c',
            'app': 'CURVE'
        },
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to Curve pool',
            'method': '0x0b4c7e4d',
            'app': 'CURVE'
        }
    },
    'AAVE': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets into Aave',
            'method': '0xe8eda9df',
            'app': 'AAVE'
        },
        'borrow': {
            'direction': 'OUTGOING',
            'description': 'Borrows assets from Aave',
            'method': '0xc858f5f9',
            'app': 'AAVE'
        }
    },
    'COMPOUND': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints cTokens',
            'method': '0xa0712d68',
            'app': 'COMPOUND'
        },
        'redeem': {
            'direction': 'OUTGOING',
            'description': 'Redeems cTokens',
            'method': '0xdb006a75',
            'app': 'COMPOUND'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0x7b939232',
            'app': 'GENERAL_DAO'
        },
        'queue': {
            'direction': 'OUTGOING',
            'description': 'Queues proposal for execution',
            'method': '0xddf0b009',
            'app': 'GENERAL_DAO'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xa694fc3a',
            'app': 'GENERAL_STAKING'
        },
        'withdraw': {
            'direction': 'OUTGOING',
            'description': 'Withdraws staked tokens',
            'method': '0x2e1a7d4d',
            'app': 'GENERAL_STAKING'
        }
    },
    'BALANCER': {
        'joinPool': {
            'direction': 'OUTGOING',
            'description': 'Joins Balancer pool',
            'method': '0x4f69c0d4',
            'app': 'BALANCER'
        },
        'exitPool': {
            'direction': 'OUTGOING',
            'description': 'Exits Balancer pool',
            'method': '0x8bdb3913',
            'app': 'BALANCER'
        }
    },
    'SYSTEM': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes contract',
            'method': '0x485cc955',
            'app': 'GENERAL'
        },
        'upgrade': {
            'direction': 'OUTGOING',
            'description': 'Upgrades contract implementation',
            'method': '0x0900f010',
            'app': 'GENERAL'
        }
    },
    'REWARDS': {
        'getReward': {
            'direction': 'OUTGOING',
            'description': 'Claims rewards',
            'method': '0x3d18b912',
            'app': 'GENERAL_STAKING'
        },
        'notifyRewardAmount': {
            'direction': 'OUTGOING',
            'description': 'Updates reward amount',
            'method': '0x3c6b16ab',
            'app': 'GENERAL_STAKING'
        }
    },
    'ORACLE': {
        'setPrice': {
            'direction': 'OUTGOING',
            'description': 'Sets asset price',
            'method': '0x91b7f5ed',
            'app': 'GENERAL_ORACLE'
        },
        'getPrice': {
            'direction': 'VIEW',
            'description': 'Gets current price',
            'method': '0x98d5fdca',
            'app': 'GENERAL_ORACLE'
        }
    },
    'BRIDGE': {
        'relay': {
            'direction': 'OUTGOING',
            'description': 'Relays cross-chain message',
            'method': '0xc2fb26a6',
            'app': 'GENERAL_BRIDGE'
        },
        'processMessage': {
            'direction': 'OUTGOING',
            'description': 'Processes bridged message',
            'method': '0x9e2262f5',
            'app': 'GENERAL_BRIDGE'
        }
    },
    'NFT': {
        'setApprovalForAll': {
            'direction': 'OUTGOING',
            'description': 'Sets approval for all tokens',
            'method': '0xa22cb465',
            'app': 'ERC721'
        },
        'transferFrom': {
            'direction': 'OUTGOING',
            'description': 'Transfers token from address',
            'method': '0x23b872dd',
            'app': 'ERC721'
        }
    },
    'UNISWAP_V2': {
        'swapExactTokensForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact amount of tokens',
            'method': '0x38ef3649',
            'app': 'UNISWAP_V2'
        },
        'swapExactETHForTokens': {
            'direction': 'OUTGOING',
            'description': 'Swaps exact ETH for tokens',
            'method': '0xfb3bdb41',
            'app': 'UNISWAP_V2'
        }
    },
    'SYSTEM': {
        'initialize': {
            'direction': 'OUTGOING',
            'description': 'Initializes contract',
            'method': '0x2cc4081e',
            'app': 'GENERAL'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes contract call',
            'method': '0xb61d27f6',
            'app': 'GENERAL'
        }
    },
    'DATA': {
        'setData': {
            'direction': 'OUTGOING',
            'description': 'Sets contract data',
            'method': '0x64617461',
            'app': 'GENERAL'
        },
        'getData': {
            'direction': 'VIEW',
            'description': 'Gets contract data',
            'method': '0x3f6dc453',
            'app': 'GENERAL'
        }
    },
    'GOVERNANCE': {
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0x89afcb44',
            'app': 'GENERAL_DAO'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Casts vote',
            'method': '0x0ec32977',
            'app': 'GENERAL_DAO'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xb88a802f',
            'app': 'GENERAL_STAKING'
        },
        'withdraw': {
            'direction': 'OUTGOING',
            'description': 'Withdraws staked tokens',
            'method': '0x2e4dbe8f',
            'app': 'GENERAL_STAKING'
        }
    },
    'ACCESS_CONTROL': {
        'grantRole': {
            'direction': 'OUTGOING',
            'description': 'Grants role to address',
            'method': '0x2f52ebb7',
            'app': 'GENERAL'
        },
        'revokeRole': {
            'direction': 'OUTGOING',
            'description': 'Revokes role from address',
            'method': '0xd547741f',
            'app': 'GENERAL'
        }
    },
    'BRIDGE': {
        'bridge': {
            'direction': 'OUTGOING',
            'description': 'Bridges assets',
            'method': '0x9caf2b97',
            'app': 'GENERAL_BRIDGE'
        },
        'claim': {
            'direction': 'OUTGOING',
            'description': 'Claims bridged assets',
            'method': '0x4e71d92d',
            'app': 'GENERAL_BRIDGE'
        },
    }
}

# Combined functions for all versions
ETH_GENERIC = {
    'ETH_GENERIC': ETH_GENERIC_FUNCTIONS
}