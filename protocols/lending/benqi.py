"""Benqi Protocol Functions for all versions"""

BENQI_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to the protocol',
                'method': '0x1249c58b'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets',
                'method': '0x2e1a7d4d'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets against collateral',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets',
                'method': '0x0e752702'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates undercollateralized positions',
                'method': '0xf0988da6'
            }
        },
        'STAKING': {
            'stake': {
                'direction': 'OUTGOING',
                'description': 'Stakes QI tokens',
                'method': '0xa694fc3a'
            },
            'unstake': {
                'direction': 'INCOMING',
                'description': 'Unstakes QI tokens',
                'method': '0x2e17de78'
            },
            'claimRewards': {
                'direction': 'INCOMING',
                'description': 'Claims staking rewards',
                'method': '0xe09c3b93'
            }
        },
        'GOVERNANCE': {
            'propose': {
                'direction': 'OUTGOING',
                'description': 'Creates governance proposal',
                'method': '0xda95691a'
            },
            'vote': {
                'direction': 'OUTGOING',
                'description': 'Votes on proposal',
                'method': '0x0121b93f'
            },
            'execute': {
                'direction': 'OUTGOING',
                'description': 'Executes proposal',
                'method': '0xfe0d94c1'
            }
        }
    }
}