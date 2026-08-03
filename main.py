from fastapi import FastAPI, HTTPException
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

@app.post("/todos", response_model=TodoOut)
def create_todo(todo: TodoCreate):
    """Создаем новую задачу."""
    title = todo.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail="Название задачи не может быть пустым")
    new_id = len(todos) + 1
    new_todo = {
        "id": new_id,
        "title": title,
        "completed": False
    }
    todos.append(new_todo)
    return new_todo

@app.get("/todos/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    """Получаем задачу по ID."""
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.put("/todos/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo: TodoCreate):
    """Обновляем задачу по ID."""
    title = todo.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail="Название задачи не может быть пустым")
    for todo_item in todos:
        if todo_item["id"] == todo_id:
            todo_item["title"] = title
            return todo_item
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Удаляем задачу."""
    for todo_item in todos:
        if todo_item["id"] == todo_id:
            todos.remove(todo_item)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Задача не найдена")