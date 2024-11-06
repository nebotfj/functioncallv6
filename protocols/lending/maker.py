"""Maker Protocol Functions for all versions"""

MAKER_V1_FUNCTIONS = {
    'VAULT': {
        'openVault': {
            'direction': 'OUTGOING',
            'description': 'Opens new CDP vault',
            'method': '0x3b11b670'
        },
        'depositCollateral': {
            'direction': 'OUTGOING',
            'description': 'Deposits collateral into vault',
            'method': '0x47e7ef24'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws collateral from vault',
            'method': '0x69328dec'
        },
        'generateDai': {
            'direction': 'INCOMING',
            'description': 'Generates DAI from vault',
            'method': '0x40c10f19'
        },
        'payback': {
            'direction': 'OUTGOING',
            'description': 'Repays DAI debt',
            'method': '0x573ade81'
        },
        'lockGem': {
            'direction': 'OUTGOING',
            'description': 'Locks collateral gem',
            'method': '0x3d18b912'
        },
        'freeGem': {
            'direction': 'INCOMING',
            'description': 'Frees locked collateral',
            'method': '0x2e1a7d4d'
        },
        'draw': {
            'direction': 'INCOMING',
            'description': 'Draws DAI from vault',
            'method': '0x9dc29fac'
        },
        'wipe': {
            'direction': 'OUTGOING',
            'description': 'Wipes DAI debt',
            'method': '0xb46310f6'
        },
        'wipeAll': {
            'direction': 'OUTGOING',
            'description': 'Wipes all DAI debt',
            'method': '0x4b84d4c5'
        }
    },
    'LIQUIDATION': {
        'bite': {
            'direction': 'BOTH',
            'description': 'Initiates liquidation',
            'method': '0xa4c0ed36'
        },
        'liquidate': {
            'direction': 'BOTH',
            'description': 'Liquidates unsafe vault',
            'method': '0x96cd4ddb'
        },
        'auctionStart': {
            'direction': 'OUTGOING',
            'description': 'Starts collateral auction',
            'method': '0x9f678cca'
        },
        'tend': {
            'direction': 'OUTGOING',
            'description': 'Places bid in auction',
            'method': '0x4b43ed12'
        },
        'dent': {
            'direction': 'OUTGOING',
            'description': 'Places reverse bid',
            'method': '0x5ff3a382'
        },
        'deal': {
            'direction': 'INCOMING',
            'description': 'Settles auction',
            'method': '0xc959c42b'
        }
    },
    'GOVERNANCE': {
        'vote': {
            'direction': 'OUTGOING',
            'description': 'Votes on proposal',
            'method': '0x15373e3d'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates voting power',
            'method': '0x5c19a95c'
        },
        'lock': {
            'direction': 'OUTGOING',
            'description': 'Locks MKR tokens',
            'method': '0x3d18b912'
        },
        'free': {
            'direction': 'INCOMING',
            'description': 'Unlocks MKR tokens',
            'method': '0x2e1a7d4d'
        },
        'plot': {
            'direction': 'OUTGOING',
            'description': 'Plans executive vote',
            'method': '0x4634691e'
        },
        'lift': {
            'direction': 'OUTGOING',
            'description': 'Activates spell',
            'method': '0x3c278bd5'
        },
        'propose': {
            'direction': 'OUTGOING',
            'description': 'Creates proposal',
            'method': '0xda95691a'
        },
        'exec': {
            'direction': 'OUTGOING',
            'description': 'Executes proposal',
            'method': '0xfe0d94c1'
        }
    }
}

MAKER_MIGRATION_FUNCTIONS = {
    'SCD_SHUTDOWN': {
        'shutdownSCD': {
            'direction': 'OUTGOING',
            'description': 'Shuts down Single Collateral DAI',
            'method': '0x7a9da510'
        },
        'redeemSCD': {
            'direction': 'INCOMING',
            'description': 'Redeems Single Collateral DAI',
            'method': '0xdb006a75'
        },
        'swapSaiToDai': {
            'direction': 'BOTH',
            'description': 'Swaps SAI to DAI',
            'method': '0x3df02124'
        }
    },
    'MCD_MIGRATION': {
        'migrateToMCD': {
            'direction': 'BOTH',
            'description': 'Migrates to Multi Collateral DAI',
            'method': '0x4ce38b5f'
        },
        'migrateCDP': {
            'direction': 'BOTH',
            'description': 'Migrates CDP to MCD vault',
            'method': '0x2f4f5cc5'
        },
        'migrateProxy': {
            'direction': 'BOTH',
            'description': 'Migrates proxy to MCD',
            'method': '0x7535d246'
        }
    },
    'COLLATERAL': {
        'migrateCollateral': {
            'direction': 'BOTH',
            'description': 'Migrates collateral to MCD',
            'method': '0x4ce38b5f'
        },
        'withdrawCollateral': {
            'direction': 'INCOMING',
            'description': 'Withdraws migrated collateral',
            'method': '0x69328dec'
        },
        'paybackDebt': {
            'direction': 'OUTGOING',
            'description': 'Pays back migration debt',
            'method': '0x573ade81'
        }
    }
}

# Combined functions for all versions
MAKER_FUNCTIONS = {
    'V1': MAKER_V1_FUNCTIONS,
    'MIGRATION': MAKER_MIGRATION_FUNCTIONS
}