from models import app, jsonify, request, User, Task, db


# Routes for users
@app.route('/users', methods=['GET'])
def get_users():
    users = [{'id': user.id, 'username': user.username} for user in User.query.all()]
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    if not username:
        return jsonify({'error': 'username cannot be empty'}), 400
    if not email:
        return jsonify({'error': 'email cannot be empty'}), 400

    existing_user = User.query.filter_by(username=username, email=email).all()
    if existing_user:
        return jsonify({ "error": "user already exists"})

    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
        return jsonify({'error': "username already exists"})

    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({'error': "email already exists"}), 409

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully', "User ID": new_user.id})


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Delete tasks associated with the user
        Task.query.filter_by(user_id=user_id).delete()

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



@app.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    if 'username' not in data:
        return jsonify({'error': 'Missing username in JSON data'}), 400
    user.username = data['username']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})