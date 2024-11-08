"""URLs for all supported protocols"""

PROTOCOL_URLS = {
    # Lending Protocols
    'AAVE': 'https://aave.com',
    'COMPOUND': 'https://compound.finance',
    'CREAM': 'https://cream.finance',
    'EULER': 'https://euler.finance',
    'FRAX': 'https://frax.finance',
    'GEIST': 'https://geist.finance',
    'GRANARY': 'https://granary.finance',
    'HUNDRED': 'https://hundred.finance',
    'IRON_BANK': 'https://ib.xyz',
    'MAKER': 'https://makerdao.com',
    'MAPLE': 'https://maple.finance',
    'MORPHO': 'https://morpho.xyz',
    'RADIANT': 'https://radiant.capital',
    'VENUS': 'https://venus.io',

    # DEX Protocols
    'UNISWAP': 'https://uniswap.org',
    'SUSHISWAP': 'https://sushi.com',
    'PANCAKESWAP': 'https://pancakeswap.finance',

    # NFT Marketplaces
    'BLUR': 'https://blur.io',
    'LOOKSRARE': 'https://looksrare.org',
    'MAGIC_EDEN': 'https://magiceden.io',
    'NFTX': 'https://nftx.io',
    'OPENSEA': 'https://opensea.io',
    'RARIBLE': 'https://rarible.com',
    'SUDOSWAP': 'https://sudoswap.xyz',
    'X2Y2': 'https://x2y2.io',

    # Bridge Protocols
    'ACROSS': 'https://across.to',
    'ALLBRIDGE': 'https://allbridge.io',
    'ARBITRUM': 'https://arbitrum.io',
    'CELER': 'https://celer.network',
    'HOP': 'https://hop.exchange',
    'LAYERZERO': 'https://layerzero.network',
    'MULTICHAIN': 'https://multichain.org',
    'OPTIMISM': 'https://optimism.io',
    'ORBITER': 'https://orbiter.finance',
    'POLYGON': 'https://polygon.technology',
    'PORTAL': 'https://portalbridge.com',
    'STARGATE': 'https://stargate.finance',
    'SYMBIOSIS': 'https://symbiosis.finance',
    'WORMHOLE': 'https://wormhole.com',

    # Derivatives Protocols
    'DRIFT': 'https://drift.trade',
    'DYDX': 'https://dydx.exchange',
    'GAINS': 'https://gains.trade',
    'GMX': 'https://gmx.io',
    'HUBBLE': 'https://hubble.exchange',
    'KWENTA': 'https://kwenta.io',
    'LEVEL': 'https://level.finance',
    'MYCELIUM': 'https://mycelium.xyz',
    'PERP': 'https://perp.com',
    'POLYNOMIAL': 'https://polynomial.fi',
    'RIBBON': 'https://ribbon.finance',
    'SYNTHETIX': 'https://synthetix.io',
    'VELA': 'https://vela.exchange',

    # Gaming Protocols
    'AXIE': 'https://axieinfinity.com',
    'BETSWIRL': 'https://betswirl.com',
    'BIGTIME': 'https://bigtime.gg',
    'CRYPTO_UNICORNS': 'https://cryptounicorns.fun',
    'DECENTRAL': 'https://decentral.games',
    'DEFI_KINGDOMS': 'https://defikingdoms.com',
    'EMBER_SWORD': 'https://embersword.com',
    'GALA': 'https://gala.games',
    'GODS_UNCHAINED': 'https://godsunchained.com',
    'ILLUVIUM': 'https://illuvium.io',
    'PEGAXY': 'https://pegaxy.io',
    'ROLLBIT': 'https://rollbit.com',
    'SORARE': 'https://sorare.com',
    'SPLINTERLANDS': 'https://splinterlands.com',
    'STAR_ATLAS': 'https://staratlas.com',
    'STEPN': 'https://stepn.com',
    'THETAN_ARENA': 'https://thetanarena.com',
    'WALLFAIR': 'https://wallfair.io',
    'ZED_RUN': 'https://zed.run',

    # Identity Protocols
    'BRIGHTID': 'https://brightid.org',
    'CIVIC': 'https://civic.com',
    'POLYGONID': 'https://polygon.technology/polygon-id',
    'WORLDCOIN': 'https://worldcoin.org',

    # Infrastructure Protocols
    'ARWEAVE': 'https://arweave.org',
    'FILECOIN': 'https://filecoin.io',
    'IPFS': 'https://ipfs.tech',
    'POCKET': 'https://pokt.network',
    'THE_GRAPH': 'https://thegraph.com',

    # Insurance Protocols
    'INSURACE': 'https://insurace.io',
    'NEXUS_MUTUAL': 'https://nexusmutual.io',
    'UNSLASHED': 'https://unslashed.finance',

    # Launchpad Protocols
    'BULLPERKS': 'https://bullperks.com',
    'GAMEFI': 'https://gamefi.org',
    'GAMESTARTER': 'https://gamestarter.com',

    # MEV Protocols
    'COWSWAP': 'https://cow.fi',
    'EDEN': 'https://eden.network',
    'FLASHBOTS': 'https://flashbots.net',
    'MANIFOLD': 'https://manifoldfinance.com',
    'ROOK': 'https://rook.fi',

    # Oracle Protocols
    'API3': 'https://api3.org',
    'BAND': 'https://bandprotocol.com',
    'CHAINLINK': 'https://chain.link',
    'DIA': 'https://diadata.org',
    'PYTH': 'https://pyth.network',
    'REDSTONE': 'https://redstone.finance',
    'TELLOR': 'https://tellor.io',
    'UMA': 'https://uma.xyz',
    'UMBRELLA': 'https://umb.network',

    # Privacy Protocols
    'AZTEC': 'https://aztec.network',
    'MONERO_BRIDGE': 'https://monero.com',
    'RAILWAY': 'https://railway.xyz',
    'TORNADO': 'https://tornado.cash',
    'ZCASH_BRIDGE': 'https://z.cash',

    # RWA Protocols
    'CENTRIFUGE': 'https://centrifuge.io',
    'GOLDFINCH': 'https://goldfinch.finance',
    'MAPLE': 'https://maple.finance',
    'TRUEFI': 'https://truefi.io',

    # Social Media Protocols
    'FARCASTER': 'https://farcaster.xyz',
    'FRIEND_TECH': 'https://friend.tech',
    'LENS': 'https://lens.xyz',

    # Staking Protocols
    'ANKR': 'https://ankr.com',
    'BINANCE': 'https://binance.com',
    'EIGENLAYER': 'https://eigenlayer.xyz',
    'LIDO': 'https://lido.fi',
    'MANTLE': 'https://mantle.xyz',
    'OETH': 'https://oeth.com',
    'ROCKETPOOL': 'https://rocketpool.net',
    'STADER': 'https://staderlabs.com',
    'STAKESTONE': 'https://stakestone.io',
    'STAKEWISE': 'https://stakewise.io',
    'SWELL': 'https://swellnetwork.io',

    # Yield Farming Protocols
    'ALPACA': 'https://alpacafinance.org',
    'BEEFY': 'https://beefy.finance',
    'CONCENTRATOR': 'https://concentrator.aladdin.club',
    'CONVEX': 'https://convexfinance.com',
    'JONES': 'https://jonesdao.io',
    'PICKLE': 'https://pickle.finance',
    'PIREX': 'https://pirex.io',
    'REDACTED': 'https://redacted.finance',
    'YEARN': 'https://yearn.finance',
    'YIELD_YAK': 'https://yieldyak.com'
}