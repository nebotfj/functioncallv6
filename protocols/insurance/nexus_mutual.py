"""Nexus Mutual Protocol Functions for all versions"""

NEXUS_MUTUAL_V1_FUNCTIONS = {
    'COVERAGE': {
        'buyCover': {
            'direction': 'OUTGOING',
            'description': 'Purchases cover policy',
            'method': '0x8f38249c'
        },
        'submitClaim': {
            'direction': 'OUTGOING',
            'description': 'Submits cover claim',
            'method': '0x9b3d47b4'
        },
        'redeemClaim': {
            'direction': 'INCOMING',
            'description': 'Redeems approved claim',
            'method': '0x4e71d92d'
        },
        'withdrawExpiredCover': {
            'direction': 'INCOMING',
            'description': 'Withdraws expired cover',
            'method': '0x69328dec'
        },
        'extendCover': {
            'direction': 'OUTGOING',
            'description': 'Extends cover duration',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stakeNXM': {
            'direction': 'OUTGOING',
            'description': 'Stakes NXM tokens',
            'method': '0xa694fc3a'
        },
        'unstakeNXM': {
            'direction': 'INCOMING',
            'description': 'Unstakes NXM tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'switchMembership': {
            'direction': 'OUTGOING',
            'description': 'Changes membership type',
            'method': '0x7535d246'
        }
    },
    'GOVERNANCE': {
        'submitProposal': {
            'direction': 'OUTGOING',
            'description': 'Submits new proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims governance rewards',
            'method': '0x4e71d92d'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        }
    },
    'ASSESSMENT': {
        'submitAssessment': {
            'direction': 'OUTGOING',
            'description': 'Submits claim assessment',
            'method': '0x9b3d47b4'
        },
        'challengeAssessment': {
            'direction': 'OUTGOING',
            'description': 'Challenges assessment',
            'method': '0x2f4f5cc5'
        },
        'claimAssessmentReward': {
            'direction': 'INCOMING',
            'description': 'Claims assessment reward',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
NEXUS_MUTUAL_FUNCTIONS = {
    'V1': NEXUS_MUTUAL_V1_FUNCTIONS
}