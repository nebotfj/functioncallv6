"""TrueFi Protocol Functions for all versions"""

TRUEFI_V1_FUNCTIONS = {
    'LENDING': {
        'createLoan': {
            'direction': 'OUTGOING',
            'description': 'Creates new loan',
            'method': '0x1698ee82'
        },
        'approveLoan': {
            'direction': 'OUTGOING',
            'description': 'Approves loan request',
            'method': '0x7535d246'
        },
        'repayLoan': {
            'direction': 'OUTGOING',
            'description': 'Repays active loan',
            'method': '0x573ade81'
        },
        'liquidateLoan': {
            'direction': 'BOTH',
            'description': 'Liquidates defaulted loan',
            'method': '0x96cd4ddb'
        },
        'rateCredit': {
            'direction': 'OUTGOING',
            'description': 'Rates borrower credit',
            'method': '0x9d2f32dd'
        }
    },
    'STAKING': {
        'stakeTRU': {
            'direction': 'OUTGOING',
            'description': 'Stakes TRU tokens',
            'method': '0xa694fc3a'
        },
        'unstakeTRU': {
            'direction': 'INCOMING',
            'description': 'Unstakes TRU tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'delegateVotes': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    },
    'PORTFOLIO': {
        'createPortfolio': {
            'direction': 'OUTGOING',
            'description': 'Creates loan portfolio',
            'method': '0x1698ee82'
        },
        'invest': {
            'direction': 'OUTGOING',
            'description': 'Invests in portfolio',
            'method': '0x47e7ef24'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems portfolio tokens',
            'method': '0xdb006a75'
        },
        'harvest': {
            'direction': 'INCOMING',
            'description': 'Harvests portfolio yield',
            'method': '0x4641257d'
        },
        'rebalance': {
            'direction': 'OUTGOING',
            'description': 'Rebalances portfolio',
            'method': '0x4ce38b5f'
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
        },
        'queue': {
            'direction': 'OUTGOING',
            'description': 'Queues proposal',
            'method': '0xddf0b009'
        }
    }
}

# Combined functions for all versions
TRUEFI_FUNCTIONS = {
    'V1': TRUEFI_V1_FUNCTIONS
}