from dataclasses import dataclass
from typing import Optional

@dataclass
class Login:
    token: Optional[str]
    username: Optional[str]
    user_id: Optional[int]
    email: Optional[str]
    image: Optional[str]