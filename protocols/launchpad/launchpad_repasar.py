"""ICO/IDO Platform Functions for all versions"""

LAUNCHPAD_V1_FUNCTIONS = {
    'COINLIST': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in token sale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims purchased tokens',
            'method': '0x4e71d92d'
        },
        'register': {
            'direction': 'OUTGOING',
            'description': 'Registers for sale whitelist',
            'method': '0x1698ee82'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from sale',
            'method': '0x69328dec'
        }
    },
    'POLKASTARTER': {
        'whitelist': {
            'direction': 'OUTGOING',
            'description': 'Joins sale whitelist',
            'method': '0x9b3d47b4'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in IDO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims IDO tokens',
            'method': '0x4e71d92d'
        },
        'emergencyWithdraw': {
            'direction': 'INCOMING',
            'description': 'Emergency withdrawal',
            'method': '0x5312ea8e'
        }
    },
    'DAO_MAKER': {
        'registerSHO': {
            'direction': 'OUTGOING',
            'description': 'Registers for Strong Holder Offering',
            'method': '0x1698ee82'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in SHO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims SHO tokens',
            'method': '0x4e71d92d'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes DAO tokens',
            'method': '0xa694fc3a'
        }
    },
    'COPPER_LAUNCH': {
        'createAuction': {
            'direction': 'OUTGOING',
            'description': 'Creates token auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims won tokens',
            'method': '0x4e71d92d'
        },
        'withdrawUnsuccessful': {
            'direction': 'INCOMING',
            'description': 'Withdraws unsuccessful bid',
            'method': '0x69328dec'
        }
    },
    'PINKSALE': {
        'createPresale': {
            'direction': 'OUTGOING',
            'description': 'Creates presale pool',
            'method': '0x1698ee82'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in presale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims presale tokens',
            'method': '0x4e71d92d'
        },
        'finalize': {
            'direction': 'OUTGOING',
            'description': 'Finalizes successful presale',
            'method': '0x4ce38b5f'
        },
        'cancelPool': {
            'direction': 'BOTH',
            'description': 'Cancels presale pool',
            'method': '0x2e1a7d4d'
        }
    },
    'SEEDIFY': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes SFUND tokens',
            'method': '0xa694fc3a'
        },
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in IGO',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims IGO tokens',
            'method': '0x4e71d92d'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes SFUND tokens',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
LAUNCHPAD_FUNCTIONS = {
    'V1': LAUNCHPAD_V1_FUNCTIONS
}