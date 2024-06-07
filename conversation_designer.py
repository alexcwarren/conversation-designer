import random
from pydantic import BaseModel
from collections import Enum


class LOCATION_NAME(Enum):
    SHIRE = "The Shire"
    RIVENDELL = "Rivendell"
    MORIA = "Moria"
    LOTHLORIEN = "Lothlorien"
    FANGORN = "Fangorn"
    ROHAN = "Rohan"
    GONDOR = "Gondor"
    MORDOR = "Mordor"
    DALE = "Dale"
    ISENGARD = "Isengard"


class Location(BaseModel):
    name: LOCATION_NAME
    affiliates: list[LOCATION_NAME]


class TOPIC(Enum):
    BLACK_RIDERS = "Black Riders"
    GANDALF = "Gandalf"
    ELVES = "Elves"
    ORCS = "Orcs"
    SAURON = "Sauron"


class ALIGNMENT(Enum):
    LAWFUL_GOOD = "Lawful Good"
    LAWFUL_NEUTRAL = "Lawful Neutral"
    LAWFUL_EVIL = "Lawful Evil"
    NEUTRAL_GOOD = "Neutral Good"
    TRUE_NEUTRAL = "True Neutral"
    NEUTRAL_EVIL = "Neutral Evil"
    CHAOTIC_GOOD = "Chaotic Good"
    CHAOTIC_NEUTRAL = "Chaotic Neutral"
    CHAOTIC_EVIL = "Chaotic Evil"


class GameData:
    NPC_NAMES = [
        "Elrandir",
        "Thalindir",
        "Galadorn",
        "Finreth",
        "Borlas",
        "Nimrodel",
        "Thrainor",
        "Celendil",
        "Eldamir",
        "Mithrand",
        "Anoriel",
        "Haldor",
        "Lindir",
        "Maethor",
        "Rhovanor",
        "Silvanis",
        "Galdor",
        "Miriel",
        "Orophin",
        "Tauriel",
        "Ecthelion",
        "Aldarion",
        "Finduilas",
        "Glorfindel",
        "Hithlain",
        "Lothariel",
        "Morwen",
        "Thalion",
        "Voronwe",
        "Yavanna"
    ]

    LOCATION_NAMES = [name.value for name in LOCATION_NAME]

    LOCATION_AFFILIATES = {
        LOCATION_NAME.SHIRE: [LOCATION_NAME.RIVENDELL],
        LOCATION_NAME.RIVENDELL: LOCATION_NAMES,
        LOCATION_NAME.MORIA: [LOCATION_NAME.MORDOR],
        LOCATION_NAME.LOTHLORIEN: LOCATION_NAMES,
        LOCATION_NAME.FANGORN: [],
        LOCATION_NAME.ROHAN: [
            LOCATION_NAME.FANGORN,
            LOCATION_NAME.GONDOR,
            LOCATION_NAME.ISENGARD,
            LOCATION_NAME.MORDOR
        ],
        LOCATION_NAME.GONDOR: [
            LOCATION_NAME.DALE,
            LOCATION_NAME.ISENGARD,
            LOCATION_NAME.LOTHLORIEN,
            LOCATION_NAME.LOTHLORIEN,
            LOCATION_NAME.MORDOR,
            LOCATION_NAME.RIVENDELL,
            LOCATION_NAME.ROHAN
        ],
        LOCATION_NAME.MORDOR: LOCATION_NAMES,
        LOCATION_NAME.DALE: [],
        LOCATION_NAME.ISENGARD: LOCATION_NAMES,
    }

    KNOWN_TOPICS = {
        LOCATION_NAME.SHIRE: [TOPIC.BLACK_RIDERS, TOPIC.ELVES, TOPIC.GANDALF],
        LOCATION_NAME.RIVENDELL: [],
        LOCATION_NAME.MORIA: [],
        LOCATION_NAME.LOTHLORIEN: [],
        LOCATION_NAME.FANGORN: [],
        LOCATION_NAME.ROHAN: [],
        LOCATION_NAME.GONDOR: [],
        LOCATION_NAME.MORDOR: [],
        LOCATION_NAME.DALE: [],
        LOCATION_NAME.ISENGARD: [],
    }

    @classmethod
    def get_random_name(cls) -> str:
        return random.choice(cls.NPC_NAMES)

    @classmethod
    def get_random_location(cls):
        location_name = random.choice(cls.LOCATION_NAMES)
        location_affiliates = cls.LOCATION_AFFILIATES[location_name]
        return Location(location_name, location_affiliates)

    @classmethod
    def get_known_topics(cls, location: Location):
        return cls.KNOWN_TOPICS[location.name]


class NPC:
    def __init__(self):
        self.name: str = GameData.get_random_name()
        self.home: Location = GameData.get_random_location()
        self.known_topics: list[TOPIC] = GameData.get_known_topics(self.home)
        self.description: str = GameData.get_random_NPC_description()
        self.alignment: ALIGNMENT = GameData.get_random_alignment()
        self.ideals: tuple[str] = GameData.get_random_ideals(self.alignment)


def build_NPC():
    pass


def build_passages(npc: NPC):
    pass


def output_twee_code(passages: dict):
    pass


if __name__ == "__main__":
    npc = build_NPC()
    passages = build_passages(npc)
    output_twee_code(passages)
