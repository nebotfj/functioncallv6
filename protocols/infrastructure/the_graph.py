"""The Graph Protocol Functions for all versions"""

THE_GRAPH_V1_FUNCTIONS = {
    'INDEXING': {
        'stake': {
            'direction': 'OUTGOING',
            'description': 'Stakes GRT tokens',
            'method': '0xa694fc3a'
        },
        'unstake': {
            'direction': 'INCOMING',
            'description': 'Unstakes GRT tokens',
            'method': '0x2e1a7d4d'
        },
        'delegate': {
            'direction': 'OUTGOING',
            'description': 'Delegates to indexer',
            'method': '0x5c19a95c'
        },
        'undelegate': {
            'direction': 'INCOMING',
            'description': 'Undelegates from indexer',
            'method': '0x4c5c0b7d'
        }
    },
    'CURATION': {
        'signal': {
            'direction': 'OUTGOING',
            'description': 'Signals on subgraph',
            'method': '0x7535d246'
        },
        'unsignal': {
            'direction': 'INCOMING',
            'description': 'Removes signal from subgraph',
            'method': '0x2e1a7d4d'
        },
        'withdraw': {
            'direction': 'INCOMING',
            'description': 'Withdraws curation shares',
            'method': '0x69328dec'
        }
    },
    'REWARDS': {
        'claimIndexingRewards': {
            'direction': 'INCOMING',
            'description': 'Claims indexer rewards',
            'method': '0x4e71d92d'
        },
        'claimDelegationRewards': {
            'direction': 'INCOMING',
            'description': 'Claims delegation rewards',
            'method': '0xe6f1daf2'
        }
    },
    'SUBGRAPHS': {
        'publishSubgraph': {
            'direction': 'OUTGOING',
            'description': 'Publishes new subgraph',
            'method': '0x1698ee82'
        },
        'deprecateSubgraph': {
            'direction': 'OUTGOING',
            'description': 'Deprecates existing subgraph',
            'method': '0x2e1a7d4d'
        },
        'updateSubgraph': {
            'direction': 'OUTGOING',
            'description': 'Updates subgraph version',
            'method': '0x7535d246'
        }
    }
}

# Combined functions for all versions
THE_GRAPH_FUNCTIONS = {
    'V1': THE_GRAPH_V1_FUNCTIONS
}