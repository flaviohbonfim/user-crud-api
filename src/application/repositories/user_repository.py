from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.entities import User

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> User:
        pass

    @abstractmethod
    async def find_by_id(self, user_id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    async def find_all(self) -> List[User]:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, user_id: UUID) -> None:
        pass
