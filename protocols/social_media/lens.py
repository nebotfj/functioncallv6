"""Lens Protocol Functions for all versions"""

LENS_V1_FUNCTIONS = {
    'PROFILE': {
        'createProfile': {
            'direction': 'OUTGOING',
            'description': 'Creates Lens profile',
            'method': '0x1698ee82'
        },
        'setProfileImageURI': {
            'direction': 'OUTGOING',
            'description': 'Sets profile picture',
            'method': '0x7535d246'
        },
        'follow': {
            'direction': 'OUTGOING',
            'description': 'Follows profile',
            'method': '0x5c19a95c'
        },
        'unfollow': {
            'direction': 'OUTGOING',
            'description': 'Unfollows profile',
            'method': '0x2e1a7d4d'
        },
        'setDefaultProfile': {
            'direction': 'OUTGOING',
            'description': 'Sets default profile',
            'method': '0x4aea29bd'
        }
    },
    'PUBLICATION': {
        'post': {
            'direction': 'OUTGOING',
            'description': 'Creates new post',
            'method': '0x7c025200'
        },
        'comment': {
            'direction': 'OUTGOING',
            'description': 'Comments on publication',
            'method': '0x9b3d47b4'
        },
        'mirror': {
            'direction': 'OUTGOING',
            'description': 'Mirrors publication',
            'method': '0x2f4f5cc5'
        },
        'collect': {
            'direction': 'OUTGOING',
            'description': 'Collects publication',
            'method': '0x4ce38b5f'
        }
    },
    'MONETIZATION': {
        'enableModuleForProfile': {
            'direction': 'OUTGOING',
            'description': 'Enables profile module',
            'method': '0x3a088cd2'
        },
        'disableModuleForProfile': {
            'direction': 'OUTGOING',
            'description': 'Disables profile module',
            'method': '0x5f7b8feb'
        },
        'claimRevenue': {
            'direction': 'INCOMING',
            'description': 'Claims earned revenue',
            'method': '0x4e71d92d'
        }
    },
    'GOVERNANCE': {
        'createProposal': {
            'direction': 'OUTGOING',
            'description': 'Creates governance proposal',
            'method': '0xda95691a'
        },
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'execute': {
            'direction': 'OUTGOING',
            'description': 'Executes passed proposal',
            'method': '0xfe0d94c1'
        }
    }
}

LENS_V2_FUNCTIONS = {
    'PROFILE': {
        'createProfileWithHandle': {
            'direction': 'OUTGOING',
            'description': 'Creates profile with handle',
            'method': '0x1698ee82'
        },
        'setProfileMetadata': {
            'direction': 'OUTGOING',
            'description': 'Sets profile metadata',
            'method': '0x7535d246'
        },
        'follow': {
            'direction': 'OUTGOING',
            'description': 'Follows profile with params',
            'method': '0x5c19a95c'
        },
        'unfollow': {
            'direction': 'OUTGOING',
            'description': 'Unfollows profile',
            'method': '0x2e1a7d4d'
        },
        'blockProfile': {
            'direction': 'OUTGOING',
            'description': 'Blocks profile',
            'method': '0x4b9f2d36'
        }
    },
    'PUBLICATION': {
        'post': {
            'direction': 'OUTGOING',
            'description': 'Creates post with actions',
            'method': '0x7c025200'
        },
        'comment': {
            'direction': 'OUTGOING',
            'description': 'Comments with reference',
            'method': '0x9b3d47b4'
        },
        'mirror': {
            'direction': 'OUTGOING',
            'description': 'Mirrors with reference',
            'method': '0x2f4f5cc5'
        },
        'quote': {
            'direction': 'OUTGOING',
            'description': 'Creates quote post',
            'method': '0x4ce38b5f'
        }
    },
    'ACTIONS': {
        'act': {
            'direction': 'OUTGOING',
            'description': 'Performs publication action',
            'method': '0x3a088cd2'
        },
        'cancelAction': {
            'direction': 'OUTGOING',
            'description': 'Cancels publication action',
            'method': '0x5f7b8feb'
        },
        'setActionModule': {
            'direction': 'OUTGOING',
            'description': 'Sets action module',
            'method': '0x7535d246'
        }
    },
    'MONETIZATION': {
        'enableFollowModule': {
            'direction': 'OUTGOING',
            'description': 'Enables follow module',
            'method': '0x3a088cd2'
        },
        'enableReferenceModule': {
            'direction': 'OUTGOING',
            'description': 'Enables reference module',
            'method': '0x5f7b8feb'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims module rewards',
            'method': '0x4e71d92d'
        }
    }
}

# Combined functions for all versions
LENS_FUNCTIONS = {
    'V1': LENS_V1_FUNCTIONS,
    'V2': LENS_V2_FUNCTIONS
}