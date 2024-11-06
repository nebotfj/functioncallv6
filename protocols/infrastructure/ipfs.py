"""IPFS Protocol Functions for all versions"""

IPFS_V1_FUNCTIONS = {
    'STORAGE': {
        'addFile': {
            'direction': 'OUTGOING',
            'description': 'Adds file to IPFS',
            'method': '0x1698ee82'
        },
        'getFile': {
            'direction': 'INCOMING',
            'description': 'Retrieves IPFS file',
            'method': '0x69328dec'
        },
        'pinFile': {
            'direction': 'OUTGOING',
            'description': 'Pins file to node',
            'method': '0x7535d246'
        },
        'unpinFile': {
            'direction': 'OUTGOING',
            'description': 'Unpins file from node',
            'method': '0x2e1a7d4d'
        }
    },
    'PINNING': {
        'addPinningService': {
            'direction': 'OUTGOING',
            'description': 'Adds remote pinning service',
            'method': '0x1698ee82'
        },
        'removePinningService': {
            'direction': 'OUTGOING',
            'description': 'Removes pinning service',
            'method': '0x2e1a7d4d'
        },
        'listPinnedFiles': {
            'direction': 'NEUTRAL',
            'description': 'Lists pinned files',
            'method': '0x9d2f32dd'
        }
    },
    'PUBSUB': {
        'publish': {
            'direction': 'OUTGOING',
            'description': 'Publishes to topic',
            'method': '0x7535d246'
        },
        'subscribe': {
            'direction': 'INCOMING',
            'description': 'Subscribes to topic',
            'method': '0x9b3d47b4'
        },
        'unsubscribe': {
            'direction': 'OUTGOING',
            'description': 'Unsubscribes from topic',
            'method': '0x2e1a7d4d'
        }
    },
    'NAMING': {
        'publishName': {
            'direction': 'OUTGOING',
            'description': 'Publishes IPNS name',
            'method': '0x1698ee82'
        },
        'resolveName': {
            'direction': 'NEUTRAL',
            'description': 'Resolves IPNS name',
            'method': '0x9d2f32dd'
        }
    }
}

# Combined functions for all versions
IPFS_FUNCTIONS = {
    'V1': IPFS_V1_FUNCTIONS
}