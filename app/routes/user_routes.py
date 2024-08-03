from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user = User(user_id=user_id)
    db.session.add(user)
    db.session.commit()

    return jsonify(
        {"message": "User created", "user": {"id": user.id, "user_id": user.user_id, "points": user.points}}), 201


@user_routes.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": {"id": user.id, "user_id": user.user_id, "points": user.points}}), 200
