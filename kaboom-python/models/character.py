from dataclasses import dataclass
from typing import Optional
from .actor import VoiceActor
from .location import Location
from .team import Team

@dataclass
class Character:
    name: Optional[str]
    alias: Optional[str]
    voice_actors: Optional[list[VoiceActor]]
    image: Optional[str]
    biography: Optional[str]
    teams: Optional[list[Team]]
    status: Optional[str]
    alignment: Optional[str]
    location_of_operation: Optional[list[Location]]
    intelligence: Optional[int]
    strength: Optional[int]
    speed: Optional[int]
    durability: Optional[int]
    power: Optional[int]
    combat: Optional[int]
    date_created: Optional[str]