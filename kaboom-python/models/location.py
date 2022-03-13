from dataclasses import dataclass
from typing import Optional

@dataclass
class Location:
    city: Optional[str]
    nation: Optional[str]
    date_created: Optional[str]