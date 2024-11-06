"""Across Protocol Bridge Functions for all versions"""

ACROSS_V1_FUNCTIONS = {
    'BRIDGE': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens for bridging',
            'method': '0xb6b55f25'
        },
        'fillRelay': {
            'direction': 'BOTH',
            'description': 'Fills bridge relay request',
            'method': '0x9b3d47b4'
        },
        'speedUpRelay': {
            'direction': 'OUTGOING',
            'description': 'Accelerates relay process',
            'method': '0x7c025200'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims bridged tokens',
            'method': '0x4e71d92d'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge pool',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge pool',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees',
            'method': '0xd294f093'
        }
    },
    'STAKING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

ACROSS_V2_FUNCTIONS = {
    'BRIDGE': {
        'deposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits tokens for bridging V2',
            'method': '0xb6b55f25'
        },
        'fillRelay': {
            'direction': 'BOTH',
            'description': 'Fills bridge relay request V2',
            'method': '0x9b3d47b4'
        },
        'speedUpRelay': {
            'direction': 'OUTGOING',
            'description': 'Accelerates relay process V2',
            'method': '0x7c025200'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims bridged tokens V2',
            'method': '0x4e71d92d'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to bridge pool V2',
            'method': '0xe8e33700'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from bridge pool V2',
            'method': '0xbaa2abde'
        },
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims accumulated fees V2',
            'method': '0xd294f093'
        },
        'rebalancePool': {
            'direction': 'BOTH',
            'description': 'Rebalances bridge pool',
            'method': '0x4ce38b5f'
        }
    },
    'REWARDS': {
        'stakeACX': {
            'direction': 'OUTGOING',
            'description': 'Stakes ACX tokens',
            'method': '0xa694fc3a'
        },
        'unstakeACX': {
            'direction': 'INCOMING',
            'description': 'Unstakes ACX tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims ACX rewards',
            'method': '0xe6f1daf2'
        },
        'compoundRewards': {
            'direction': 'OUTGOING',
            'description': 'Compounds ACX rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
ACROSS_FUNCTIONS = {
    'V1': ACROSS_V1_FUNCTIONS,
    'V2': ACROSS_V2_FUNCTIONS
}