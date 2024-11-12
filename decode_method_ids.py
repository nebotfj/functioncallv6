from eth_hash.auto import keccak
from typing import Optional, Tuple, Dict, List
import binascii
import requests


import os
import csv
import tkinter as tk
from tkinter import scrolledtext, messagebox
import pandas as pd


import protocols

from protocols.bridges import across, allbridge, arbitrum, celer, hop, layerzero, multichain, optimism, orbiter, polygon, portal, stargate, symbiosis, synapse, wormhole
from protocols.derivatives import drift, dydx, gains, gmx, hubble, kwenta, level, mycelium, perpetual, polynomial, ribbon, synthetix, vela
from protocols.dex import balancer, bancor, beethoven, biswap, camelot, chronos, curve, dodo, dystopia, gmx, gnosis, hashflow, kyberswap, loopring, maverick, meshswap, mixswap, oneinch, orca, pancakeswap, paraswap, platypus, quickswap, ramses, raydium, solidly, spiritswap, spookyswap, sushiswap, traderjoe, uniswap, velodrome, vulpefi, wombat, zapper, zerion, zeroex, zyberswap
from protocols. gaming import axie, augur, betswirl, bigtime, crypto_unicorns, decentral, defi_kingdoms, ember_sword, gala, gods_unchained, illuvium, pegaxy, polymarket, rollbit, sorare, splinterlands, star_atlas, stepn, thetan_arena, wallfair, zed_run
from protocols.identity import brightid, civic, polygonid, worldcoin
from protocols.infrastructure import arweave, filecoin, ipfs, pocket, the_graph
from protocols.insurance import insurace, nexus_mutual, unslashed
from protocols. launchpad import bullperks, coinlist, copper_launch, daomaker, gamefi, gamestarter, pinksale, polkastarter, seedify
from protocols.lending import aave, benqi, compound, cream, euler, frax, geist, granary, hundred, ironbank, maple, maker, morpho, radiant, venus
from protocols.mev import cowswap, eden, flashbots, manifold, rook
from protocols.nft import blur, looksrare, magiceden, nftx, opensea, rarible, sudoswap, x2y2
from protocols.options import dopex, hegic, lyra, premia
from protocols.oracles import api3, band, chainlink, dia, pyth, redstone, tellor, uma, umbrella
from protocols.privacy import aztec, monero, railway, tornado, zcash
from protocols.rwa import centrifuge, goldfinch, maple, truefi
from protocols.social_media import farcaster, friend_tech, lens
from protocols.staking import ankr, binance, eigenlayer, lido, mantle, oeth, rocketpool, stader, stakestone, stakewise, swell
from protocols.tokens import erc1155, erc20, erc2981, erc3525, erc4626, erc5192, erc721
from protocols.tokens import restos
from protocols.yield_farming import alpaca, beefy, concentrator, convex, jones, pickle, pirex, redacted, yearn, yield_yak

#BRIDGES
from protocols.bridges.across import ACROSS_FUNCTIONS
from protocols.bridges.allbridge import ALLBRIDGE_FUNCTIONS
from protocols.bridges.arbitrum import ARBITRUM_FUNCTIONS
from protocols.bridges.celer import CELER_FUNCTIONS
from protocols.bridges.hop import HOP_FUNCTIONS
from protocols.bridges.layerzero import LAYERZERO_FUNCTIONS
from protocols.bridges.multichain import MULTICHAIN_FUNCTIONS
from protocols.bridges.optimism import OPTIMISM_FUNCTIONS
from protocols.bridges.orbiter import ORBITER_FUNCTIONS
from protocols.bridges.polygon import POLYGON_FUNCTIONS
from protocols.bridges.portal import PORTAL_FUNCTIONS
from protocols.bridges.stargate import STARGATE_FUNCTIONS
from protocols.bridges.symbiosis import SYMBIOSIS_FUNCTIONS
from protocols.bridges.synapse import SYNAPSE_FUNCTIONS
from protocols.bridges.wormhole import WORMHOLE_FUNCTIONS

# DERIVATIVES
from protocols.derivatives.drift import DRIFT_FUNCTIONS
from protocols.derivatives.dydx import DYDX_FUNCTIONS
from protocols.derivatives.gains import GAINS_FUNCTIONS
from protocols.derivatives.gmx import GMX_FUNCTIONS
from protocols.derivatives.hubble import HUBBLE_FUNCTIONS
from protocols.derivatives.kwenta import KWENTA_FUNCTIONS
from protocols.derivatives.level import LEVEL_FUNCTIONS
from protocols.derivatives.mycelium import MYCELIUM_FUNCTIONS
from protocols.derivatives.perpetual import PERP_FUNCTIONS
from protocols.derivatives.polynomial import POLYNOMIAL_FUNCTIONS
from protocols.derivatives.ribbon import RIBBON_FUNCTIONS
from protocols.derivatives.synthetix import SYNTHETIX_FUNCTIONS
from protocols.derivatives.vela import VELA_FUNCTIONS

# DEX
from protocols.dex.balancer import BALANCER_FUNCTIONS
from protocols.dex.bancor import BANCOR_FUNCTIONS
from protocols.dex.beethoven import BEETHOVEN_FUNCTIONS
from protocols.dex.biswap import BISWAP_FUNCTIONS
from protocols.dex.camelot import CAMELOT_FUNCTIONS
from protocols.dex.chronos import CHRONOS_FUNCTIONS
from protocols.dex.curve import CURVE_FUNCTIONS
from protocols.dex.dodo import DODO_FUNCTIONS
from protocols.dex.dystopia import DYSTOPIA_FUNCTIONS
from protocols.dex.gmx import GMX_FUNCTIONS
from protocols.dex.gnosis import GNOSIS_FUNCTIONS
from protocols.dex.hashflow import HASHFLOW_FUNCTIONS
from protocols.dex.kyberswap import KYBERSWAP_FUNCTIONS
from protocols.dex.loopring import LOOPRING_FUNCTIONS
from protocols.dex.maverick import MAVERICK_FUNCTIONS
from protocols.dex.meshswap import MESHSWAP_FUNCTIONS
from protocols.dex.mixswap import MIXSWAP_FUNCTIONS
from protocols.dex.oneinch import ONEINCH_FUNCTIONS
from protocols.dex.orca import ORCA_FUNCTIONS
from protocols.dex.pancakeswap import PANCAKESWAP_FUNCTIONS
from protocols.dex.paraswap import PARASWAP_FUNCTIONS
from protocols.dex.platypus import PLATYPUS_FUNCTIONS
from protocols.dex.quickswap import QUICKSWAP_FUNCTIONS
from protocols.dex.ramses import RAMSES_FUNCTIONS
from protocols.dex.raydium import RAYDIUM_FUNCTIONS
from protocols.dex.solidly import SOLIDLY_FUNCTIONS
from protocols.dex.spiritswap import SPIRITSWAP_FUNCTIONS
from protocols.dex.spookyswap import SPOOKYSWAP_FUNCTIONS
from protocols.dex.sushiswap import SUSHISWAP_FUNCTIONS
from protocols.dex.traderjoe import TRADERJOE_FUNCTIONS
from protocols.dex.uniswap import UNISWAP_FUNCTIONS
from protocols.dex.velodrome import VELODROME_FUNCTIONS
from protocols.dex.vulpefi import VULPEFI_FUNCTIONS
from protocols.dex.wombat import WOMBAT_FUNCTIONS
from protocols.dex.zapper import ZAPPER_FUNCTIONS
from protocols.dex.zerion import ZERION_FUNCTIONS
from protocols.dex.zeroex import ZEROEX_FUNCTIONS
from protocols.dex.zyberswap import ZYBERSWAP_FUNCTIONS

# GAMING
from protocols.gaming.axie import AXIE_FUNCTIONS
from protocols.gaming.augur import AUGUR_FUNCTIONS
from protocols.gaming.betswirl import BETSWIRL_FUNCTIONS
from protocols.gaming.bigtime import BIGTIME_FUNCTIONS
from protocols.gaming.crypto_unicorns import CRYPTO_UNICORNS_FUNCTIONS
from protocols.gaming.decentral import DECENTRAL_FUNCTIONS
from protocols.gaming.defi_kingdoms import DEFI_KINGDOMS_FUNCTIONS
from protocols.gaming.ember_sword import EMBER_SWORD_FUNCTIONS
from protocols.gaming.gala import GALA_FUNCTIONS
from protocols.gaming.gods_unchained import GODS_UNCHAINED_FUNCTIONS
from protocols.gaming.illuvium import ILLUVIUM_FUNCTIONS
from protocols.gaming.pegaxy import PEGAXY_FUNCTIONS
from protocols.gaming.polymarket import POLYMARKET_FUNCTIONS
from protocols.gaming.rollbit import ROLLBIT_FUNCTIONS
from protocols.gaming.sorare import SORARE_FUNCTIONS
from protocols.gaming.splinterlands import SPLINTERLANDS_FUNCTIONS
from protocols.gaming.star_atlas import STAR_ATLAS_FUNCTIONS
from protocols.gaming.stepn import STEPN_FUNCTIONS
from protocols.gaming.thetan_arena import THETAN_ARENA_FUNCTIONS
from protocols.gaming.wallfair import WALLFAIR_FUNCTIONS
from protocols.gaming.zed_run import ZED_RUN_FUNCTIONS

# IDENTITY
from protocols.identity.brightid import BRIGHTID_FUNCTIONS
from protocols.identity.civic import CIVIC_FUNCTIONS
from protocols.identity.polygonid import POLYGONID_FUNCTIONS
from protocols.identity.worldcoin import WORLDCOIN_FUNCTIONS

# INFRASTRUCTURE
from protocols.infrastructure.arweave import ARWEAVE_FUNCTIONS
from protocols.infrastructure.filecoin import FILECOIN_FUNCTIONS
from protocols.infrastructure.ipfs import IPFS_FUNCTIONS
from protocols.infrastructure.pocket import POCKET_FUNCTIONS
from protocols.infrastructure.the_graph import THE_GRAPH_FUNCTIONS

# INSURANCE
from protocols.insurance.insurace import INSURACE_FUNCTIONS
from protocols.insurance.nexus_mutual import NEXUS_MUTUAL_FUNCTIONS
from protocols.insurance.unslashed import UNSLASHED_FUNCTIONS

# LAUNCHPAD
from protocols.launchpad.bullperks import BULLPERKS_FUNCTIONS
from protocols.launchpad.coinlist import COINLIST_FUNCTIONS
from protocols.launchpad.copper_launch import COPPER_LAUNCH_FUNCTIONS
from protocols.launchpad.daomaker import DAOMAKER_FUNCTIONS
from protocols.launchpad.gamefi import GAMEFI_FUNCTIONS
from protocols.launchpad.gamestarter import GAMESTARTER_FUNCTIONS
from protocols.launchpad.pinksale import PINKSALE_FUNCTIONS
from protocols.launchpad.polkastarter import POLKASTARTER_FUNCTIONS
from protocols.launchpad.seedify import SEEDIFY_FUNCTIONS

# LENDING
from protocols.lending.aave import AAVE_FUNCTIONS
from protocols.lending.benqi import BENQI_FUNCTIONS
from protocols.lending.compound import COMPOUND_FUNCTIONS
from protocols.lending.cream import CREAM_FUNCTIONS
from protocols.lending.euler import EULER_FUNCTIONS
from protocols.lending.frax import FRAX_FUNCTIONS
from protocols.lending.geist import GEIST_FUNCTIONS
from protocols.lending.granary import GRANARY_FUNCTIONS
from protocols.lending.hundred import HUNDRED_FUNCTIONS
from protocols.lending.ironbank import IRONBANK_FUNCTIONS
from protocols.lending.maple import MAPLE_FUNCTIONS
from protocols.lending.maker import MAKER_FUNCTIONS
from protocols.lending.morpho import MORPHO_FUNCTIONS
from protocols.lending.radiant import RADIANT_FUNCTIONS
from protocols.lending.venus import VENUS_FUNCTIONS

# MEV
from protocols.mev.cowswap import COWSWAP_FUNCTIONS
from protocols.mev.eden import EDEN_FUNCTIONS
from protocols.mev.flashbots import FLASHBOTS_FUNCTIONS
from protocols.mev.manifold import MANIFOLD_FUNCTIONS
from protocols.mev.rook import ROOK_FUNCTIONS

# NFT
from protocols.nft.blur import BLUR_FUNCTIONS
from protocols.nft.looksrare import LOOKSRARE_FUNCTIONS
from protocols.nft.magiceden import MAGICEDEN_FUNCTIONS
from protocols.nft.nftx import NFTX_FUNCTIONS
from protocols.nft.opensea import OPENSEA_FUNCTIONS
from protocols.nft.rarible import RARIBLE_FUNCTIONS
from protocols.nft.sudoswap import SUDOSWAP_FUNCTIONS
from protocols.nft.x2y2 import X2Y2_FUNCTIONS

# OPTIONS
from protocols.options.dopex import DOPEX_FUNCTIONS
from protocols.options.hegic import HEGIC_FUNCTIONS
from protocols.options.lyra import LYRA_FUNCTIONS
from protocols.options.premia import PREMIA_FUNCTIONS

# ORACLES
from protocols.oracles.api3 import API3_FUNCTIONS
from protocols.oracles.band import BAND_FUNCTIONS
from protocols.oracles.chainlink import CHAINLINK_FUNCTIONS
from protocols.oracles.dia import DIA_FUNCTIONS
from protocols.oracles.pyth import PYTH_FUNCTIONS
from protocols.oracles.redstone import REDSTONE_FUNCTIONS
from protocols.oracles.tellor import TELLOR_FUNCTIONS
from protocols.oracles.uma import UMA_FUNCTIONS
from protocols.oracles.umbrella import UMBRELLA_FUNCTIONS

# PRIVACY
from protocols.privacy.aztec import AZTEC_FUNCTIONS
from protocols.privacy.monero import MONERO_FUNCTIONS
from protocols.privacy.railway import RAILWAY_FUNCTIONS
from protocols.privacy.tornado import TORNADO_FUNCTIONS
from protocols.privacy.zcash import ZCASH_FUNCTIONS

# RWA
from protocols.rwa.centrifuge import CENTRIFUGE_FUNCTIONS
from protocols.rwa.goldfinch import GOLDFINCH_FUNCTIONS
from protocols.rwa.maple import MAPLE_FUNCTIONS
from protocols.rwa.truefi import TRUEFI_FUNCTIONS

# SOCIAL MEDIA
from protocols.social_media.farcaster import FARCASTER_FUNCTIONS
from protocols.social_media.friend_tech import FRIEND_TECH_FUNCTIONS
from protocols.social_media.lens import LENS_FUNCTIONS

# STAKING
from protocols.staking.ankr import ANKR_FUNCTIONS
from protocols.staking.binance import BINANCE_FUNCTIONS
from protocols.staking.eigenlayer import EIGENLAYER_FUNCTIONS
from protocols.staking.lido import LIDO_FUNCTIONS
from protocols.staking.mantle import MANTLE_FUNCTIONS
from protocols.staking.oeth import OETH_FUNCTIONS
from protocols.staking.rocketpool import ROCKETPOOL_FUNCTIONS
from protocols.staking.stader import STADER_FUNCTIONS
from protocols.staking.stakestone import STAKESTONE_FUNCTIONS
from protocols.staking.stakewise import STAKEWISE_FUNCTIONS
from protocols.staking.swell import SWELL_FUNCTIONS

# TOKENS
from protocols.tokens.erc1155 import ERC1155_FUNCTIONS
from protocols.tokens.erc20 import ERC20_FUNCTIONS
from protocols.tokens.erc2981 import ERC2981_FUNCTIONS
from protocols.tokens.erc3525 import ERC3525_FUNCTIONS
from protocols.tokens.erc4626 import ERC4626_FUNCTIONS
from protocols.tokens.erc5192 import ERC5192_FUNCTIONS
from protocols.tokens.erc721 import ERC721_FUNCTIONS
#RESTOS
from protocols.tokens.restos import ETH_GENERIC

# YIELD FARMING
from protocols.yield_farming.alpaca import ALPACA_FUNCTIONS
from protocols.yield_farming.beefy import BEEFY_FUNCTIONS
from protocols.yield_farming.concentrator import CONCENTRATOR_FUNCTIONS
from protocols.yield_farming.convex import CONVEX_FUNCTIONS
from protocols.yield_farming.jones import JONES_FUNCTIONS
from protocols.yield_farming.pickle import PICKLE_FUNCTIONS
from protocols.yield_farming.pirex import PIREX_FUNCTIONS
from protocols.yield_farming.redacted import REDACTED_FUNCTIONS
from protocols.yield_farming.yearn import YEARN_FUNCTIONS
from protocols.yield_farming.yield_yak import YIELD_YAK_FUNCTIONS



#

def search_function(function_name):
    protocols = {
        #RESTOS
    "ETH_GENERIC": ETH_GENERIC,

        # BRIDGES
    "ACROSS": ACROSS_FUNCTIONS,
    "ALLBRIDGE": ALLBRIDGE_FUNCTIONS,
    "ARBITRUM": ARBITRUM_FUNCTIONS,
    "CELER": CELER_FUNCTIONS,
    "HOP": HOP_FUNCTIONS,
    "LAYERZERO": LAYERZERO_FUNCTIONS,
    "MULTICHAIN": MULTICHAIN_FUNCTIONS,
    "OPTIMISM": OPTIMISM_FUNCTIONS,
    "ORBITER": ORBITER_FUNCTIONS,
    "POLYGON": POLYGON_FUNCTIONS,
    "PORTAL": PORTAL_FUNCTIONS,
    "STARGATE": STARGATE_FUNCTIONS,
    "SYMBIOSIS": SYMBIOSIS_FUNCTIONS,
    "SYNAPSE": SYNAPSE_FUNCTIONS,
    "WORMHOLE": WORMHOLE_FUNCTIONS,

    # DERIVATIVES
    "DRIFT": DRIFT_FUNCTIONS,
    "DYDX": DYDX_FUNCTIONS,
    "GAINS": GAINS_FUNCTIONS,
    "GMX": GMX_FUNCTIONS,
    "HUBBLE": HUBBLE_FUNCTIONS,
    "KWENTA": KWENTA_FUNCTIONS,
    "LEVEL": LEVEL_FUNCTIONS,
    "MYCELIUM": MYCELIUM_FUNCTIONS,
    "PERPETUAL": PERP_FUNCTIONS,
    "POLYNOMIAL": POLYNOMIAL_FUNCTIONS,
    "RIBBON": RIBBON_FUNCTIONS,
    "SYNTHETIX": SYNTHETIX_FUNCTIONS,
    "VELA": VELA_FUNCTIONS,

    # DEX
    "BALANCER": BALANCER_FUNCTIONS,
    "BANCOR": BANCOR_FUNCTIONS,
    "BEETHOVEN": BEETHOVEN_FUNCTIONS,
    "BISWAP": BISWAP_FUNCTIONS,
    "CAMELOT": CAMELOT_FUNCTIONS,
    "CHRONOS": CHRONOS_FUNCTIONS,
    "CURVE": CURVE_FUNCTIONS,
    "DODO": DODO_FUNCTIONS,
    "DYSTOPIA": DYSTOPIA_FUNCTIONS,
    "GMX": GMX_FUNCTIONS,
    "GNOSIS": GNOSIS_FUNCTIONS,
    "HASHFLOW": HASHFLOW_FUNCTIONS,
    "KYBERSWAP": KYBERSWAP_FUNCTIONS,
    "LOOPRING": LOOPRING_FUNCTIONS,
    "MAVERICK": MAVERICK_FUNCTIONS,
    "MESH_SWAP": MESHSWAP_FUNCTIONS,
    "MIX_SWAP": MIXSWAP_FUNCTIONS,
    "ONEINCH": ONEINCH_FUNCTIONS,
    "ORCA": ORCA_FUNCTIONS,
    "PANCAKESWAP": PANCAKESWAP_FUNCTIONS,
    "PARASWAP": PARASWAP_FUNCTIONS,
    "PLATYPUS": PLATYPUS_FUNCTIONS,
    "QUICKSWAP": QUICKSWAP_FUNCTIONS,
    "RAMSES": RAMSES_FUNCTIONS,
    "RAYDIUM": RAYDIUM_FUNCTIONS,
    "SOLIDLY": SOLIDLY_FUNCTIONS,
    "SPIRITSWAP": SPIRITSWAP_FUNCTIONS,
    "SPOOKYSWAP": SPOOKYSWAP_FUNCTIONS,
    "SUSHISWAP": SUSHISWAP_FUNCTIONS,
    "TRADERJOE": TRADERJOE_FUNCTIONS,
    "UNISWAP": UNISWAP_FUNCTIONS,
    "VELODROME": VELODROME_FUNCTIONS,
    "VULPEFI": VULPEFI_FUNCTIONS,
    "WOMBAT": WOMBAT_FUNCTIONS,
    "ZAPPER": ZAPPER_FUNCTIONS,
    "ZERION": ZERION_FUNCTIONS,
    "ZEROEX": ZEROEX_FUNCTIONS,
    "ZYBERSWAP": ZYBERSWAP_FUNCTIONS,

    # GAMING
    "AXIE": AXIE_FUNCTIONS,
    "AUGUR" :  AUGUR_FUNCTIONS,
    "BETSWIRL": BETSWIRL_FUNCTIONS,
    "BIGTIME": BIGTIME_FUNCTIONS,
    "CRYPTO_UNICORNS": CRYPTO_UNICORNS_FUNCTIONS,
    "DECENTRAL": DECENTRAL_FUNCTIONS,
    "DEFI_KINGDOMS": DEFI_KINGDOMS_FUNCTIONS,
    "EMBER_SWORD": EMBER_SWORD_FUNCTIONS,
    "GALA": GALA_FUNCTIONS,
    "GODS_UNCHAINED": GODS_UNCHAINED_FUNCTIONS,
    "ILLUVIUM": ILLUVIUM_FUNCTIONS,
    "PEGAXY": PEGAXY_FUNCTIONS,
    "POLYMARKET": POLYMARKET_FUNCTIONS,
    "ROLLBIT": ROLLBIT_FUNCTIONS,
    "SORARE": SORARE_FUNCTIONS,
    "SPLINTERLANDS": SPLINTERLANDS_FUNCTIONS,
    "STAR_ATLAS": STAR_ATLAS_FUNCTIONS,
    "STEPN": STEPN_FUNCTIONS,
    "THETAN_ARENA": THETAN_ARENA_FUNCTIONS,
    "WALLFAIR": WALLFAIR_FUNCTIONS,
    "ZED_RUN": ZED_RUN_FUNCTIONS,

    # IDENTITY
    "BRIGHTID": BRIGHTID_FUNCTIONS,
    "CIVIC": CIVIC_FUNCTIONS,
    "POLYGONID": POLYGONID_FUNCTIONS,
    "WORLDCOIN": WORLDCOIN_FUNCTIONS,

    # INFRASTRUCTURE
    "ARWEAVE": ARWEAVE_FUNCTIONS,
    "FILECOIN": FILECOIN_FUNCTIONS,
    "IPFS": IPFS_FUNCTIONS,
    "POCKET": POCKET_FUNCTIONS,
    "THE_GRAPH": THE_GRAPH_FUNCTIONS,

    # INSURANCE
    "INSURACE": INSURACE_FUNCTIONS,
    "NEXUS_MUTUAL": NEXUS_MUTUAL_FUNCTIONS,
    "UNSLASHED": UNSLASHED_FUNCTIONS,

    # LAUNCHPAD
    "BULLPERKS": BULLPERKS_FUNCTIONS,
    "COINLIST": COINLIST_FUNCTIONS,
    "COPPER_LAUNCH": COPPER_LAUNCH_FUNCTIONS,
    "DAOMAKER": DAOMAKER_FUNCTIONS,
    "GAMEFI": GAMEFI_FUNCTIONS,
    "GAMESTARTER": GAMESTARTER_FUNCTIONS,
    "PINKSALE": PINKSALE_FUNCTIONS,
    "POLKSTARTER": POLKASTARTER_FUNCTIONS,
    "SEEDIFY": SEEDIFY_FUNCTIONS,

    # LENDING
    "AAVE": AAVE_FUNCTIONS,
    "BENQI": BENQI_FUNCTIONS,
    "COMPOUND": COMPOUND_FUNCTIONS,
    "CREAM": CREAM_FUNCTIONS,
    "EULER": EULER_FUNCTIONS,
    "FRAX": FRAX_FUNCTIONS,
    "GEIST": GEIST_FUNCTIONS,
    "GRANARY": GRANARY_FUNCTIONS,
    "HUNDRED": HUNDRED_FUNCTIONS,
    "IRONBANK": IRONBANK_FUNCTIONS,
    "MAPLE": MAPLE_FUNCTIONS,
    "MAKER": MAKER_FUNCTIONS,
    "MORPHO": MORPHO_FUNCTIONS,
    "RADIANT": RADIANT_FUNCTIONS,
    "VENUS": VENUS_FUNCTIONS,

    # MEV
    "COWSWAP": COWSWAP_FUNCTIONS,
    "EDEN": EDEN_FUNCTIONS,
    "FLASHBOTS": FLASHBOTS_FUNCTIONS,
    "MANIFOLD": MANIFOLD_FUNCTIONS,
    "ROOK": ROOK_FUNCTIONS,

    # NFT
    "BLUR": BLUR_FUNCTIONS,
    "LOOKSRARE": LOOKSRARE_FUNCTIONS,
    "MAGICEDEN": MAGICEDEN_FUNCTIONS,
    "NFTX": NFTX_FUNCTIONS,
    "OPENSEA": OPENSEA_FUNCTIONS,
    "RARIBLE": RARIBLE_FUNCTIONS,
    "SUDOSWAP": SUDOSWAP_FUNCTIONS,
    "X2Y2": X2Y2_FUNCTIONS,

    # OPTIONS
    "DOPEX": DOPEX_FUNCTIONS,
    "HEGIC": HEGIC_FUNCTIONS,
    "LYRA": LYRA_FUNCTIONS,
    "PREMIA": PREMIA_FUNCTIONS,

    # ORACLES
    "API3": API3_FUNCTIONS,
    "BAND": BAND_FUNCTIONS,
    "CHAINLINK": CHAINLINK_FUNCTIONS,
    "DIA": DIA_FUNCTIONS,
    "PYTH": PYTH_FUNCTIONS,
    "REDSTONE": REDSTONE_FUNCTIONS,
    "TELLOR": TELLOR_FUNCTIONS,
    "UMA": UMA_FUNCTIONS,
    "UMBRELLA": UMBRELLA_FUNCTIONS,

    # PRIVACY
    "AZTEC": AZTEC_FUNCTIONS,
    "MONERO": MONERO_FUNCTIONS,
    "RAILWAY": RAILWAY_FUNCTIONS,
    "TORNADO": TORNADO_FUNCTIONS,
    "ZCASH": ZCASH_FUNCTIONS,

    # RWA
    "CENTRIFUGE": CENTRIFUGE_FUNCTIONS,
    "GOLDFINCH": GOLDFINCH_FUNCTIONS,
    "MAPLE": MAPLE_FUNCTIONS,
    "TRUEFI": TRUEFI_FUNCTIONS,

    # SOCIAL_MEDIA
    "FARCASTER": FARCASTER_FUNCTIONS,
    "FRIEND_TECH": FRIEND_TECH_FUNCTIONS,
    "LENS": LENS_FUNCTIONS,

    # STAKING
    "ANKR": ANKR_FUNCTIONS,
    "BINANCE": BINANCE_FUNCTIONS,
    "EIGENLAYER": EIGENLAYER_FUNCTIONS,
    "LIDO": LIDO_FUNCTIONS,
    "MANTLE": MANTLE_FUNCTIONS,
    "OETH": OETH_FUNCTIONS,
    "ROCKETPOOL": ROCKETPOOL_FUNCTIONS,
    "STADER": STADER_FUNCTIONS,
    "STAKESTONE": STAKESTONE_FUNCTIONS,
    "STAKEWISE": STAKEWISE_FUNCTIONS,
    "SWELL": SWELL_FUNCTIONS,

    # TOKENS
    "ERC1155": ERC1155_FUNCTIONS,
    "ERC20": ERC20_FUNCTIONS,
    "ERC2981": ERC2981_FUNCTIONS,
    "ERC3525": ERC3525_FUNCTIONS,
    "ERC4626": ERC4626_FUNCTIONS,
    "ERC5192": ERC5192_FUNCTIONS,
    "ERC721": ERC721_FUNCTIONS,

    # YIELD FARMING
    "ALPACA": ALPACA_FUNCTIONS,
    "BEEFY": BEEFY_FUNCTIONS,
    "CONCENTRATOR": CONCENTRATOR_FUNCTIONS,
    "CONVEX": CONVEX_FUNCTIONS,
    "JONES": JONES_FUNCTIONS,
    "PICKLE": PICKLE_FUNCTIONS,
    "PIREX": PIREX_FUNCTIONS,
    "REDACTED": REDACTED_FUNCTIONS,
    "YEARN": YEARN_FUNCTIONS,
    "YIELD_YAK": YIELD_YAK_FUNCTIONS,

    }
    
    results = []
    
    for protocol_name, protocol_data in protocols.items():
        for version, categories in protocol_data.items():
            for category, functions in categories.items():
                if function_name in functions:
                    # Al encontrar la función, añade los detalles al resultado
                    results.append({
                        'protocol': protocol_name,
                        'version': version,
                        'category': category,
                        'details': functions[function_name]
                        # Guarda los detalles de la función
                    })

    return results



class MethodIdDecoder:
    def __init__(self):
        # Inicializar diccionarios
        self.known_signatures: Dict[str, str] = {
            '0x095ea7b3': 'approve(address,uint256)',
            '0xa9059cbb': 'transfer(address,uint256)',
            '0x23b872dd': 'transferFrom(address,address,uint256)',
            '0xa0712d68': 'mint(uint256)',
            '0x1249c58b': 'mint()',
            '0x40c10f19': 'mint(address,uint256)',
            '0x9dc29fac': 'burn(address,uint256)',
            '0x3ccfd60b': 'withdraw()',
            '0xd0e30db0': 'deposit()',
            '0xa694fc3a': 'stake(uint256)',
            '0xb6b55f25': 'deposit(uint256)',
            '0x2e1a7d4d': 'withdraw(uint256)',
            '0x6a627842': 'mint(address)',
            '0xdf133bca': 'vote(uint256,bool,bool)',
            '0x4e71d92d': 'claim()',
            '0xadc9772e': 'stake(address,uint256)',
            '0x47e7ef24': 'deposit(address,uint256)',
            '0xd85d3d27': 'mint(string)',
            '0xb510391f': 'mint(address,bytes)',
            '0xbe27b22c': 'claim(bytes,bytes)',
            '0x1cff79cd': 'execute(address,bytes)',
            '0x5c19a95c': 'delegate(address)',
            '0x1e83409a': 'claim(address)',
            '0x38ed1739': 'swapExactTokensForTokens(uint256,uint256,address[],address,uint256)',
            '0xf305d719': 'addLiquidityETH(address,uint256,uint256,uint256,address,uint256)',
            '0xe8e33700': 'addLiquidity(address,address,uint256,uint256,uint256,uint256,address,uint256)',
            '0x7ff36ab5': 'swapExactETHForTokens(uint256,address[],address,uint256)',
            '0x18cbafe5': 'swapExactTokensForETH(uint256,uint256,address[],address,uint256)',
            # ... (añadir el resto de signatures del mensaje anterior)
        }
        
        self.known_words: Dict[str, str] = {
            '0x64617461': 'WORD: "data"',
            '0x53686f72': 'WORD: "Shor"',
            '0x456c6f6e': 'WORD: "Elon"',
            '0x52656164': 'WORD: "Read"',
            '0x6e696767': 'WORD: "nigg"',
            '0x466f6c6c': 'WORD: "Foll"',
            '0x43617265': 'WORD: "Care"',
            '0x53686962': 'WORD: "Shib"',
            '0x496d6167': 'WORD: "Imag"',
            # ... (añadir el resto de words del mensaje anterior)
        }

        # Lista exhaustiva de tipos Solidity
        self.common_types = [
            '', # Para funciones sin parámetros
            
            # Tipos básicos
            'bool',
            'string',
            'address',
            'bytes',
            
            # Integers sin signo
            'uint',
            'uint8',
            'uint16',
            'uint24',
            'uint32',
            'uint40',
            'uint48',
            'uint56',
            'uint64',
            'uint72',
            'uint80',
            'uint88',
            'uint96',
            'uint104',
            'uint112',
            'uint120',
            'uint128',
            'uint136',
            'uint144',
            'uint152',
            'uint160',
            'uint168',
            'uint176',
            'uint184',
            'uint192',
            'uint200',
            'uint208',
            'uint216',
            'uint224',
            'uint232',
            'uint240',
            'uint248',
            'uint256',
            
            # Integers con signo
            'int',
            'int8',
            'int16',
            'int24',
            'int32',
            'int40',
            'int48',
            'int56',
            'int64',
            'int72',
            'int80',
            'int88',
            'int96',
            'int104',
            'int112',
            'int120',
            'int128',
            'int136',
            'int144',
            'int152',
            'int160',
            'int168',
            'int176',
            'int184',
            'int192',
            'int200',
            'int208',
            'int216',
            'int224',
            'int232',
            'int240',
            'int248',
            'int256',
            
            # Bytes fijos
            'bytes1',
            'bytes2',
            'bytes3',
            'bytes4',
            'bytes5',
            'bytes6',
            'bytes7',
            'bytes8',
            'bytes9',
            'bytes10',
            'bytes11',
            'bytes12',
            'bytes13',
            'bytes14',
            'bytes15',
            'bytes16',
            'bytes17',
            'bytes18',
            'bytes19',
            'bytes20',
            'bytes21',
            'bytes22',
            'bytes23',
            'bytes24',
            'bytes25',
            'bytes26',
            'bytes27',
            'bytes28',
            'bytes29',
            'bytes30',
            'bytes31',
            'bytes32',
            
            # Arrays
            'bool[]',
            'string[]',
            'address[]',
            'bytes[]',
            'uint[]',
            'uint8[]',
            'uint16[]',
            'uint24[]',
            'uint32[]',
            'uint40[]',
            'uint48[]',
            'uint56[]',
            'uint64[]',
            'uint72[]',
            'uint80[]',
            'uint88[]',
            'uint96[]',
            'uint104[]',
            'uint112[]',
            'uint120[]',
            'uint128[]',
            'uint136[]',
            'uint144[]',
            'uint152[]',
            'uint160[]',
            'uint168[]',
            'uint176[]',
            'uint184[]',
            'uint192[]',
            'uint200[]',
            'uint208[]',
            'uint216[]',
            'uint224[]',
            'uint232[]',
            'uint240[]',
            'uint248[]',
            'uint256[]',
            'int[]',
            'int8[]',
            'int16[]',
            'int24[]',
            'int32[]',
            'int40[]',
            'int48[]',
            'int56[]',
            'int64[]',
            'int72[]',
            'int80[]',
            'int88[]',
            'int96[]',
            'int104[]',
            'int112[]',
            'int120[]',
            'int128[]',
            'int136[]',
            'int144[]',
            'int152[]',
            'int160[]',
            'int168[]',
            'int176[]',
            'int184[]',
            'int192[]',
            'int200[]',
            'int208[]',
            'int216[]',
            'int224[]',
            'int232[]',
            'int240[]',
            'int248[]',
            'int256[]',
            'bytes1[]',
            'bytes2[]',
            'bytes3[]',
            'bytes4[]',
            'bytes5[]',
            'bytes6[]',
            'bytes7[]',
            'bytes8[]',
            'bytes9[]',
            'bytes10[]',
            'bytes11[]',
            'bytes12[]',
            'bytes13[]',
            'bytes14[]',
            'bytes15[]',
            'bytes16[]',
            'bytes17[]',
            'bytes18[]',
            'bytes19[]',
            'bytes20[]',
            'bytes21[]',
            'bytes22[]',
            'bytes23[]',
            'bytes24[]',
            'bytes25[]',
            'bytes26[]',
            'bytes27[]',
            'bytes28[]',
            'bytes29[]',
            'bytes30[]',
            'bytes31[]',
            'bytes32[]',
            
            # Arrays multidimensionales
            'uint256[][]',
            'address[][]',
            'bytes[][]',
            'string[][]',
            
            # Tuplas
            'tuple',
            'tuple[]',
            
            # Fixed/UFixed (aunque son poco comunes)
            'fixed',
            'ufixed',
            
            # Tipos especiales
            'function',
            'contract',
            'enum',
            'struct'
        ]

        # Añadir diccionario de palabras conocidas
        self.known_words = {
            '0x53686f72': 'WORD: "Shor"',
            '0x456c6f6e': 'WORD: "Elon"',
            '0x52656164': 'WORD: "Read"',
            '0x6e696767': 'WORD: "nigg"',
            '0x466f6c6c': 'WORD: "Foll"',
            '0x43617265': 'WORD: "Care"',
            '0x53686962': 'WORD: "Shib"',
            '0x496d6167': 'WORD: "Imag"',
            '0x5368616d': 'WORD: "Sham"',
            '0x68617070': 'WORD: "happ"',
            '0x50656570': 'WORD: "Peep"',
            '0x70657065': 'WORD: "pepe"',
            '0x4e6f7720': 'WORD: "Now "',
            '0x62696c6c': 'WORD: "bill"',
            '0x4c6f7265': 'WORD: "Lore"',
            '0x4920616d': 'WORD: "I am"',
            '0x52656769': 'WORD: "Regi"',
            '0x74657374': 'WORD: "test"',
            '0x0a77656c': 'WORD: "\nwel"',
            '0x53617920': 'WORD: "Say "'
        }

        # Nuevas signatures encontradas
        self.known_signatures = {
            # Uniswap/DEX
            '0x38ed1739': 'swapExactTokensForTokens(uint256,uint256,address[],address,uint256)',
            '0xf305d719': 'addLiquidityETH(address,uint256,uint256,uint256,address,uint256)',
            '0xe8e33700': 'addLiquidity(address,address,uint256,uint256,uint256,uint256,address,uint256)',
            '0x7ff36ab5': 'swapExactETHForTokens(uint256,address[],address,uint256)',
            '0xfb3bdb41': 'swapExactETHForTokensSupportingFeeOnTransferTokens(uint256,address[],address,uint256)',
            
            # Governance/Voting
            '0xdf133bca': 'vote(uint256,bool,bool)',
            '0xb384abef': 'vote(uint256,uint256)',
            '0x5c19a95c': 'delegate(address)',
            '0x9b172b35': 'grantRole(bytes32,address)',
            '0xc8fd6ed0': 'revokeRole(bytes32,address)',
            
            # Staking/Farming
            '0xc04b8d59': 'setPoolParameters(uint256,uint256,uint256)',
            '0xf64db050': 'updatePool(uint256)',
            '0xac9650d8': 'massUpdatePools()',
            '0x0ec32977': 'harvestRewards(uint256)',
            '0x38ef3649': 'harvestAllRewards()',
            '0x88f56f09': 'reinvestRewards()',
            
            # NFT/Marketplace
            '0xd85d3d27': 'mint(string)',
            '0xb510391f': 'mint(address,bytes)',
            '0x94bf804d': 'mint(uint256,address)',
            '0xfaf039f4': 'initialize(address,string,string)',
            '0x8ae541cb': 'setBaseURI(string)',
            
            # Access Control
            '0xe6c6b7f0': 'setMinter(address)',
            '0xbc67e887': 'setBurnEnabled(bool)',
            '0x8af033fb': 'setTransferEnabled(bool)',
            '0x6a40701c': 'setWhitelistEnabled(bool)',
            
            # Fee Management
            '0xa6f95726': 'setTreasuryFee(uint256)',
            '0xf6d36ccb': 'setMaxTransferAmount(uint256)',
            '0x5c11d795': 'setFeeExempt(address,bool)',
            
            # Bridge/Cross-chain
            '0xed9999ca': 'bridgeTokens(address,uint256,uint256)',
            '0xb88a802f': 'processBridgeRequest(bytes32)',
            '0x35e4365f': 'claimBridgedTokens(bytes32)',
            
            # Oracle/Price
            '0xec32ee72': 'setPriceOracle(address)',
            '0xdfcbb4a0': 'updatePrice(uint256)',
            '0xdd78d136': 'getLatestPrice()',
            
            # Vault/Strategy
            '0xb5a4618e': 'setVaultParameters(uint256,uint256)',
            '0x2851ff81': 'setStrategy(address,bool)',
            '0xd0febe4c': 'migrateStrategy(address)',
            
            # Lending
            '0x310f2668': 'borrow(uint256,uint256)',
            '0x44ddc37b': 'repay(uint256)',
            '0xb6ace2fd': 'liquidate(address)',
            
            # Utility
            '0x598647f8': 'pause()',
            '0x8c4e7e2a': 'unpause()',
            '0x1071a290': 'setEmergencyMode(bool)',
            '0x51ed8288': 'recoverTokens(address)',
            
            # Specific Protocol Functions
            '0x5334e8b4': 'setRewardDistribution(address[])',
            '0x82c07d5d': 'setRewardWeights(uint256[])',
            '0xcf4df16f': 'setMaxTotalSupply(uint256)',
            '0x0df45469': 'setTransferEnabled(bool)',
            '0x2fb44d15': 'setBaseURI(string)',
            '0x13f78a49': 'setMinter(address)',
            '0xbaa2abde': 'setBurnEnabled(bool)',
            '0xaa7415f5': 'setTreasuryFee(uint256)',
            '0xd7bb99ba': 'setMaxTransferAmount(uint256)',
            
            # Additional Functions
            '0x3ce33bff': 'setWhitelistEnabled(bool)',
            '0x2e4dbe8f': 'setFeeExempt(address,bool)',
            '0xf75e0384': 'bridgeTokens(address,uint256)',
            '0xcfc93274': 'processBridgeRequest(bytes32)',
            '0xfa021524': 'claimBridgedTokens(bytes32)',
            '0xc7a50eba': 'setPriceOracle(address)',
            '0x095c9d8e': 'updatePrice(uint256)',
            '0xf2c298be': 'getLatestPrice()',
            '0x87260a7c': 'setVaultParameters(uint256)',
            
            # System Functions
            '0x0000000d': 'initialize()',
            '0x47175878': 'setController(address)',
            '0xad823822': 'setAdmin(address)',
            '0xc132e27f': 'setOperator(address)',
            '0x643654d5': 'setGuardian(address)',
            '0xb969b4bf': 'setTimelock(address)',
            '0xb5d011c3': 'setGovernance(address)',
            '0xbb4cee01': 'setPendingGovernance(address)',
            '0xc9b298f1': 'acceptGovernance()',
            
            # Additional Protocol Functions
            '0x0f93d622': 'setRewardToken(address)',
            '0x821ac41b': 'setRewardRate(uint256)',
            '0xd365a377': 'setRewardsDuration(uint256)',
            '0x5590febd': 'setRewardDistributor(address)',
            '0xc83980dd': 'setStakingToken(address)',
            '0x9a98f01b': 'setMinStakeTime(uint256)',
            '0x39bf70d1': 'setMaxStakeAmount(uint256)',
            '0x8cd6944a': 'setMinStakeAmount(uint256)',
            '0xbeebc5da': 'setStakingFee(uint256)',
            '0xb48951e4': 'setUnstakingFee(uint256)',
            '0x6af8e7eb': 'setPerformanceFee(uint256)',
            '0x24904cb3': 'setManagementFee(uint256)',
            '0x5c833bfd': 'setWithdrawalFee(uint256)',
            '0x79433d8b': 'setDepositLimit(uint256)',
            '0xac7b22dc': 'setInvestmentStrategy(address)',
            '0x0df96f55': 'setFeeBeneficiary(address)',
            '0xb9d2d7ed': 'setEmergencyReturn(address)'
        }

    def get_method_id(self, signature: str) -> str:
        """Calcula el method ID para una signature dada."""
        k = keccak(text=signature)
        return '0x' + k.hex()[:8]

    def is_text(self, hex_str: str) -> Optional[str]:
        """Verifica si el hex string es texto ASCII legible."""
        try:
            if hex_str.startswith('0x'):
                hex_str = hex_str[2:]
            text = bytes.fromhex(hex_str).decode('ascii')
            if all(32 <= ord(c) <= 126 or c in ['\n', '\t', '\r'] for c in text):
                return f'WORD: "{text}"'
            return None
        except (UnicodeDecodeError, binascii.Error):
            return None

    def get_function_signature_from_4byte(self, method_id: str) -> str:
        """Consulta 4byte.directory para obtener la firma de una función a partir de un method ID."""
        url = f"https://www.4byte.directory/api/v1/signatures/?hex_signature={method_id}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get('results')
            if results:
                return results[0]['text_signature']
        return "No se pudo decodificar"

    def search_function_by_methodid(self, method_id: str) -> Optional[str]:
        """Busca el method ID en todos los protocolos y devuelve la función correspondiente."""
        protocols = {
            # Ejemplo de estructura de datos para protocolos
            "ACROSS": ACROSS_FUNCTIONS,
            "ALLBRIDGE": ALLBRIDGE_FUNCTIONS,
            # ... (resto del diccionario de protocolos como en el script original)
        }
        
        for protocol_name, protocol_data in protocols.items():
            for version, categories in protocol_data.items():
                for category, functions in categories.items():
                    for function_name, details in functions.items():
                        if isinstance(details, dict) and details.get('method') == method_id:
                            return function_name
        return None

    def try_decode(self, method_id: str) -> Tuple[str, str]:
        """
        Intenta decodificar un method ID.
        Retorna una tupla (tipo, resultado)
        """
        # Normalizar method_id
        method_id = method_id.lower()
        if not method_id.startswith('0x'):
            method_id = '0x' + method_id
            
        # Buscar en signatures conocidas
        if method_id in self.known_signatures:
            return ('FUNCTION', self.known_signatures[method_id])
            
        # Buscar en palabras conocidas
        if method_id in self.known_words:
            return ('WORD', self.known_words[method_id])
        
        # Intentar decodificar usando 4byte.directory
        signature = self.get_function_signature_from_4byte(method_id)
        if signature != "No se pudo decodificar":
            return ('FUNCTION', signature)
        
        # Buscar en protocolos
        function_name = self.search_function_by_methodid(method_id)
        if function_name:
            return ('FUNCTION', function_name)
            
        # Si no se encuentra en ninguna lista, se considera desconocido
        return ('UNKNOWN', f'No se encontró coincidencia para el method ID: {method_id}')

    def decode_multiple(self, method_ids: List[str]) -> Dict[str, str]:
        """
        Decodifica múltiples method IDs y retorna un diccionario
        """
        results = {}
        for method_id in method_ids:
            tipo, resultado = self.try_decode(method_id)
            results[method_id] = resultado
        return results

def main():
    decoder = MethodIdDecoder()
    
    print("\nBienvenido al decodificador de Method IDs")
    print("Introduce los Method IDs separados por comas (ejemplo: 0xa9059cbb,0x095ea7b3)")
    print("Para salir, escribe 'exit' o 'quit'\n")
    
    while True:
        user_input = input("Introduce Method IDs: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("¡Hasta luego!")
            break
            
        if not user_input:
            continue
            
        method_ids = [mid.strip() for mid in user_input.split(',')]
        
        print("\nDecodificando method IDs...")
        results = decoder.decode_multiple(method_ids)
        
        functions_found = 0
        words_found = 0
        unknown = 0
        
        for method_id, resultado in results.items():
            if "FUNCTION" in resultado:
                print(f"✅ {method_id} => {resultado}")
                functions_found += 1
            elif "WORD" in resultado:
                print(f"📝 {method_id} => {resultado}")
                words_found += 1
            else:
                print(f"❌ {method_id} => {resultado}")
                unknown += 1
                
        total = len(method_ids)
        print(f"\nResumen:")
        print(f"- Funciones encontradas: {functions_found}/{total}")
        print(f"- Palabras encontradas: {words_found}/{total}")
        print(f"- No decodificados: {unknown}/{total}\n")

if __name__ == "__main__":
    main() 