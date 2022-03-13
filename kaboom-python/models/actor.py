from dataclasses import dataclass
from typing import Optional

@dataclass
class VoiceActor:
    name: Optional[str]
    image: Optional[str]
    date_of_birth: Optional[str]
    date_of_death: Optional[str]
    age: Optional[int]
    biography: Optional[str]
    date_of_created: Optional[str]