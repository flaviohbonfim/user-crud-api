from uuid import UUID
from typing import List, Optional
from src.domain.entities import User
from src.application.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, name: str, email: str, phone: str) -> User:
        user = User(name=name, email=email, phone=phone)
        return await self.user_repository.save(user)

class GetUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: UUID) -> Optional[User]:
        return await self.user_repository.find_by_id(user_id)

class GetAllUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self) -> List[User]:
        return await self.user_repository.find_all()

class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: UUID, name: str, email: str, phone: str) -> Optional[User]:
        user = await self.user_repository.find_by_id(user_id)
        if not user:
            return None
        user.name = name
        user.email = email
        user.phone = phone
        return await self.user_repository.update(user)

class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: UUID) -> None:
        await self.user_repository.delete(user_id)
