from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    id: Optional[int] = None
    name: str = ""
    email: str = ""
