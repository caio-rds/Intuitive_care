import asyncio
import pytest
from ..main import app
from fastapi.testclient import TestClient

base_url = "http://localhost:8000"

client = TestClient(app)

@pytest.fixture(scope="function")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_search_no_name():
    response = client.get("/search")
    assert response.status_code == 400
    assert response.json() == {"detail": "Name is required"}

@pytest.mark.asyncio
async def test_search_mock():
    response = client.get("/search", params={"name": "some_name", "mock": True})
    assert response.status_code == 404
    assert response.json() == {"detail": "No organization found"}

@pytest.mark.asyncio
async def test_search_db_name():
    response = client.get("/search", params={"name": "A"})
    assert response.status_code == 200
    assert response.json()[0]["razao_social"] == "18 DE JULHO ADMINISTRADORA DE BENEFÍCIOS LTDA"
    assert response.json()[1]["razao_social"] == "2B ODONTOLOGIA OPERADORA DE PLANOS ODONTOLÓGICOS LTDA"

@pytest.mark.asyncio
async def test_search_specific_name_db():
    response = client.get("/search", params={"name": "APUB"})
    assert response.status_code == 200
    assert response.json()[0]['razao_social'] == "ASSOCIACAO DOS PROFESSORES UNIVERSITÁRIOS DA BAHIA"

@pytest.mark.asyncio
async def test_search_specific_name_mock():
    response = client.get("/search", params={"name": "APUB", "mock": True})
    assert response.status_code == 200
    assert response.json()[0]['razao_social'] == "ASSOCIACAO DOS PROFESSORES UNIVERSITÁRIOS DA BAHIA"