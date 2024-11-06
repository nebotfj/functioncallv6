"""ERC1155 Token Protocol Functions"""

ERC1155_V1_FUNCTIONS = {
    'BASIC': {
        'safeTransferFrom': {
            'direction': 'OUTGOING',
            'description': 'Safely transfers tokens',
            'method': '0xf242432a'
        },
        'safeBatchTransferFrom': {
            'direction': 'OUTGOING',
            'description': 'Transfers multiple tokens',
            'method': '0x2eb2c2d6'
        },
        'setApprovalForAll': {
            'direction': 'OUTGOING',
            'description': 'Approves operator for all tokens',
            'method': '0xa22cb465'
        }
    },
    'MINT': {
        'mint': {
            'direction': 'OUTGOING',
            'description': 'Mints new tokens',
            'method': '0x40c10f19'
        },
        'mintBatch': {
            'direction': 'OUTGOING',
            'description': 'Mints multiple tokens',
            'method': '0x1f7fdffa'
        },
        'burn': {
            'direction': 'OUTGOING',
            'description': 'Burns tokens',
            'method': '0x42966c68'
        },
        'burnBatch': {
            'direction': 'OUTGOING',
            'description': 'Burns multiple tokens',
            'method': '0x6b20c454'
        }
    },
    'URI': {
        'setURI': {
            'direction': 'OUTGOING',
            'description': 'Sets token metadata URI',
            'method': '0x02fe5305'
        },
        'setBaseURI': {
            'direction': 'OUTGOING',
            'description': 'Sets base URI for all tokens',
            'method': '0x55f804b3'
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
ERC1155_FUNCTIONS = {
    'V1': ERC1155_V1_FUNCTIONS
}