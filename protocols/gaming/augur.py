"""Augur Protocol Functions for all versions"""

AUGUR_V1_FUNCTIONS = {
    'LEGACY': {
        'migrateFromLegacyReputationToken': {
            'direction': 'OUTGOING',
            'description': 'Migrates REP tokens from legacy to new version',
            'method': '0x7f9f19a5'
        },
        'migrateBalances': {
            'direction': 'OUTGOING',
            'description': 'Migrates balances from V1 to V2',
            'method': '0x4c2f04a4'
        },
        'claimTradingProceeds': {
            'direction': 'INCOMING',
            'description': 'Claims proceeds from completed markets',
            'method': '0x8f2c97d9'
        }
    },
}

AUGUR_V2_FUNCTIONS = {
    'MARKET': {
        'createMarket': {
            'direction': 'OUTGOING',
            'description': 'Creates a new prediction market',
            'method': '0x79474b24'
        },
        'doInitialReport': {
            'direction': 'OUTGOING',
            'description': 'Submits initial report for market resolution',
            'method': '0x8ea2cc84'
        },
        'contributeToTentative': {
            'direction': 'OUTGOING',
            'description': 'Contributes REP to a tentative outcome',
            'method': '0x4c2f83c2'
        },
        'disavowMarket': {
            'direction': 'OUTGOING',
            'description': 'Allows market creator to disavow a market in fork period',
            'method': '0x6a1a80fd'
        },
        'claimMarketsProceeds': {
            'direction': 'INCOMING',
            'description': 'Claims trading proceeds from multiple markets',
            'method': '0x89f9aab7'
        },
        'claimParticipationTokens': {
            'direction': 'INCOMING',
            'description': 'Claims REP from participation token redemption',
            'method': '0xe7f892a4'
        },
        'buyParticipationTokens': {
            'direction': 'OUTGOING',
            'description': 'Purchases participation tokens for fee window',
            'method': '0x3aa6b597'
        }
    },
}

AUGUR_V3_FUNCTIONS = {
    'MARKET': {
        'createScalarMarket': {
            'direction': 'OUTGOING',
            'description': 'Creates a new scalar prediction market',
            'method': '0x4336a37d'
        },
        'createYesNoMarket': {
            'direction': 'OUTGOING',
            'description': 'Creates a new yes/no prediction market',
            'method': '0x2c644f32'
        },
        'createCategoricalMarket': {
            'direction': 'OUTGOING',
            'description': 'Creates a new categorical prediction market',
            'method': '0x1c3b35f2'
        },
        'disputeWindow': {
            'direction': 'OUTGOING',
            'description': 'Participates in market dispute window',
            'method': '0x7bb9a884'
        },
        'finalizeMarket': {
            'direction': 'OUTGOING',
            'description': 'Finalizes a market after dispute window',
            'method': '0x2f29576c'
        },
        'claimWinningsTradingProceeds': {
            'direction': 'INCOMING',
            'description': 'Claims winnings from trading in resolved markets',
            'method': '0x8f2c97d9'
        },
        'claimDisputeWindowProceeds': {
            'direction': 'INCOMING',
            'description': 'Claims proceeds from dispute window participation',
            'method': '0x6ab150b4'
        },
        'migrateREPv2ToREPv3': {
            'direction': 'OUTGOING',
            'description': 'Migrates REPv2 tokens to REPv3',
            'method': '0x9a8b2d42'
        },
        'mintCompleteSets': {
            'direction': 'OUTGOING',
            'description': 'Mints complete sets of outcome shares',
            'method': '0x42d16cea'
        },
        'redeemStake': {
            'direction': 'INCOMING',
            'description': 'Redeems staked REP after market resolution',
            'method': '0x8d2b24d8'
        },
        'reportingParticipantDisavow': {
            'direction': 'OUTGOING',
            'description': 'Allows reporting participant to disavow during fork',
            'method': '0x969b8353'
        }
    }
}

# Combined functions for all versions
AUGUR_FUNCTIONS = {
    'V2': AUGUR_V1_FUNCTIONS,
    'V3': AUGUR_V2_FUNCTIONS,
    'V4': AUGUR_V3_FUNCTIONS
}