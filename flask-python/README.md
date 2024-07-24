# TODO with flask in python

## Install requirements

```bash
pip install -r requirements.txt
```

## Run the app

```bash
py src/app.py
```

## Endpoints

- GET /tasks

  - Get all tasks

- GET /tasks/{id}

  - Get task by id

- POST /tasks

  - Create a new task
  - Body: { "title": "Task title", "description": "Task description" }

- PUT /tasks/{id}

  - Change title and description values
  - Body: { "title": "Task title", "description": "Task description" }

- PATCH /tasks/{id}

  - Change completed status

- DELETE /tasks/{id}

  - Delete task

### Example

```bash
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Task title", "description": "Task description"}'
```

```bash
curl -X GET http://localhost:5000/tasks
```

```bash
curl -X GET http://localhost:5000/tasks/1
```

```bash
curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "New task title", "description": "New task description"}'
```

```bash
curl -X PATCH http://localhost:5000/tasks/1
```

```bash
curl -X GET http://localhost:5000/tasks/1
```

```bash
curl -X DELETE http://localhost:5000/tasks/1
```

```bash
curl -X GET http://localhost:5000/tasks
```
