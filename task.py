from models import request, Task, jsonify, db, app

# Routes for tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')  # 'completed' or 'uncompleted' or None
    if status == 'completed':
        all_tasks = Task.query.filter(Task.completed == True).all()
    elif status == 'uncompleted':
        all_tasks = Task.query.filter(Task.completed == False).all()
    else:
        all_tasks = Task.query.filter(Task.completed.isnot(None)).all()
    tasks = [{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed, 'date_created': task.date_created.strftime("%Y-%m-%d %H:%M:%S"), 'user_id': task.user_id} for task in all_tasks]
    return jsonify(tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    required_keys = ['title', 'description', 'user_id']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required keys in JSON data'}), 400
    new_task = Task(title=data['title'], description=data['description'], user_id=data['user_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully'})

@app.route('/mark_complete/<int:id>', methods=['PUT'])
def mark_complete(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()
    return jsonify({'message': 'Task marked as complete'})

# Route to view all tasks by user
@app.route('/user_tasks/<int:user_id>', methods=['GET'])
def get_user_tasks(user_id):
    tasks = [{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed, 'date_created': task.date_created.strftime("%Y-%m-%d %H:%M:%S")} for task in Task.query.filter_by(user_id=user_id).all()]
    return jsonify(tasks)
