"""Unslashed Protocol Functions for all versions"""

UNSLASHED_V1_FUNCTIONS = {
    'COVERAGE': {
        'purchasePolicy': {
            'direction': 'OUTGOING',
            'description': 'Purchases insurance policy',
            'method': '0x8f38249c'
        },
        'fileClaim': {
            'direction': 'OUTGOING',
            'description': 'Files insurance claim',
            'method': '0x9b3d47b4'
        },
        'withdrawClaim': {
            'direction': 'INCOMING',
            'description': 'Withdraws claim payout',
            'method': '0x69328dec'
        },
        'cancelPolicy': {
            'direction': 'OUTGOING',
            'description': 'Cancels active policy',
            'method': '0x2e1a7d4d'
        },
        'renewPolicy': {
            'direction': 'OUTGOING',
            'description': 'Renews existing policy',
            'method': '0x7535d246'
        }
    },
    'CAPITAL': {
        'depositCapital': {
            'direction': 'OUTGOING',
            'description': 'Deposits capital to pool',
            'method': '0x47e7ef24'
        },
        'withdrawCapital': {
            'direction': 'INCOMING',
            'description': 'Withdraws capital from pool',
            'method': '0x69328dec'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims capital rewards',
            'method': '0x4e71d92d'
        },
        'reinvestRewards': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
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
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    },
    'RISK_ASSESSMENT': {
        'submitRiskAssessment': {
            'direction': 'OUTGOING',
            'description': 'Submits risk assessment',
            'method': '0x9b3d47b4'
        },
        'updateRiskParameters': {
            'direction': 'OUTGOING',
            'description': 'Updates risk parameters',
            'method': '0x7535d246'
        },
        'claimAssessmentRewards': {
            'direction': 'INCOMING',
            'description': 'Claims assessment rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
UNSLASHED_FUNCTIONS = {
    'V1': UNSLASHED_V1_FUNCTIONS
}