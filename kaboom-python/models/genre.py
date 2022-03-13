from dataclasses import dataclass
from typing import Optional

@dataclass
class Genre:
    id: Optional[int]
    genre: Optional[str]