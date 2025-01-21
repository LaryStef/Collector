import os
from random import uniform, randint
from string import ascii_letters, digits

from sqlalchemy import create_engine, Engine, MetaData
from sqlalchemy.orm import Session

from src.database.models import CryptoCourse, CryptoCurrency, Fiat


SQLALCHEMY_DATABASE_URI: str = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/{os.getenv('POSTGRES_NAME')}"  # noqa: E501

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata: MetaData = MetaData()


def _add_fiat_currencies() -> None:
    session.add(
        Fiat(
            iso="USD",
            name="United States Dollar",
            description="Dollar description",
            volume=1_000_000.37
        )
    )


def _add_cryptocurrencies() -> None:
    # session.add(
    #     CryptoCurrency(
    #         ticker="BTC",
    #         name="Bitcoin",
    #         description="""
    #             <h3>Overview</h3>
    #             <p>
    #                 Bitcoin (BTC) is the world's first globally viable
    #                 cryptocurrency built with blockchain technology. Outlined
    #                 in 2008 by an anonymous developer under the pseudonym
    #                 Satoshi Nakamoto, Bitcoin remains the most widely accepted
    #                 and traded cryptocurrency today. Nakamoto conceived
    #                 Bitcoin as a peer-to-peer electronic cash system that had
    #                 no need for a central authority or single administrator. A
    #                 global team of developers continues to maintain and work
    #                 on the improvement of the Bitcoin protocol.
    #             </p>
    #             <h3>Who created Bitcoin?</h3>
    #             <p>
    #                 An unknown programmer published the Bitcoin white paper
    #                 under the pseudonym "Satoshi Nakamoto" in 2008. Satoshi
    #                 Nakamoto may be an individual or a group of people.
    #                 Despite the widespread use and popularity of Bitcoin, the
    #                 true identity of Satoshi Nakamoto remains a mystery. Over
    #                 the years, many people have claimed to be the real Satoshi
    #                 Nakamoto, but none of them have been able to provide
    #                 definitive evidence to support their claims. Whoever
    #                 Nakamoto is or was, they went to great lengths to remain
    #                 anonymous. This mystery has helped increase the appeal of
    #                 bitcoin as a global currency and fascination surrounding
    #                 the origins of Bitcoin. Those closely related to
    #                 cryptography around the time of Bitcoin's conception
    #                 remain the most prominent suspects. These include computer
    #                 programmers Nick Szabo and the late Hal Finney. Miners
    #                 created the Bitcoin genesis block on January 3, 2009.
    #             </p>""",
    #         volume=28_388_811_901.29
    #     )
    # )
    # session.add(
    #     CryptoCurrency(
    #         ticker="ETH",
    #         name="Ethereum",
    #         description="""
    #             <h3>Overview</h3>
    #             <p>
    #                 Ethereum is a decentralized, open-source blockchain
    #                 platform established in 2013. Unlike Bitcoin, which
    #                 focuses mainly on digital payments, Ethereum empowers
    #                 developers to create decentralized applications (dApps)
    #                 for diverse purposes, such as finance, gaming, and supply
    #                 chain management. Smart contracts, which are
    #                 self-executing programs containing the terms of agreements
    #                 in code, underpin these applications. Ethereum was the
    #                 first platform to introduce smart contract functionality.
    #                 It operates using Ether (ETH), its native cryptocurrency,
    #                 necessary for executing smart contracts and transactions
    #                 on the network. Ether, the second largest cryptocurrency
    #                 by market capitalization, can be traded on exchanges and
    #                 serves as a store of value, akin to Bitcoin. Users of the
    #                 Ethereum blockchain pay gas fees, denominated in ETH, for
    #                 transaction validation.
    #             </p>
    #             <h3>Creator</h3>
    #             <p>
    #                 Vitalik Buterin, a Russian-Canadian programmer, created
    #                 Ethereum. At just 19, he recognized the limitations of
    #                 centralized systems after a frustrating change to his
    #                 favorite World of Warcraft character. This inspired his
    #                 vision of a decentralized digital network enabling the
    #                 development of applications interacting with digital
    #                 currencies. Before Ethereum, Buterin co-founded Bitcoin
    #                 Magazine, one of the earliest Bitcoin publications. He
    #                 published the Ethereum white paper in 2014 and launched
    #                 the project in 2015, mining the genesis block on July 30,
    #                 2015. Buterin's vision attracted several passionate
    #                 co-founders, including Gavin Wood, Joseph Lubin, Anthony
    #                 Di Iorio, and Charles Hoskinson. Together, they founded
    #                 the Ethereum Foundation, a non-profit organization aimed
    #                 at supporting the platform's development and ecosystem.
    #                 Notably, only Buterin remains with the project from the
    #                 original co-founders.
    #             </p>
    #             <a href="https://www.youtube.com/shorts/LtrgP17dw_E">
    #                 His best video ever.
    #             </a>""",
    #         volume=7_865_323_997.26
    #     )
    # )
    # session.add(
    #     CryptoCurrency(
    #         ticker="USDT",
    #         name="Tether",
    #         description="""
    #             <h3>Overview</h3>
    #             <p>
    #                 Tether (USDT) is a stablecoin, which is a type of
    #                 cryptocurrency that actively works to keep its valuation
    #                 stable through market mechanisms. It's used by investors
    #                 who want to hedge against the inherent volatility of their
    #                 cryptocurrency investments while still keeping value
    #                 inside the crypto market, ready to be used without hassle.
    #                 Tether is a fiat-collateralized stablecoin, which is a
    #                 type of stablecoin that is backed by a fiat currency like
    #                 USD, CAD, AUD, or even Yen (JPY). Tether was created to
    #                 bridge the gaps between fiat currencies and blockchain
    #                 assets while offering transparency, stability, and low
    #                 fees for USDT users. Tether is pegged against the U.S.
    #                 Dollar at a 1:1 ratio. There is no guarantee from Tether
    #                 Ltd. for any right of redemption or exchange of Tether to
    #                 USD. USDT cannot be exchanged directly for USD through the
    #                 Tether company.
    #             </p>
    #             <h3>How does Tether work?</h3>
    #             <p>
    #                 Each Tether issued is backed by one US dollar worth
    #                 of assets. All Tether was initially issued on the Bitcoin
    #                 blockchain via the Omni Layer protocol, but can now be
    #                 issued on any chain that Tether currently supports. Once a
    #                 tether (a single unit of USDT) has been issued, it can be
    #                 used the same as any other currency or token on the chain
    #                 that it has been issued on. Tether currently supports the
    #                 Bitcoin, Ethereum, EOS, Tron, Algorand, and OMG Network
    #                 blockchains. Tether uses Proof Of Reserves, which means
    #                 that at any time their reserves will be equal to or
    #                 greater than the number of Tether in circulation. This can
    #                 be verified via their website.
    #             </p>""",
    #         volume=42_177_103_848.39
    #     )
    # )
    session.add(
        CryptoCurrency(
            ticker="XRP",
            name="Ripple",
            description="""
                <h3>Overview</h3>
                <p>
                    The XRP Ledger, or XRPL is an open-source distributed
                    ledger powered by a network of peer-to-peer servers. XRPis
                    the digital asset native to the network, which is designed
                    to function as a bridge currency. The goal of the network
                    is to “power innovative technology across the payments
                    space” and enable “seamless, real-time, final, and
                    cost-effective” global payments, as stated on the project
                    website.
                </p>
                <h3>Uses for Ripple</h3>
                <p>
                    The network seeks to achieveimproved currency utility over
                    legacy payment channels, asXRP can be used by a wide range
                    of third parties that seekto augment their value through
                    decentralized means. TheXRP Ledger operates on the basis of
                    validator nodes thatcollect the set of all candidate
                    transactions and reachconsensus on transactions that
                    occurred before the cut-offtime for any given ledger. Once
                    the set of transactions isagreed upon, they are executed in
                    a deterministic order,subject to the objective rules of the
                    network, as imposedby every server independently. The
                    ledger reachesconsensus on all outstanding transactions
                    every 3-5seconds.
                </p>
                <h3>How does Ripple Work?</h3>
                <p>
                    The ledger features a decentralized exchange that allows
                    the trading of IOUs and XRP. It also features some smart
                    contract functionality and supports the network-agnostic
                    Interledger Protocol. XRPL was released in 2012 and has
                    since been maintained by community participants, including
                    Ripple, which holds a large amount of XRP, though its
                    holdings are largely locked and purpose-bound.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="ADA",
            name="Cardano",
            description="""
                <h3>Overview</h3>
                <p>
                    Cardano is a public blockchain platform and smart contract
                    development platform that is similar to Ethereum. Founded
                    in 2015, Cardano touts itself as the first blockchain
                    platform in the crypto industry to be founded on
                    peer-reviewed research. Its blockchain is powered by
                    Ouroboros, a proof-of-stake protocol that its proponents
                    claim has improved upon the foundations of other consensus
                    mechanisms. ADA is the multi-purpose native token of
                    Cardano and powers all transactions on the network. It
                    also provides rewards to network validators (also called
                    stakers). These users help secure the network and verify
                    new transactions entering the Cardano blockchain. The
                    Cardano blockchain provides a secure way for users to
                    store and send ADA over the network. This factor includes
                    native tokens created on top of the Cardano blockchain.
                    Additionally, it provides functionality for developing
                    decentralized applications.
                </p>
                <h3>How does Cardano work?</h3>
                <p>
                    The native coin of the Cardano blockchain is ADA, which
                    has a maximum supply of 45 billion coins. Cardano's
                    tokenomics include a built-in treasury system and a
                    mechanism for funding future development through a
                    decentralized governance system. Validators process
                    transactions on the Cardano blockchain. To do this, they
                    must first lock away an amount of native tokens in a
                    staking smart contract. Holders use specific crypto wallets
                    to store ADA. These can be either hardware wallet or
                    software-based wallets. Cardano allows users to stake
                    Cardano ADA coins to earn rewards and participate in the
                    management of its blockchain network. Soon, holders of ADA
                    will be able to vote on changes made within the protocol,
                    giving them direct control over its features and operation.
                    Cryptocurrencies that allow holders to vote on the future
                    development of the blockchain protocol they are associated
                    with are known as governance tokens. Governance features
                    are expected to go live once the Voltaire phase of
                    Cardano's development begins.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="AVAX",
            name="Avalanche",
            description="""
                <h3>Overview</h3>
                <p>
                    Avalanche is a blockchain platform that aims to address the
                    blockchain trilemma of scalability, security and
                    decentralization thanks to its unique Proof of Stake (PoS)
                    mechanism. Like Ethereum, Avalanche supports smart
                    contracts to run decentralized applications (dApps) on its
                    network. Since Avalanche's smart contracts are written in
                    the Solidity language also used by Ethereum, it aims to
                    create greater blockchain interoperably by integrating a
                    number of decentralized finance (DeFi) ecosystems,
                    including well-established projects like Aave and Curve.
                    AVAX, the native token of the Avalanche platform, is used
                    to power transactions in its ecosystem. AVAX serves as the
                    means to distribute system rewards, participate in
                    governance and facilitate transactions on the network by
                    paying fees.
                </p>
                <h3>Who created Avalanche?</h3>
                <p>
                    In May 2018, Team Rocket — a pseudonymous group of software
                    developers — published an article that detailed the basis
                    for the Avalanche protocol. Soon afterwards, Emin Gün Sirer
                    founded AVA Labs with the goal of creating and developing
                    the Avalanche blockchain. Sirer is a professor of computer
                    science at Cornell University and was a notable member of
                    the Initiative for Cryptocurrencies and Contracts (IC3). In
                    2003, he also created Karma, a Proof of Work virtual
                    currency for peer-to-peer file sharing systems that
                    predated Bitcoin. Avalanche raised $42 million through an
                    ICO in July 2020 and has continued to draw big investments
                    since. In July 2021, the Avalanche Foundation held a token
                    sale raising $230 million, with participants including
                    large VC companies such as Polychain and Three Arrows
                    Capital.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="DOGE",
            name="Dogecoin",
            description="""
                <h3>Overview</h3>
                <p>
                    Dogecoin is a decentralized, peer-to-peer cryptocurrency
                    centering around the "Doge" meme, which serves as its
                    mascot. Built using blockchain technology, Dogecoin (DOGE)
                    was once a popular tipping cryptocurrency and fundraising
                    mechanism for multiple charitable causes. Dogecoin features
                    the likeness of the Shiba Inu dog popularized in the "Doge"
                    meme. The cryptocurrency first appeared as a light-hearted
                    marketing experiment in 2013. DOGE quickly gained a massive
                    audience in the crypto market and now boasts one of the
                    largest market caps in the industry. Doge is pleased. The
                    success and virality of Dogecoin spurred the creation of
                    other Shiba Inu-themed projects thereby launching an
                    entirely new crypto industry sector of "meme coins." Shiba
                    Inu Coin (SHIB) is a leading example of a popular spin-off
                    with a similarly large market capitalization.
                </p>
                <h3>How does Dogecoin work?</h3>
                <p>
                    Dogecoin operates using a proof-of-work-based (PoW)
                    consensus mechanism and has an inflationary supply of
                    coins. This fact means that there is no cap on the maximum
                    supply of coins that the protocol can create. Initially,
                    Palmer and Markus agreed to set the max supply at 100
                    billion coins. However, the co-founders later removed this
                    feature to keep prices low and encourage users to send
                    tokens to one another. Dogecoin's inflationary nature means
                    its native digital asset DOGE, is not typically recommended
                    as a reliable store of value. As of April 2023, the current
                    supply of Dogecoins is over 130 billion DOGE, with a
                    maximum supply of 10,000 DOGE per block. The balance of
                    supply is constantly changing as new coins are minted
                    through mining. This steady influx of fixed block rewards
                    means the inflation rate technically decreases over
                    time. Dogecoin's inflationary supply allows for a more
                    flexible and adaptable ecosystem that can respond to market
                    demands. Palmer and Markus created Dogecoin as a fork of
                    Lucky Coin, an open-source proof-of-work project forked
                    from Litecoin. Because of this, Dogecoin uses the Scrypt
                    mining algorithm instead of the SHA-256 mining algorithm
                    used by Bitcoin.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="SOL",
            name="Solana",
            description="""
                <h3>Overview</h3>
                <p>
                    Solana is a leading blockchain-based platform that provides
                    smart contract functionality for developers to create their
                    own decentralized applications. Blockchains like Solana
                    allow a network of users to track information in a
                    peer-to-peer way. Solana is not reliant on a single
                    intermediary, like a person or a company, to verify
                    information stored on its blockchain. Instead, this
                    information is collectively shared and updated across the
                    blockchain network itself. Smart contracts, like those used
                    on Solana, allow individuals to define and automatically
                    execute actions based on pre-defined conditions. Smart
                    contracts are the building blocks of much of the
                    functionality on the Solana blockchain. Leveraging these
                    smart contracts, blockchain developers can create their own
                    unique decentralized applications (dApps), crypto tokens,
                    and other services on the Solana blockchain for others to
                    use.
                </p>
                <h3>What makes Solana unique?</h3>
                <p>
                    Solana has differentiated itself from other blockchain
                    networks by offering a platform that has faster transaction
                    speeds and lower fees than many other blockchains. Although
                    Bitcoin and Ethereum are still the projects with the
                    largest market capitalizations in the cryptocurrency
                    market, Solana's focus on increasing speed and lowering
                    fees has helped it rise within the blockchain space.
                    Solana's ability to process a comparatively high number of
                    transactions per second with lower transaction fees has
                    helped it become a popular choice for decentralized finance
                    (DeFi) and non-fungible token (NFT) projects. In contrast
                    to many newer blockchains that still developing an
                    ecosystem of apps and projects, Solana offers a vibrant
                    community of different products and services. This ability
                    to integrate with and build alongside projects with
                    existing userbases has made Solana an attractive blockchain
                    for many new crypto project developers.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="TON",
            name="Toncoin",
            description="""
                <h3>Overview</h3>
                <p>
                    Toncoin (TON) is a decentralized cryptocurrency that powers
                    the Ton blockchain, which was designed to be fast,
                    scalable, and secure. Originally developed as part of the
                    Telegram Open Network (TON) by the team behind the
                    messaging app Telegram, TON aims to provide a platform for
                    decentralized applications (dApps), fast payments, and
                    secure data storage. The blockchain features a
                    multi-layered structure and sharding technology, allowing
                    it to handle millions of transactions per second. Toncoin
                    is used for transaction fees, staking, and governance
                    within the network. With its focus on low-cost, high-speed
                    transactions and the ability to support a wide range of
                    decentralized services, Toncoin has gained popularity in
                    the cryptocurrency community. After the project's split
                    from Telegram, the TON Foundation continued its
                    development, ensuring the blockchain remains
                    community-driven and open-source.
                </p>
                <h3>Who created Toncoin?</h3>
                <p>
                    Toncoin was initially created by the team behind Telegram,
                    including Pavel and Nikolai Durov, the founders of the
                    messaging app. The project was launched in 2018 under the
                    name Telegram Open Network (TON) and was designed to
                    integrate blockchain technology with Telegram's vast user
                    base. However, after legal challenges from the U.S.
                    Securities and Exchange Commission (SEC), Telegram halted
                    its involvement with the project in 2020. Despite this, the
                    community continued to develop the project independently,
                    leading to the rebranding of TON as Toncoin. The Toncoin
                    blockchain is now maintained by the TON Foundation, a
                    decentralized organization that oversees the network's
                    growth and development, ensuring that it remains
                    open-source and community-driven.
                </p>""",
            volume=28_388_811_901.29
        )
    )
    session.add(
        CryptoCurrency(
            ticker="TRX",
            name="Tron",
            description="""
                <h3>Overview</h3>
                <p>
                    Launched at the height of 2017's crypto mania, Tron has
                    since galvanized a global group of investors and developers
                    around a vision for how cryptocurrencies could reshape the
                    internet. But if the goal of using blockchains to create a
                    distributed web was common among projects launching at the
                    time, Tron distinguished its offering with communications
                    that resonated, even as criticisms about its technology
                    persisted. For instance, Tron was rare among
                    cryptocurrencies launching in 2017 in that it did not seek
                    to advertise any advances in cryptography or network
                    design. Rather, the basic building blocks of Tron -
                    decentralized applications, smart contracts, tokens,
                    delegated proof-of-stake consensus - were pioneered by
                    other projects prior to its launch. Tron even went so far
                    as to make components of its technology compatible with
                    Ethereum (ETH) (which sparked accusations it went too far
                    in borrowing its ideas).Tron would further differentiate
                    with an Asia-focused go-to-market strategy that heavily
                    relied on publicizing its creator Justin Sun and
                    translating its technical documents into a wider variety of
                    languages than generally targeted by cryptocurrency
                    projects.
                </p>
                <h3>Who created Tron?</h3>
                <p>
                    Tron was created by entrepreneur Sun Yuchen (Justin Sun), a
                    two-time recipient of Forbes' “30-Under-30” award in Asia,
                    in early 2017. An established presence in China, Sun had
                    earlier founded the audio content application Peiwo and
                    served in 2015 as a representative for Ripple, the
                    for-profit company that stewards the XRP cryptocurrency,
                    before founding the Tron Foundation that year. Sun's
                    business background succeeded in attracting early interest
                    from investors including Clash of Kings founder Tang Binsen
                    and CEO of bike sharing startup OFO Dai Wei, among others.
                    These supporters, in turn, boosted visibility of the
                    project's September ICO, which raised millions in
                    cryptocurrency from the public using a token on the
                    ethereum blockchain. A second version of the white paper
                    further outlining Tron's technology was released in 2018.
                </p>""",
            volume=28_388_811_901.29
        )
    )


def _add_test_prices() -> None:
    def _generate_id(length: int) -> str:
        symbols: str = ascii_letters + digits
        _id: str = ""

        for _ in range(length):
            _id += symbols[randint(0, 61)]
        return _id

    def _push_day_course(min_: float, max_: float, ticker: str):
        for hour in range(24):
            session.add(
                CryptoCourse(
                    ID=_generate_id(16),
                    ticker=ticker,
                    type_="hour",
                    number=hour,
                    price=round(uniform(min_, max_), ndigits=2)
                )
            )

    def _push_month_course(min_: float, max_: float, ticker: str):
        for day in range(1, 32):
            session.add(
                CryptoCourse(
                    ID=_generate_id(16),
                    ticker=ticker,
                    type_="day",
                    number=day,
                    price=round(uniform(min_, max_), ndigits=2)
                )
            )

    def _push_year_course(min_: float, max_: float, ticker: str):
        for month in range(1, 13):
            session.add(
                CryptoCourse(
                    ID=_generate_id(16),
                    ticker=ticker,
                    type_="month",
                    number=month*2,
                    price=round(uniform(min_, max_), ndigits=2)
                )
            )
            session.add(
                CryptoCourse(
                    ID=_generate_id(16),
                    ticker=ticker,
                    type_="month",
                    number=month*2-1,
                    price=round(uniform(min_, max_), ndigits=2)
                )
            )

    # _push_day_course(0.985, 1.015, "USDT")
    # _push_month_course(0.985, 1.015, "USDT")
    # _push_year_course(0.985, 1.015, "USDT")

    # _push_day_course(2373.0, 2963.0, "ETH")
    # _push_month_course(2173.0, 3263.0, "ETH")
    # _push_year_course(1973.0, 3463.0, "ETH")

    # _push_day_course(38928.0, 82931.0, "BTC")
    # _push_month_course(33928.0, 89931.0, "BTC")
    # _push_year_course(27928.0, 101931.0, "BTC")

    _push_day_course(2.56, 3.42, "XRP")
    _push_month_course(2.56, 3.42, "XRP")
    _push_year_course(2.56, 3.42, "XRP")

    _push_day_course(0.7, 1.41, "ADA")
    _push_month_course(0.7, 1.41, "ADA")
    _push_year_course(0.7, 1.41, "ADA")

    _push_day_course(21.0, 63.0, "AVAX")
    _push_month_course(21.0, 63.0, "AVAX")
    _push_year_course(21.0, 63.0, "AVAX")

    _push_day_course(0.08, 0.5, "DOGE")
    _push_month_course(0.08, 0.5, "DOGE")
    _push_year_course(0.08, 0.5, "DOGE")

    _push_day_course(142.0, 264.0, "SOL")
    _push_month_course(142.0, 264.0, "SOL")
    _push_year_course(142.0, 264.0, "SOL")

    _push_day_course(4.2, 8.1, "TON")
    _push_month_course(4.2, 8.1, "TON")
    _push_year_course(4.2, 8.1, "TON")

    _push_day_course(0.18, 0.45, "TRX")
    _push_month_course(0.18, 0.45, "TRX")
    _push_year_course(0.18, 0.45, "TRX")


with Session(engine) as session:
    metadata.create_all(bind=engine)

    # _add_fiat_currencies()
    _add_cryptocurrencies()
    _add_test_prices()

    session.commit()
    print("Data pushed successfully.")
