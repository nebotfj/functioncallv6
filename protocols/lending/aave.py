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
                'description': 'Delegates voting power by type',
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
            'supplyWithPermit': {
                'direction': 'OUTGOING',
                'description': 'Supplies with permit signature',
                'method': '0x02c205f0'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws an amount of underlying asset',
                'method': '0x69328dec'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows an amount of asset',
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
                'description': 'Switches between stable and variable rate',
                'method': '0x94ba89a2'
            },
            'rebalanceStableBorrowRate': {
                'direction': 'BOTH',
                'description': 'Rebalances stable borrow rate',
                'method': '0xcd112382'
            },
            'setUserUseReserveAsCollateral': {
                'direction': 'OUTGOING',
                'description': 'Enables/disables asset as collateral',
                'method': '0x5a3b74b9'
            },
            'liquidationCall': {
                'direction': 'BOTH',
                'description': 'Liquidates unhealthy position',
                'method': '0x00a718a9'
            },
            'flashLoan': {
                'direction': 'BOTH',
                'description': 'Executes flash loan',
                'method': '0xab9c4b5d'
            },
            'flashLoanSimple': {
                'direction': 'BOTH',
                'description': 'Executes simple flash loan',
                'method': '0x42b0b77c'
            }
        },
        'STAKING': {
            'stake': {
                'direction': 'OUTGOING',
                'description': 'Stakes tokens in Safety Module',
                'method': '0xa694fc3a'
            },
            'unstake': {
                'direction': 'INCOMING',
                'description': 'Unstakes tokens',
                'method': '0x3d02c422'
            },
            'claimRewards': {
                'direction': 'INCOMING',
                'description': 'Claims rewards',
                'method': '0xe6f1daf2'
            }
        }
    }
}