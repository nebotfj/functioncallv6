"""Aave Protocol Functions for all versions"""

AAVE_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'deposit': {
                'direction': 'OUTGOING',
                'description': 'Deposits tokens into the lending pool',
                'method': '0xe8eda9df'
            },
            'depositAave': {
                'direction': 'OUTGOING',
                'description': 'Deposits AAVE tokens into the protocol',
                'method': '0x47e7ef24'
            },
            'withdrawAave': {
                'direction': 'INCOMING',
                'description': 'Withdraws AAVE tokens from the protocol',
                'method': '0x69328dec'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems aTokens for underlying tokens',
                'method': '0xdb006a75'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows tokens from the lending pool',
                'method': '0xc858f5ba'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed tokens',
                'method': '0x5ceae9c4'
            },
            'liquidationCall': {
                'direction': 'BOTH',
                'description': 'Liquidates an unhealthy position',
                'method': '0x00a718a9'
            },
            'getUserReserveData': {
                'direction': 'OUTGOING',
                'description': 'Gets the user data for a specific reserve',
                'method': '0x28dd2d01'
            }
        }
    },
    'V2': {
        'LENDING': {
            'deposit': {
                'direction': 'OUTGOING',
                'description': 'Deposits an amount of underlying asset into the reserve',
                'method': '0xe8eda9df'
            },
            'depositAave': {
                'direction': 'OUTGOING',
                'description': 'Deposits AAVE tokens into the protocol',
                'method': '0x47e7ef24'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws an amount of underlying asset from the reserve',
                'method': '0x69328dec'
            },
            'withdrawAave': {
                'direction': 'INCOMING',
                'description': 'Withdraws AAVE tokens from the protocol',
                'method': '0x69328dec'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows an amount of asset with stable or variable rate',
                'method': '0xc858f5ba'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays a borrowed amount on the specific reserve',
                'method': '0x573ade81'
            },
            'swapBorrowRateMode': {
                'direction': 'BOTH',
                'description': 'Switches between stable and variable borrow rate',
                'method': '0x94ba89a2'
            },
            'rebalanceStableBorrowRate': {
                'direction': 'BOTH',
                'description': 'Rebalances the stable borrow rate of the user',
                'method': '0xcd112382'
            },
            'setUserUseReserveAsCollateral': {
                'direction': 'OUTGOING',
                'description': 'Enables/disables an asset as collateral',
                'method': '0x5a3b74b9'
            },
            'liquidationCall': {
                'direction': 'BOTH',
                'description': 'Liquidates an unhealthy position',
                'method': '0x00a718a9'
            },
            'flashLoan': {
                'direction': 'BOTH',
                'description': 'Executes a flash loan operation',
                'method': '0xab9c4b5d'
            },
            'initReserve': {
                'direction': 'OUTGOING',
                'description': 'Initializes a new reserve in the protocol',
                'method': '0x7a708e92'
            },
            'setReservePause': {
                'direction': 'OUTGOING',
                'description': 'Pauses or unpauses a reserve',
                'method': '0x48d9f693'
            }
        },
        'STAKING': {
            'stake': {
                'direction': 'OUTGOING',
                'description': 'Stakes tokens in the Safety Module',
                'method': '0xa694fc3a'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems staked tokens',
                'method': '0xdb006a75'
            }
        },
        'GOVERNANCE': {
            'delegateByType': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power of a specific type',
                'method': '0x0185f782'
            }
        }
    },
    'V3': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies an amount of underlying asset into the protocol',
                'method': '0x617ba037'
            },
            'depositAave': {
                'direction': 'OUTGOING',
                'description': 'Deposits AAVE tokens into the protocol',
                'method': '0x47e7ef24'
            },
            'supplyWithPermit': {
                'direction': 'OUTGOING',
                'description': 'Supplies with permit signature (no prior approve needed)',
                'method': '0x02c205f0'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws an amount of underlying asset',
                'method': '0x69328dec'
            },
            'withdrawAave': {
                'direction': 'INCOMING',
                'description': 'Withdraws AAVE tokens from the protocol',
                'method': '0x69328dec'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows an amount of asset with stable or variable rate',
                'method': '0xa415bcad'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays a borrowed amount',
                'method': '0x573ade81'
            },
            'repayWithPermit': {
                'direction': 'OUTGOING',
                'description': 'Repays with permit signature',
                'method': '0x94b576de'
            },
            'repayWithATokens': {
                'direction': 'OUTGOING',
                'description': 'Repays borrow using aTokens',
                'method': '0x2dad97d4'
            },
            'swapBorrowRateMode': {
                'direction': 'BOTH',
                'description': 'Switches between stable and variable borrow rate',
                'method': '0x94ba89a2'
            },
            'rebalanceStableBorrowRate': {
                'direction': 'BOTH',
                'description': 'Rebalances the stable borrow rate of the user',
                'method': '0xcd112382'
            },
            'setUserUseReserveAsCollateral': {
                'direction': 'OUTGOING',
                'description': 'Enables/disables an asset as collateral',
                'method': '0x5a3b74b9'
            },
            'liquidationCall': {
                'direction': 'BOTH',
                'description': 'Liquidates an unhealthy position',
                'method': '0x00a718a9'
            },
            'flashLoan': {
                'direction': 'BOTH',
                'description': 'Executes a flash loan operation',
                'method': '0xab9c4b5d'
            },
            'flashLoanSimple': {
                'direction': 'BOTH',
                'description': 'Executes a simple flash loan of one asset',
                'method': '0x42b0b77c'
            },
            'mintUnbacked': {
                'direction': 'OUTGOING',
                'description': 'Mints unbacked aTokens to bridge liquidity',
                'method': '0x69a933a5'
            },
            'backUnbacked': {
                'direction': 'OUTGOING',
                'description': 'Backs previously unbacked aTokens with collateral',
                'method': '0xd65dc7a1'
            },
            'supplyWithPermitSignature': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets using EIP-2612 permit',
                'method': '0x680dd47c'
            },
            'borrowWithPermitSignature': {
                'direction': 'INCOMING',
                'description': 'Borrows using EIP-2612 permit',
                'method': '0x1a8d3acd'
            },
            'encodeTokenPermit': {
                'direction': 'OUTGOING',
                'description': 'Encodes permit data for token approvals',
                'method': '0x87d45c33'
            },
            'encodeDelegationPermit': {
                'direction': 'OUTGOING',
                'description': 'Encodes permit data for credit delegation',
                'method': '0x2d4aafc4'
            }
        },
        'STAKING': {
            'stake': {
                'direction': 'OUTGOING',
                'description': 'Stakes tokens in the Safety Module',
                'method': '0xa694fc3a'
            },
            'unstake': {
                'direction': 'INCOMING',
                'description': 'Unstakes tokens from Safety Module',
                'method': '0x3d02c422'
            },
            'cooldown': {
                'direction': 'OUTGOING',
                'description': 'Activates the cooldown period',
                'method': '0x7fb52f1a'
            },
            'claimRewards': {
                'direction': 'INCOMING',
                'description': 'Claims accumulated rewards',
                'method': '0xe6f1daf2'
            },
            'claimRewardsOnBehalf': {
                'direction': 'OUTGOING',
                'description': 'Claims rewards on behalf of a user',
                'method': '0x6d34b96e'
            },
            'claimRewardsAndStake': {
                'direction': 'BOTH',
                'description': 'Claims and automatically stakes rewards',
                'method': '0x9a5c32e7'
            }
        },
        'GOVERNANCE': {
            'submitVote': {
                'direction': 'OUTGOING',
                'description': 'Submits vote on proposal',
                'method': '0x612c56fa'
            },
            'delegate': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power',
                'method': '0x5c19a95c'
            },
            'proposalCreate': {
                'direction': 'OUTGOING',
                'description': 'Creates new governance proposal',
                'method': '0x7d5e81e2'
            },
            'queueTransaction': {
                'direction': 'OUTGOING',
                'description': 'Queues successful proposal',
                'method': '0x3a66f901'
            },
            'executeTransaction': {
                'direction': 'OUTGOING',
                'description': 'Executes queued proposal',
                'method': '0x0825f38f'
            },
            'delegateByType': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power by type (proposition or voting)',
                'method': '0x0185f782'
            },
            'delegateWithSig': {
                'direction': 'OUTGOING',
                'description': 'Delegates with signature (gasless)',
                'method': '0x7f4f3e52'
            },
            'submitVoteBySignature': {
                'direction': 'OUTGOING',
                'description': 'Submits vote using signature (gasless)',
                'method': '0x9a802a6d'
            }
        }
    }
}