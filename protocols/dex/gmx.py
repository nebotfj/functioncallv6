"""GMX Protocol Functions for all versions"""

GMX_V1_FUNCTIONS = {
    'TRADING': {
        'increasePosition': {
            'direction': 'OUTGOING',
            'description': 'Increases leverage position',
            'method': '0x969b0e0c'
        },
        'decreasePosition': {
            'direction': 'INCOMING',
            'description': 'Decreases leverage position',
            'method': '0x82a08fcd'
        },
        'liquidatePosition': {
            'direction': 'BOTH',
            'description': 'Liquidates underwater position',
            'method': '0x96cd4ddb'
        },
        'swap': {
            'direction': 'BOTH',
            'description': 'Executes token swap',
            'method': '0x128acb08'
        }
    },
    'LIQUIDITY': {
        'addLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Adds liquidity to GLP',
            'method': '0x68bf9329'
        },
        'removeLiquidity': {
            'direction': 'INCOMING',
            'description': 'Removes liquidity from GLP',
            'method': '0x39603469'
        },
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes tokens in protocol',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes tokens from protocol',
            'method': '0x2e1a7d4d'
        }
    },
    'REWARDS': {
        'claimFees': {
            'direction': 'INCOMING',
            'description': 'Claims trading fees',
            'method': '0xd294f093'
        },
        'claimEsGmx': {
            'direction': 'INCOMING',
            'description': 'Claims esGMX rewards',
            'method': '0x84e9fe26'
        },
        'stakeEsGmx': {
            'direction': 'OUTGOING',
            'description': 'Stakes esGMX tokens',
            'method': '0x12c071b1'
        },
        'vestEsGmx': {
            'direction': 'OUTGOING',
            'description': 'Vests esGMX tokens to GMX',
            'method': '0x1749e1e3'
        }
    },
    'REFERRALS': {
        'setReferralCode': {
            'direction': 'OUTGOING',
            'description': 'Sets referral code',
            'method': '0x4b9f2d36'
        },
        'claimReferralRewards': {
            'direction': 'INCOMING',
            'description': 'Claims referral rewards',
            'method': '0x5e91d8ec'
        },
        'compound': {
            'direction': 'OUTGOING',
            'description': 'Compounds rewards',
            'method': '0xf69e2046'
        }
    }
}

# Combined functions for all versions
GMX_FUNCTIONS = {
    'V1': GMX_V1_FUNCTIONS
}