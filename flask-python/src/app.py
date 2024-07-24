from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasksList = []
task_id = 0

@app.route('/tasks', methods=['GET'])
def getTask():
    try:
        tasks = [task.__dict__ for task in tasksList]
        response = {
            'tasks': tasks,
            'total_tasks': Task.total_tasks(tasks)
        }
        return jsonify(response), 200, {'content-type': 'application/json'}
    except Exception as err:
        print(err)
        return jsonify({'message': 'An error occurred'}), 500
    
@app.route('/tasks/<int:id>', methods=['GET'])
def getTaskById(id):
    try:
        for task in tasksList:
            if task.id == id:
                response = {
                    'message': 'Task found successfully',
                    'task': task.__dict__
                }
                return jsonify(response), 200, {'content-type': 'application/json'}
        return jsonify({'message': 'Task not found'}), 404
    except Exception as err:
        print(err)
        return jsonify({'message': 'An error occurred'}), 500

@app.route('/tasks', methods=['POST'])
def createTask():
    try:
        data = request.get_json()

        global task_id
        task_id += 1

        new_task = Task(task_id, data['title'], data['description'])
        tasksList.append(new_task)
        response = {
            'message': 'Task created successfully',
            'task': new_task.__dict__
        }
        return jsonify(response), 201, {'content-type': 'application/json'}
    except KeyError:
        return jsonify({'message': 'Invalid request'}), 400
    
@app.route('/tasks/<int:id>', methods=['PUT'])
def updateTask(id):
    try:
        data = request.get_json()
        task = next((task for task in tasksList if task.id == id), None)
        if task:
            task.title = data['title']
            task.description = data['description']
            response = {
                'message': 'Task updated successfully',
                'task': task.__dict__
            }
            return jsonify(response), 200, {'content-type': 'application/json'}
        else:
            return jsonify({'message': 'Task not found'}), 404, {'content-type': 'application/json'}
    except KeyError:
        return jsonify({'message': 'Invalid request'}), 400
    
@app.route('/tasks/<int:id>', methods=['PATCH'])
def completeTask(id):
    try:
        task = next((task for task in tasksList if task.id == id), None)
        if task:
            task.completed = not task.completed
            response = {
                'message': 'Task status updated successfully',
                'task': task.__dict__
            }
            return jsonify(response), 200, {'content-type': 'application/json'}
        else:
            return jsonify({'message': 'Task not found'}), 404, {'content-type': 'application/json'}
    except KeyError:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id):
    try:
        task = next((task for task in tasksList if task.id == id), None)
        if task:
            tasksList.remove(task)
            response = {
                'message': 'Task deleted successfully',
                'task': task.__dict__
            }
            return jsonify(response), 200, {'content-type': 'application/json'}
        else:
            return jsonify({'message': 'Task not found'}), 404, {'content-type': 'application/json'}
    except KeyError:
        return jsonify({'message': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True)