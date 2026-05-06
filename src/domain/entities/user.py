from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class User:
    name: str
    email: str
    phone: str
    id: UUID = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid4()
