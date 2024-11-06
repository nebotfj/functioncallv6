"""Eden Network Protocol Functions for all versions"""

EDEN_V1_FUNCTIONS = {
    'SLOTS': {
        'reserveSlot': {
            'direction': 'OUTGOING',
            'description': 'Reserves block builder slot',
            'method': '0x1698ee82'
        },
        'cancelReservation': {
            'direction': 'OUTGOING',
            'description': 'Cancels slot reservation',
            'method': '0x2e1a7d4d'
        },
        'claimSlotRewards': {
            'direction': 'INCOMING',
            'description': 'Claims slot usage rewards',
            'method': '0x4e71d92d'
        }
    },
    'STAKING': {
        'stakeEDEN': {
            'direction': 'OUTGOING',
            'description': 'Stakes EDEN tokens',
            'method': '0xa694fc3a'
        },
        'unstakeEDEN': {
            'direction': 'INCOMING',
            'description': 'Unstakes EDEN tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'BUNDLES': {
        'submitBundle': {
            'direction': 'OUTGOING',
            'description': 'Submits transaction bundle',
            'method': '0x7535d246'
        },
        'cancelBundle': {
            'direction': 'OUTGOING',
            'description': 'Cancels submitted bundle',
            'method': '0x2e1a7d4d'
        }
    },
    'BUILDER': {
        'registerBuilder': {
            'direction': 'OUTGOING',
            'description': 'Registers as block builder',
            'method': '0x1698ee82'
        },
        'updateBuilderConfig': {
            'direction': 'OUTGOING',
            'description': 'Updates builder settings',
            'method': '0x7535d246'
        },
        'claimBuilderRewards': {
            'direction': 'INCOMING',
            'description': 'Claims builder rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
EDEN_FUNCTIONS = {
    'V1': EDEN_V1_FUNCTIONS
}