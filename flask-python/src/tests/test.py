import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

def test_create_task():
    new_task_data = {
        'title': 'Nova Tarefa',
        'description': 'Descrição da nova tarefa',
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    response_data = response.json()

    assert response.status_code == 201
    assert "message" in response_data
    assert response_data['task']['id']

    tasks.append(response_data['task']['id'])

def test_get_task():
    response = requests.get(f'{BASE_URL}/tasks/{tasks[0]}')
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['task']['id'] == tasks[0]

def test_get_all_task():
    response = requests.get(f'{BASE_URL}/tasks')
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data['tasks']) > 0

def test_get_false_task():
    response = requests.get(f'{BASE_URL}/tasks/0')
    response_data = response.json()

    assert response.status_code == 404
    assert "message" in response_data

def test_update_task():
    update_task_data = {
        'title': 'Tarefa Atualizada',
        'description': 'Descrição da tarefa atualizada',
    }
    response = requests.put(f'{BASE_URL}/tasks/{tasks[0]}', json=update_task_data)
    response_data = response.json()

    assert response.status_code == 200
    assert "message" in response_data
    assert response_data['task']['title'] == update_task_data['title'] and response_data['task']['description'] == update_task_data['description']

def test_complete_task():
    response = requests.patch(f'{BASE_URL}/tasks/{tasks[0]}')
    response_data = response.json()

    assert response.status_code == 200
    assert "message" in response_data
    assert response_data['task']['completed'] == True

def test_delete_task():
    response = requests.delete(f'{BASE_URL}/tasks/{tasks[0]}')
    response_data = response.json()

    assert response.status_code == 200
    assert "message" in response_data
    assert response_data['task']['id'] == tasks[0]
    
    tasks.pop(0)

def test_delete_false_task():
    response = requests.delete(f'{BASE_URL}/tasks/0')
    response_data = response.json()

    assert response.status_code == 404
    assert "message" in response_data
