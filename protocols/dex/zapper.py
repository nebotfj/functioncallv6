"""Zapper Protocol Functions for all versions"""

ZAPPER_V1_FUNCTIONS = {
    'ZAPS': {
        'zapIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps token into protocol',
            'method': '0x6d914547'
        },
        'zapOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of protocol',
            'method': '0x0c2d3f2b'
        },
        'multiZapIn': {
            'direction': 'OUTGOING',
            'description': 'Zaps into multiple protocols',
            'method': '0x945bcec9'
        },
        'multiZapOut': {
            'direction': 'INCOMING',
            'description': 'Zaps out of multiple protocols',
            'method': '0x4ce38b5f'
        },
        'zapAcross': {
            'direction': 'BOTH',
            'description': 'Zaps between protocols',
            'method': '0x7c025200'
        },
         'ZapOut2PairToken': {
            'direction': 'INCOMING',
            'description': 'Remove liquidity and convert to token pair',
            'method': '0x41f13681',
            'protocol': ['Zapper.fi']
        }
    },
    'FARMING': {
        'farmDeposit': {
            'direction': 'OUTGOING',
            'description': 'Deposits into farm',
            'method': '0xe2bbb158'
        },
        'farmWithdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws from farm',
            'method': '0x441a3e70'
        },
        'harvestRewards': {
            'direction': 'INCOMING',
            'description': 'Claims farming rewards',
            'method': '0x4641257d'
        },
        'compoundFarm': {
            'direction': 'OUTGOING',
            'description': 'Compounds farm rewards',
            'method': '0xf69e2046'
        }
    },
    'STAKING': {
        'stakeTokens': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens',
            'method': '0xa694fc3a'
        },
        'unstakeTokens': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
ZAPPER_FUNCTIONS = {
    'V1': ZAPPER_V1_FUNCTIONS
}