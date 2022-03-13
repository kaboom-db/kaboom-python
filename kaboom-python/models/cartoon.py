from dataclasses import dataclass
from typing import Optional
from .genre import Genre
from .network import Network
from .character import Character

@dataclass
class Cartoon:
    id: Optional[int]
    genres: Optional[list[Genre]]
    network: Optional[Network]
    characters: Optional[list[Character]]
    name: Optional[str]
    summary: Optional[str]
    season_count: Optional[int]
    cover_image: Optional[str]
    background_image: Optional[str]
    status: Optional[str]
    rating: Optional[float]
    website: Optional[str]
    tmdb_id: Optional[int]
    imdb_id: Optional[str]
    date_created: Optional[str]