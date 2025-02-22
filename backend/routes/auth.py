import re
import jwt
import datetime
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import create_user, get_user_by_email
auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "your_secret_key"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    
    password_hash = generate_password_hash(password)
    result = create_user(email, password_hash)

    return jsonify(result), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)
    if user and check_password_hash(user['password'], password):
        token = jwt.encode({"user_id": user["id"], "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"message": "Login successful", "token": token, "user_id": user["id"]})
    
    return jsonify({"error": "Invalid credentials"}), 401
