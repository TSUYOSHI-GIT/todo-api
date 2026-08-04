# Todo API

Простой REST API для списка задач.  
Делал для портфолио в Т-Академию, чтобы попробовать веб и FastAPI.

## Что умеет

- Показывать все задачи
- Создавать новую задачу
- Просматривать задачу по id
- Обновлять название задачи
- Удалять задачу
- Возвращает 404 если задача не найдена, 400 если название пустое
- Все данные хранятся в памяти, при перезапуске сбрасываются

## Стек

- Python 3.14+
- FastAPI
- Pydantic
- Pytest
- Uvicorn

## Как запустить

```bash
# Клонировать репозиторий
https://github.com/TSUYOSHI-GIT/todo-api.git
cd todo-api

# Создать и активировать виртуальное окружение
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер
uvicorn main:app --reload
```

После запуска открывай в браузере http://127.0.0.1:8000/docs — там можно отправлять запросы и смотреть ответы

## Тесты

```bash
python -m pytest
```

## Эндпоинты

* **GET** `/todos` — все задачи
* **POST** `/todos` — создать
* **GET** `/todos/{id}` — одна задача
* **PUT** `/todos/{id}` — обновить
* **DELETE** `/todos/{id}` — удалить