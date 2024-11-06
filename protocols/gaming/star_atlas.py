"""Star Atlas Protocol Functions for all versions"""

STAR_ATLAS_V1_FUNCTIONS = {
    'GAMEPLAY': {
        'startMission': {
            'direction': 'OUTGOING',
            'description': 'Starts fleet mission',
            'method': '0x1698ee82'
        },
        'completeMission': {
            'direction': 'INCOMING',
            'description': 'Completes active mission',
            'method': '0x4ce38b5f'
        },
        'repairShip': {
            'direction': 'OUTGOING',
            'description': 'Repairs damaged ship',
            'method': '0x7535d246'
        },
        'upgradeShip': {
            'direction': 'OUTGOING',
            'description': 'Upgrades ship components',
            'method': '0x7535d246'
        },
        'minePlanets': {
            'direction': 'BOTH',
            'description': 'Mines planetary resources',
            'method': '0x7c025200'
        }
    },
    'MARKETPLACE': {
        'listAsset': {
            'direction': 'OUTGOING',
            'description': 'Lists asset for sale',
            'method': '0x6c1aaf13'
        },
        'buyAsset': {
            'direction': 'OUTGOING',
            'description': 'Purchases listed asset',
            'method': '0x94b576de'
        },
        'createAuction': {
            'direction': 'OUTGOING',
            'description': 'Creates asset auction',
            'method': '0x3b11b670'
        },
        'placeBid': {
            'direction': 'OUTGOING',
            'description': 'Places auction bid',
            'method': '0x9d2f32dd'
        },
        'claimAuction': {
            'direction': 'INCOMING',
            'description': 'Claims won auction',
            'method': '0x4e71d92d'
        }
    },
    'STAKING': {
        'stakeATLAS': {
            'direction': 'OUTGOING',
            'description': 'Stakes ATLAS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeATLAS': {
            'direction': 'INCOMING',
            'description': 'Unstakes ATLAS tokens',
            'method': '0x2e1a7d4d'
        },
        'stakePOLIS': {
            'direction': 'OUTGOING',
            'description': 'Stakes POLIS tokens',
            'method': '0xa694fc3a'
        },
        'unstakePOLIS': {
            'direction': 'INCOMING',
            'description': 'Unstakes POLIS tokens',
            'method': '0x2e1a7d4d'
        },
        'stakeLPTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes LP tokens',
            'method': '0xa694fc3a'
        },
        'unstakeLPTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes LP tokens',
            'method': '0x2e1a7d4d'
        }
    }
}

# Combined functions for all versions
STAR_ATLAS_FUNCTIONS = {
    'V1': STAR_ATLAS_V1_FUNCTIONS
}