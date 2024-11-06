"""GameStarter Protocol Functions for all versions"""

GAMESTARTER_V1_FUNCTIONS = {
    'IGO': {
        'participate': {
            'direction': 'OUTGOING',
            'description': 'Participates in game token sale',
            'method': '0x8f38249c'
        },
        'claim': {
            'direction': 'INCOMING',
            'description': 'Claims purchased game tokens',
            'method': '0x4e71d92d'
        },
        'refund': {
            'direction': 'INCOMING',
            'description': 'Claims refund for failed IGO',
            'method': '0x590e1ae3'
        }
    },
    'STAKING': {
        'stakeGAME': {
            'direction': 'OUTGOING',
            'description': 'Stakes GAME tokens',
            'method': '0xa694fc3a'
        },
        'unstakeGAME': {
            'direction': 'INCOMING',
            'description': 'Unstakes GAME tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'TIERS': {
        'lockTokens': {
            'direction': 'OUTGOING',
            'description': 'Locks tokens for tier access',
            'method': '0x3d18b912'
        },
        'unlockTokens': {
            'direction': 'INCOMING',
            'description': 'Unlocks tier tokens',
            'method': '0x2e1a7d4d'
        },
        'upgradeTier': {
            'direction': 'OUTGOING',
            'description': 'Upgrades access tier',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
GAMESTARTER_FUNCTIONS = {
    'V1': GAMESTARTER_V1_FUNCTIONS
}