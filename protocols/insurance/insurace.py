"""InsurAce Protocol Functions for all versions"""

INSURACE_V1_FUNCTIONS = {
    'COVERAGE': {
        'buyCover': {
            'direction': 'OUTGOING',
            'description': 'Purchases insurance coverage',
            'method': '0x8f38249c'
        },
        'renewCover': {
            'direction': 'OUTGOING',
            'description': 'Renews existing coverage',
            'method': '0x7535d246'
        },
        'submitClaim': {
            'direction': 'OUTGOING',
            'description': 'Submits insurance claim',
            'method': '0x9b3d47b4'
        },
        'redeemClaim': {
            'direction': 'INCOMING',
            'description': 'Redeems approved claim',
            'method': '0x4e71d92d'
        },
        'cancelCover': {
            'direction': 'OUTGOING',
            'description': 'Cancels active coverage',
            'method': '0x2e1a7d4d'
        }
    },
    'STAKING': {
        'stakeINSUR': {
            'direction': 'OUTGOING',
            'description': 'Stakes INSUR tokens',
            'method': '0xa694fc3a'
        },
        'unstakeINSUR': {
            'direction': 'INCOMING',
            'description': 'Unstakes INSUR tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'reinvestRewards': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
        }
    },
    'INVESTMENT': {
        'invest': {
            'direction': 'OUTGOING',
            'description': 'Invests in coverage pool',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws investment',
            'method': '0x69328dec'
        },
        'reinvest': {
            'direction': 'OUTGOING',
            'description': 'Reinvests pool earnings',
            'method': '0xf69e2046'
        },
        'claimInvestmentRewards': {
            'direction': 'INCOMING',
            'description': 'Claims investment rewards',
            'method': '0x4e71d92d'
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
INSURACE_FUNCTIONS = {
    'V1': INSURACE_V1_FUNCTIONS
}