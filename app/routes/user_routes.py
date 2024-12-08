from flask import Blueprint, jsonify, request
from app import db
from app.models.user import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/api/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    users = User.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'total': users.total,
        'pages': users.pages,
        'current_page': users.page,
        'per_page': users.per_page,
        'next_page': users.next_num,
        'prev_page': users.prev_num,
        'users': [user.user_id for user in users.items]
    }), 200


@user_routes.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user = User(user_id=user_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201


@user_routes.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user_id": user.user_id, "points": user.points}), 200


@user_routes.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.user_id = data.get('user_id', user.user_id)
    user.points = data.get('points', user.points)
    db.session.commit()
    return jsonify({"message": "User updated"}), 200


@user_routes.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
