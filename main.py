from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Хранилище в памяти в виде списка словарей
todos = []

# Pydantic схема для создания задачи
class TodoCreate(BaseModel):
    title: str

# Схема для ответа
class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/todos")
def get_todos():
    """Возвращаем все задачи."""
    return todos

@app.post("/todos")
def create_todo(todo: TodoCreate):
    """Создаем новую задачу."""
    new_id = len(todos) + 1
    new_todo = {
        "id": new_id,
        "title": todo.title,        
        "completed": False
    }
    todos.append(new_todo)
    return new_todo

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """Получаем задачу по ID."""
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None  

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate):
    """Обновляем задачу по ID"""
    for todo_item in todos:
        if todo_item["id"] == todo_id:
            todo_item["title"] = todo.title  
            return todo_item
    return None

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Удаляем задачу."""
    for todo_item in todos:
        if todo_item["id"] == todo_id:
            todos.remove(todo_item)
            break
    return {"message": "deleted"}