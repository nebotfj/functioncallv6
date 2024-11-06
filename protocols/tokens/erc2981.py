"""ERC2981 NFT Royalty Standard Functions"""

ERC2981_V1_FUNCTIONS = {
    'ROYALTIES': {
        'setDefaultRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Sets default royalty info',
            'method': '0x4e06fc7f'
        },
        'deleteDefaultRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Removes default royalty',
            'method': '0x8e8b8e93'
        },
        'setTokenRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Sets token specific royalty',
            'method': '0x5e86d2b0'
        },
        'resetTokenRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Resets token royalty',
            'method': '0x0cad0bfa'
        }
    },
    'INFO': {
        'royaltyInfo': {
            'direction': 'NEUTRAL',
            'description': 'Gets royalty information',
            'method': '0x2a55205a'
        },
        'supportsInterface': {
            'direction': 'NEUTRAL',
            'description': 'Checks interface support',
            'method': '0x01ffc9a7'
        }
    }
}

# Combined functions for all versions
ERC2981_FUNCTIONS = {
    'V1': ERC2981_V1_FUNCTIONS
}