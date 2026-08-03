"""
Тесты для Todo API.
"""
from fastapi.testclient import TestClient
from main import app, todos

client = TestClient(app)


def test_create_todo():
    """Создание задачи."""
    todos.clear()
    response = client.post("/todos", json={"title": "Купить молоко"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Купить молоко"
    assert data["id"] == 1
    assert data["completed"] == False


def test_get_todos():
    """Получение списка задач."""
    todos.clear()
    client.post("/todos", json={"title": "Прибраться"})
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_get_todo_by_id():
    """Получение задачи по ID."""
    todos.clear()
    client.post("/todos", json={"title": "Сделать тесты"})
    response = client.get("/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Сделать тесты"
    assert data["id"] == 1


def test_update_todo():
    """Обновление задачи."""
    todos.clear()
    client.post("/todos", json={"title": "Старое название"})
    response = client.put("/todos/1", json={"title": "Новое название"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Новое название"


def test_delete_todo():
    """Удаление задачи."""
    todos.clear()
    client.post("/todos", json={"title": "Удаляемая задача"})
    response = client.delete("/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "deleted"
    get_response = client.get("/todos")
    assert get_response.json() == []