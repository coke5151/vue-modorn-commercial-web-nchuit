from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import get_user_by_id, update_user

user_bp = Blueprint('user', __name__)

@user_bp.route("/profile", methods=["GET"])
@jwt_required()  # 確保只有登入後的用戶才能存取
def get_profile():
    user_id = get_jwt_identity()  # 取得 JWT Token 內的使用者 ID
    user = get_user_by_id(user_id)  # 查詢用戶資料
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
    "name": user["name"],
    "email": user["email"],
    "address": user["address"],
    "birth_date": user["birth_date"].strftime("%Y-%m-%d"),
})

@user_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()  # 取得當前登入的用戶 ID
    data = request.get_json()

    if not data.get("name") or not data.get("address") or not data.get("birth_date"):
        return jsonify({"error": "Missing required fields"}), 400

    update_user(user_id, data["name"], data["address"], data["birth_date"])

    return jsonify({"message": "Profile updated successfully"})