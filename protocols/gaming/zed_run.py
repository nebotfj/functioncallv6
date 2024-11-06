"""ZED RUN Protocol Functions for all versions"""

ZED_RUN_V1_FUNCTIONS = {
    'RACING': {
        'enterRace': {
            'direction': 'OUTGOING',
            'description': 'Enters horse in race',
            'method': '0x1698ee82'
        },
        'claimPrize': {
            'direction': 'INCOMING',
            'description': 'Claims race winnings',
            'method': '0x4e71d92d'
        },
        'breedHorses': {
            'direction': 'OUTGOING',
            'description': 'Breeds new horse',
            'method': '0x8f38249c'
        },
        'sellHorse': {
            'direction': 'INCOMING',
            'description': 'Sells horse NFT',
            'method': '0x454a2ab3'
        }
    },
    'STAKING': {
        'stakeWETH': {
            'direction': 'OUTGOING',
            'description': 'Stakes WETH tokens',
            'method': '0xa694fc3a'
        },
        'unstakeWETH': {
            'direction': 'INCOMING',
            'description': 'Unstakes WETH tokens',
            'method': '0x2e1a7d4d'
        },
        'claimRewards': {
            'direction': 'INCOMING',
            'description': 'Claims staking rewards',
            'method': '0xe6f1daf2'
        }
    },
    'TOURNAMENTS': {
        'registerTournament': {
            'direction': 'OUTGOING',
            'description': 'Registers for tournament',
            'method': '0x9b3d47b4'
        },
        'claimTournamentRewards': {
            'direction': 'INCOMING',
            'description': 'Claims tournament prizes',
            'method': '0x4e71d92d'
        },
        'withdrawEntry': {
            'direction': 'INCOMING',
            'description': 'Withdraws tournament entry',
            'method': '0x69328dec'
        }
    }
}

# Combined functions for all versions
ZED_RUN_FUNCTIONS = {
    'V1': ZED_RUN_V1_FUNCTIONS
}