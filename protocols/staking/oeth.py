"""Origin ETH Protocol Functions for all versions"""

OETH_V1_FUNCTIONS = {
    'STAKING': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints OETH tokens',
            'method': '0x40c10f19'
        },
        'redeem': {
            'direction': 'INCOMING',
            'description': 'Redeems OETH for ETH',
            'method': '0xdb006a75'
        },
        'rebase': {
            'direction': 'NEUTRAL',
            'description': 'Performs rebase operation',
            'method': '0x4c1f00cc'
        },
        'claimYield': {
            'direction': 'INCOMING',
            'description': 'Claims yield rewards',
            'method': '0xe6f1daf2'
        }
    },
    'VAULT': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits assets to vault',
            'method': '0x47e7ef24'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws assets from vault',
            'method': '0x69328dec'
        },
        'harvestYield': {
            'direction': 'INCOMING',
            'description': 'Harvests vault yield',
            'method': '0x4641257d'
        },
        'rebalance': {
            'direction': 'OUTGOING',
            'description': 'Rebalances vault assets',
            'method': '0x4ce38b5f'
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
OETH_FUNCTIONS = {
    'V1': OETH_V1_FUNCTIONS
}