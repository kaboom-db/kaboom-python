from dataclasses import dataclass
from typing import Optional

@dataclass
class Team:
    name: Optional[str]
    tagline: Optional[str]
    disbanded: Optional[int]
    history: Optional[str]
    logo: Optional[str]
    date_created: Optional[str]