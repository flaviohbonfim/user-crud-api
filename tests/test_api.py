import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from src.infrastructure.api.routes import router as user_router

def get_test_app():
    app = FastAPI()
    app.include_router(user_router)
    return app

@pytest.mark.asyncio
async def test_create_user_success():
    app = get_test_app()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"name": "John Doe", "email": "john@example.com", "phone": "123456789"}
        response = await ac.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

@pytest.mark.asyncio
async def test_get_user_not_found():
    app = get_test_app()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/non-existent-id")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_all_users():
    app = get_test_app()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create one user first
        await ac.post("/users/", json={"name": "Jane", "email": "jane@example.com", "phone": "987654321"})
        response = await ac.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.asyncio
async def test_delete_user():
    app = get_test_app()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create user
        create_res = await ac.post("/users/", json={"name": "To Delete", "email": "del@example.com", "phone": "00000"})
        user_id = create_res.json()["id"]
        
        # Delete user
        delete_res = await ac.delete(f"/users/{user_id}")
    assert delete_res.status_code == 204
    
    # Verify deleted
    async with AsyncClient(app=app, base_url="http://test") as ac:
        get_res = await ac.get(f"/users/{user_id}")
    assert get_res.status_code == 404
