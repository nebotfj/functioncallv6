"""Tellor Protocol Functions for all versions"""

TELLOR_V1_FUNCTIONS = {
    'ORACLE': {
        'submitValue': {
            'direction': 'OUTGOING',
            'description': 'Submits oracle value',
            'method': '0x7535d246'
        },
        'disputeValue': {
            'direction': 'OUTGOING',
            'description': 'Disputes submitted value',
            'method': '0x2f4f5cc5'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on dispute',
            'method': '0x15373e3d'
        },
        'retrieveData': {
            'direction': 'NEUTRAL',
            'description': 'Gets oracle data',
            'method': '0x9d2f32dd'
        }
    },
    'STAKING': {
        'depositStake': {
            'direction': 'OUTGOING',
            'description': 'Stakes TRB tokens',
            'method': '0xa694fc3a'
        },
        'requestStakingWithdraw': {
            'direction': 'OUTGOING',
            'description': 'Requests stake withdrawal',
            'method': '0x0c49ccbe'
        },
        'withdrawStake': {
            'direction': 'INCOMING',
            'description': 'Withdraws staked tokens',
            'method': '0x2e1a7d4d'
        }
    },
    'REWARDS': {
        'claimTip': {
            'direction': 'INCOMING',
            'description': 'Claims reporter tip',
            'method': '0x4e71d92d'
        },
        'claimReward': {
            'direction': 'INCOMING',
            'description': 'Claims oracle rewards',
            'method': '0xe6f1daf2'
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
TELLOR_FUNCTIONS = {
    'V1': TELLOR_V1_FUNCTIONS
}