"""Betswirl Protocol Functions for all versions"""

BETSWIRL_V1_FUNCTIONS = {
    'BETTING': {
        'placeBet': {
            'direction': 'OUTGOING',
            'description': 'Places new bet',
            'method': '0x8f38249c'
        },
        'claimWinnings': {
            'direction': 'INCOMING',
            'description': 'Claims bet winnings',
            'method': '0x4e71d92d'
        },
        'refundBet': {
            'direction': 'INCOMING',
            'description': 'Claims bet refund',
            'method': '0x590e1ae3'
        },
        'multibet': {
            'direction': 'OUTGOING',
            'description': 'Places multiple bets',
            'method': '0x945bcec9'
        }
    },
    'STAKING': {
        'stakeBETS': {
            'direction': 'OUTGOING',
            'description': 'Stakes BETS tokens',
            'method': '0xa694fc3a'
        },
        'unstakeBETS': {
            'direction': 'INCOMING',
            'description': 'Unstakes BETS tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        },
        'reinvestRewards': {
            'direction': 'OUTGOING',
            'description': 'Reinvests earned rewards',
            'method': '0xf69e2046'
        }
    },
    'BANKROLL': {
        'provideLiquidity': {
            'direction': 'OUTGOING',
            'description': 'Provides bankroll liquidity',
            'method': '0xe8e33700'
        },
        'withdrawLiquidity': {
            'direction': 'INCOMING',
            'description': 'Withdraws bankroll liquidity',
            'method': '0xbaa2abde'
        },
        'claimBankrollRewards': {
            'direction': 'INCOMING',
            'description': 'Claims bankroll rewards',
            'method': '0xe6f1daf2'
        }
    }
}

# Combined functions for all versions
BETSWIRL_FUNCTIONS = {
    'V1': BETSWIRL_V1_FUNCTIONS
}