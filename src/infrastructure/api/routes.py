from fastapi import APIRouter, HTTPException, Depends, status
from uuid import UUID
from typing import List
from src.application.use_cases import (
    CreateUserUseCase,
    GetUserUseCase,
    GetAllUsersUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase
)
from src.infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from src.infrastructure.api.schemas.user_schemas import (
    UserCreateSchema,
    UserUpdateSchema,
    UserResponseSchema
)

# In a real application, you would use a proper DI container or FastAPI Depends with a factory
# For this simple CRUD, we'll use a single instance for the demo
user_repository = InMemoryUserRepository()

def get_user_repository():
    return user_repository

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreateSchema, 
    repo: InMemoryUserRepository = Depends(get_user_repository)
):
    use_case = CreateUserUseCase(repo)
    user = await use_case.execute(user_data.name, user_data.email, user_data.phone)
    return user

@router.get("/", response_model=List[UserResponseSchema])
async def get_all_users(repo: InMemoryUserRepository = Depends(get_user_repository)):
    use_case = GetAllUsersUseCase(repo)
    return await use_case.execute()

@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(
    user_id: UUID, 
    repo: InMemoryUserRepository = Depends(get_user_repository)
):
    use_case = GetUserUseCase(repo)
    user = await use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_user(
    user_id: UUID, 
    user_data: UserUpdateSchema, 
    repo: InMemoryUserRepository = Depends(get_user_repository)
):
    use_case = UpdateUserUseCase(repo)
    user = await use_case.execute(user_id, user_data.name, user_data.email, user_data.phone)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID, 
    repo: InMemoryUserRepository = Depends(get_user_repository)
):
    use_case = DeleteUserUseCase(repo)
    await use_case.execute(user_id)
    return None
