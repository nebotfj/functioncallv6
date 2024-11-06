"""Goldfinch Protocol Functions for all versions"""

GOLDFINCH_V1_FUNCTIONS = {
    'LENDING': {
        'createLoan': {
            'direction': 'OUTGOING',
            'description': 'Creates new loan',
            'method': '0x1698ee82'
        },
        'fundLoan': {
            'direction': 'OUTGOING',
            'description': 'Funds approved loan',
            'method': '0x47e7ef24'
        },
        'repayLoan': {
            'direction': 'OUTGOING',
            'description': 'Repays active loan',
            'method': '0x573ade81'
        },
        'claimRepayment': {
            'direction': 'INCOMING',
            'description': 'Claims loan repayment',
            'method': '0x4e71d92d'
        },
        'assessLoan': {
            'direction': 'OUTGOING',
            'description': 'Assesses loan application',
            'method': '0x7535d246'
        }
    },
    'POOLS': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into senior pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from senior pool',
            'method': '0x69328dec'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes pool tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes pool tokens',
            'method': '0x2e1a7d4d'
        },
        'claimPoolRewards': {
            'direction': 'INCOMING',
            'description': 'Claims pool rewards',
            'method': '0xe6f1daf2'
        }
    },
    'MEMBERSHIP': {
        'verifyKYC': {
            'direction': 'OUTGOING',
            'description': 'Verifies KYC status',
            'method': '0x9d2f32dd'
        },
        'mintMembership': {
            'direction': 'OUTGOING',
            'description': 'Mints membership NFT',
            'method': '0x40c10f19'
        },
        'updateStatus': {
            'direction': 'OUTGOING',
            'description': 'Updates member status',
            'method': '0x7535d246'
        },
        'revokeAccess': {
            'direction': 'OUTGOING',
            'description': 'Revokes member access',
            'method': '0x2e1a7d4d'
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
        }
    }
}

# Combined functions for all versions
GOLDFINCH_FUNCTIONS = {
    'V1': GOLDFINCH_V1_FUNCTIONS
}