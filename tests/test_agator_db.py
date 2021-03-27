from agator_db import BaseDB, DBAuth, PubDB, Publication, __version__
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


def test_version():
    assert __version__ == '0.1.0'


def test_connection():
    global DB_AUTH
    assert BaseDB(DB_AUTH).status()


def test_pubdb():
    global DB_AUTH
    pubdb = PubDB(DB_AUTH)

    pub = Publication(
        id=str(uuid4()),
        title="Test Publication",
        description="A Test Publication",
        link="https://example.com",
        banner="https://www.welt.de/rss-logo.png",
        icon="https://www.welt.net/favicon.ico",
        color="#FF00FF"
    )
    pubdb.add_pub(pub)
