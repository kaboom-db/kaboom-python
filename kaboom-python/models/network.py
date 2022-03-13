from dataclasses import dataclass
from typing import Optional

@dataclass
class Network:
    id: Optional[int]
    name: Optional[str]
    website: Optional[str]
    logo: Optional[str]
    date_created: Optional[str]