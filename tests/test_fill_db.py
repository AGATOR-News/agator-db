from agator_db import BaseDB, DBAuth, PubDB, PublicationIN, __version__
import dotenv
from os import environ as env
from uuid import uuid4

dotenv.load_dotenv(dotenv.find_dotenv())

DB_AUTH = DBAuth(
    host=env.get("DB:HOST", "127.0.0.1"),
    port=env.get("DB:HOST", 28015),
    user=env.get("DB:USER", "admin"),
    password=env.get("DB:PASS")
)

PUBLICATIONS = [
    PublicationIN(
        link="https://www.spiegel.de",
        title="DER SPIEGEL",
        description="Deutschlands führende Nachrichtenseite. Alles Wichtige aus Politik, Wirtschaft, Sport, Kultur, Wissenschaft, Technik und mehr.",
        banner="https://www.spiegel.de/public/spon/images/logos/der-spiegel-h60.png",
        icon="https://cdn.prod.www.spiegel.de/public/spon/images/icons/favicon.ico",
        color="#E44524"
    ),
    PublicationIN(
        link="https://www.faz.net",
        title="FAZ.NET",
        description="News, Nachrichten und aktuelle Meldungen aus allen Ressorts. Politik, Wirtschaft, Sport, Feuilleton und Finanzen im Überblick.",
        banner="https://www.faz.net/img/fazlogo_ressort.png",
        icon="https://www.faz.net/favicon.ico",
        color="#E44524"
    ),
    PublicationIN(
        link="https://www.welt.de",
        title="WELT",
        description="Aktuelle Nachrichten von WELT",
        banner="https://www.welt.de/rss-logo.png",
        icon="https://www.welt.net/favicon.ico",
        color="#043B59"
    ),
    PublicationIN(
        link="https://www.bild.de",
        title="BILD",
        description="Aktuelle Nachrichten",
        banner="https://bilder.bild.de/fotos/bild-logo-35166394/Bild/45.bild.png",
        icon="https://www.bild.de/favicon.ico",
        color="#CB0814"
    ),
    PublicationIN(
        link="https://www.n-tv.de",
        title="n-tv.de",
        description="n-tv.de, Nachrichten seriös, schnell und kompetent. Artikel und Videos aus Politik, Wirtschaft, Börse, Sport und aller Welt.",
        banner="https://www.n-tv.de/resources/16663117/adaptive/images/head_logo.png",
        icon="https://www.n-tv.de/favicon.ico",
        color="#D90B2F"
    ),
    PublicationIN(
        link="https://www.focus.de",
        title="FOCUS Online",
        description="FOCUS Online - minutenaktuelle Nachrichten und Service-Informationen.",
        banner="https://p5.focus.de/fol/pics/fol/logo_125x40.png",
        icon="https://www.focus.de/favicon.ico",
        color="#D30918"
    )
    # ,
    # PublicationIN(
    #     link="https://www.focus.de",
    #     title="DIE ZEIT",
    #     description="FOCUS Online - minutenaktuelle Nachrichten und Service-Informationen.",
    #     banner="https://p5.focus.de/fol/pics/fol/logo_125x40.png",
    #     icon="https://www.focus.de/favicon.ico"
    #     color="#1D1D1B"
    # )
]


def test_connection():
    global DB_AUTH
    assert BaseDB(DB_AUTH).status()


def test_pubdb():
    global PUBLICATIONS
    global DB_AUTH
    pubdb = PubDB(DB_AUTH)
    # pub = PublicationIN(
    #     id=str(uuid4()),
    #     title="DER SPIEGEL",
    #     link="https://example.com",
    #     image="https://example.com/image.png",
    #     color="#FF00FF"
    # )

    for pub in PUBLICATIONS:
        pubdb.add_pub(pub)
