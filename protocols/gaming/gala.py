"""Gala Games Protocol Functions for all versions"""

GALA_V1_FUNCTIONS = {
    'NODES': {
        'operateNode': {
            'direction': 'OUTGOING',
            'description': 'Operates Gala node',
            'method': '0x7535d246'
        },
        'claimNodeRewards': {
            'direction': 'INCOMING',
            'description': 'Claims node rewards',
            'method': '0x4e71d92d'
        },
        'upgradeNode': {
            'direction': 'OUTGOING',
            'description': 'Upgrades node tier',
            'method': '0x7535d246'
        },
        'migrateNode': {
            'direction': 'BOTH',
            'description': 'Migrates node setup',
            'method': '0x4ce38b5f'
        }
    },
    'GAMING': {
        'purchaseItem': {
            'direction': 'OUTGOING',
            'description': 'Purchases game item',
            'method': '0x94b576de'
        },
        'sellItem': {
            'direction': 'INCOMING',
            'description': 'Sells game item',
            'method': '0x454a2ab3'
        },
        'useItem': {
            'direction': 'OUTGOING',
            'description': 'Uses game item',
            'method': '0x7535d246'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims gaming rewards',
            'method': '0x4e71d92d'
        }
    },
    'STAKING': {
        'stakeGALA': {
            'direction': 'OUTGOING',
            'description': 'Stakes GALA tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGALA': {
            'direction': 'INCOMING',
            'description': 'Unstakes GALA tokens',
            'method': '0x2e1a7d4d'
        },
        'claimStakingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
GALA_FUNCTIONS = {
    'V1': GALA_V1_FUNCTIONS
}