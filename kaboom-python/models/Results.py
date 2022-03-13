from dataclasses import dataclass
from typing import Optional
from .cartoon import Cartoon

@dataclass
class CartoonsResults:
    count: Optional[int]
    next: Optional[str]
    previous: Optional[str]
    results: Optional[list[Cartoon]]