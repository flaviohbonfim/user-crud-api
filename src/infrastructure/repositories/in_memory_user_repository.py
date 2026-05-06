from uuid import UUID
from typing import List, Optional, Dict
from src.domain.entities import User
from src.application.repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: Dict[UUID, User] = {}

    async def save(self, user: User) -> User:
        self._users[user.id] = user
        return user

    async def find_by_id(self, user_id: UUID) -> Optional[User]:
        return self._users.get(user_id)

    async def find_all(self) -> List[User]:
        return list(self._users.values())

    async def update(self, user: User) -> User:
        if user.id in self._users:
            self._users[user.id] = user
            return user
        return None

    async def delete(self, user_id: UUID) -> None:
        if user_id in self._users:
            del self._users[user_id]
