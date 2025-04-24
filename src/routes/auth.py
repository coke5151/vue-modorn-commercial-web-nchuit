import datetime
import re

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models.user import create_user, get_user_by_email

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    # 取得表單資料
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
    address = data.get("address")
    birth_date = data.get("birth_date")

    # 🛑 檢查 Email 格式
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400

    # 🛑 檢查密碼長度
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    # 🛑 檢查是否已註冊
    if get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    # 🛑 檢查名稱（至少兩個中文字符）
    if not re.match(r"^[\u4e00-\u9fa5]{2,}$", name):
        return jsonify({"error": "Name must be at least 2 Chinese characters"}), 400

    # 🛑 檢查地址（確保是台灣地址格式）
    if not re.match(r"^(?:(\S{2,3}[縣市]))\s*(\S{2,3}[鄉鎮市區])?\s*(\S+[路街道巷弄])(\d+號?)?", address):
        return jsonify({"error": "Invalid Taiwan address format"}), 400

    # 🛑 檢查生日格式（YYYY-MM-DD）
    try:
        birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid birth date format (YYYY-MM-DD)"}), 400

    # 🔑 密碼加密
    password_hash = generate_password_hash(password)

    # ✅ 建立使用者
    result = create_user(email, password_hash, name, address, birth_date)

    return jsonify(result), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = get_user_by_email(email)
    if user and check_password_hash(user["password_hash"], password):
        access_token = create_access_token(identity=str(user["id"]), expires_delta=datetime.timedelta(days=1))
        return jsonify({"message": "Login successful", "access_token": access_token, "user_id": user["id"]})

    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """測試是否能夠正確取得 `user_id`"""
    user_id = get_jwt_identity()

    return jsonify({"message": "Access granted", "user_id": user_id})
