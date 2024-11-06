"""Centrifuge Protocol Functions for all versions"""

CENTRIFUGE_V1_FUNCTIONS = {
    'ASSETS': {
        'createAsset': {
            'direction': 'OUTGOING',
            'description': 'Creates new real world asset',
            'method': '0x1698ee82'
        },
        'updateAsset': {
            'direction': 'OUTGOING',
            'description': 'Updates asset parameters',
            'method': '0x7535d246'
        },
        'mintNFT': {
            'direction': 'OUTGOING',
            'description': 'Mints asset NFT',
            'method': '0x40c10f19'
        },
        'transferAsset': {
            'direction': 'BOTH',
            'description': 'Transfers asset ownership',
            'method': '0x23b872dd'
        },
        'verifyDocument': {
            'direction': 'OUTGOING',
            'description': 'Verifies asset documentation',
            'method': '0x9d2f32dd'
        }
    },
    'FINANCING': {
        'createPool': {
            'direction': 'OUTGOING',
            'description': 'Creates financing pool',
            'method': '0x1698ee82'
        },
        'invest': {
            'direction': 'OUTGOING',
            'description': 'Invests in financing pool',
            'method': '0x47e7ef24'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems pool investment',
            'method': '0xdb006a75'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims pool rewards',
            'method': '0x4e71d92d'
        },
        'updatePoolParameters': {
            'direction': 'OUTGOING',
            'description': 'Updates pool settings',
            'method': '0x7535d246'
        }
    },
    'STAKING': {
        'stakeCFG': {
            'direction': 'OUTGOING',
            'description': 'Stakes CFG tokens',
            'method': '0xa694fc3a'
        },
        'unstakeCFG': {
            'direction': 'INCOMING',
            'description': 'Unstakes CFG tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'delegateStake': {
            'direction': 'OUTGOING',
            'description': 'Delegates staking power',
            'method': '0x5c19a95c'
        }
    },
    'GOVERNANCE': {
        'propose': {
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

# Combined functions for all versions
CENTRIFUGE_FUNCTIONS = {
    'V1': CENTRIFUGE_V1_FUNCTIONS
}