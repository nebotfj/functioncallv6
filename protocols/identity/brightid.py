"""BrightID Protocol Functions for all versions"""

BRIGHTID_V1_FUNCTIONS = {
    'VERIFICATION': {
        'verify': {
            'direction': 'OUTGOING',
            'description': 'Verifies user identity',
            'method': '0x4b8a3529'
        },
        'sponsor': {
            'direction': 'OUTGOING',
            'description': 'Sponsors user verification',
            'method': '0x8b9e4f93'
        },
        'link': {
            'direction': 'OUTGOING',
            'description': 'Links user accounts',
            'method': '0x7535d246'
        },
        'removeConnection': {
            'direction': 'OUTGOING',
            'description': 'Removes user connection',
            'method': '0x2e1a7d4d'
        }
    },
    'GROUPS': {
        'createGroup': {
            'direction': 'OUTGOING',
            'description': 'Creates new group',
            'method': '0x1698ee82'
        },
        'joinGroup': {
            'direction': 'OUTGOING',
            'description': 'Joins existing group',
            'method': '0x9b3d47b4'
        },
        'leaveGroup': {
            'direction': 'OUTGOING',
            'description': 'Leaves current group',
            'method': '0x7c025200'
        },
        'inviteMember': {
            'direction': 'OUTGOING',
            'description': 'Invites new member',
            'method': '0x2f4f5cc5'
        }
    },
    'CONTEXT': {
        'addContext': {
            'direction': 'OUTGOING',
            'description': 'Adds verification context',
            'method': '0x4ce38b5f'
        },
        'removeContext': {
            'direction': 'OUTGOING',
            'description': 'Removes verification context',
            'method': '0x5f7b8feb'
        },
        'updateContext': {
            'direction': 'OUTGOING',
            'description': 'Updates context parameters',
            'method': '0xe74b981b'
        }
    }
}

# Combined functions for all versions
BRIGHTID_FUNCTIONS = {
    'V1': BRIGHTID_V1_FUNCTIONS
}