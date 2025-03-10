import pytest
import httpx

USERNAME = "TestUser"
RESET_URL = f"http://127.0.0.1:8000/api/v1/reset?username={USERNAME}"
LOGIN_URL = "http://127.0.0.1:8000/api/v1/login"
MOVE_URL = "http://127.0.0.1:8000/api/v1/move"

async def login_request():
    """Simulates a frontend login."""
    payload = {"username": USERNAME}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(LOGIN_URL, json=payload)
        assert response.status_code == 200

async def reset_request():
    """Reset Game state"""
    async with httpx.AsyncClient() as client:
        response = await client.get(RESET_URL)
        assert response.status_code == 200
        game_state = response.json()
        assert game_state["current_position"] == [1, 0]
        return game_state

async def move_request(direction):
    """Simulates a frontend move request."""
    payload = {"username": USERNAME, "direction": direction}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(MOVE_URL, json=payload)
        assert response.status_code == 200
        game_state = response.json()
        assert game_state["health"] >= 0
        return game_state

@pytest.mark.asyncio
async def test_integration():
    """Test basic movement integration"""
    await login_request()
    game_state = await reset_request()
    
    # Move down 5 times to reach position [1,5]
    for _ in range(5):
        game_state = await move_request("down")
    
    assert game_state["current_position"] == [1,5]
    assert game_state["health"] > 0

@pytest.mark.asyncio
async def test_solver():
    """Test complete maze solution"""
    await login_request()
    game_state = await reset_request()
    
    # Solution path to reach end position [9,5]
    solution_path = ["down"] * 5 + ["right"] * 8
    
    for move in solution_path:
        game_state = await move_request(move)
    
    assert game_state["health"] == 666  # Win condition
    assert game_state["current_position"] == [9,5]  # End position
