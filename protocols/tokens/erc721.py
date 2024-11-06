"""ERC721 Token Protocol Functions"""

ERC721_V1_FUNCTIONS = {
    'BASIC': {
        'safeTransferFrom': {
            'direction': 'OUTGOING',
            'description': 'Safely transfers NFT',
            'method': '0x42842e0e'
        },
        'transferFrom': {
            'direction': 'OUTGOING',
            'description': 'Transfers NFT',
            'method': '0x23b872dd'
        },
        'approve': {
            'direction': 'OUTGOING',
            'description': 'Approves NFT transfer',
            'method': '0x095ea7b3'
        },
        'setApprovalForAll': {
            'direction': 'OUTGOING',
            'description': 'Approves operator for all NFTs',
            'method': '0xa22cb465'
        }
    },
    'MINT': {
        'safeMint': {
            'direction': 'OUTGOING',
            'description': 'Safely mints new NFT',
            'method': '0x40d097c3'
        },
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new NFT',
            'method': '0x40c10f19'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns existing NFT',
            'method': '0x42966c68'
        }
    },
    'METADATA': {
        'setBaseURI': {
            'direction': 'OUTGOING',
            'description': 'Sets base URI for metadata',
            'method': '0x55f804b3'
        },
        'setTokenURI': {
            'direction': 'OUTGOING',
            'description': 'Sets specific token URI',
            'method': '0x162094c4'
        },
        'freeze': {
            'direction': 'OUTGOING',
            'description': 'Freezes token metadata',
            'method': '0x62a5af3b'
        }
    },
    'ROYALTIES': {
        'setDefaultRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Sets default royalty',
            'method': '0x4e06fc7f'
        },
        'setTokenRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Sets token specific royalty',
            'method': '0x5e86d2b0'
        },
        'deleteDefaultRoyalty': {
            'direction': 'OUTGOING',
            'description': 'Removes default royalty',
            'method': '0x8e8b8e93'
        }
    }
}

# Combined functions for all versions
ERC721_FUNCTIONS = {
    'V1': ERC721_V1_FUNCTIONS
}