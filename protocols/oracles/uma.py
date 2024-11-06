"""UMA Protocol Functions for all versions"""

UMA_V1_FUNCTIONS = {
    'ORACLE': {
        'requestPrice': {
            'direction': 'OUTGOING',
            'description': 'Requests price data',
            'method': '0x9b3d47b4'
        },
        'proposePrice': {
            'direction': 'OUTGOING',
            'description': 'Proposes price value',
            'method': '0x7535d246'
        },
        'disputePrice': {
            'direction': 'OUTGOING',
            'description': 'Disputes proposed price',
            'method': '0x2f4f5cc5'
        },
        'settleRequest': {
            'direction': 'INCOMING',
            'description': 'Settles price request',
            'method': '0x4ce38b5f'
        }
    },
    'VOTING': {
        'commitVote': {
            'direction': 'OUTGOING',
            'description': 'Commits vote hash',
            'method': '0x15373e3d'
        },
        'revealVote': {
            'direction': 'OUTGOING',
            'description': 'Reveals committed vote',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims voting rewards',
            'method': '0xe6f1daf2'
        }
    },
    'KPI_OPTIONS': {
        'createOption': {
            'direction': 'OUTGOING',
            'description': 'Creates KPI option',
            'method': '0x1698ee82'
        },
        'exercise': {
            'direction': 'BOTH',
            'description': 'Exercises KPI option',
            'method': '0x4ce38b5f'
        },
        'settle': {
            'direction': 'INCOMING',
            'description': 'Settles KPI option',
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
UMA_FUNCTIONS = {
    'V1': UMA_V1_FUNCTIONS
}