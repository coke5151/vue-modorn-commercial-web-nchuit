from flask import Blueprint, jsonify, request

from ..models.database import get_db_connection

news_bp = Blueprint("news", __name__)


@news_bp.route("/news", methods=["GET"])
def get_all_news():
    """取得所有新聞列表 (首頁使用)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news ORDER BY created_at DESC")
    news_list = cursor.fetchall()
    return jsonify(news_list)


@news_bp.route("news/<int:news_id>", methods=["GET"])
def get_news_detail(news_id):
    """取得特定新聞的詳細內容"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM news WHERE id = %s", (news_id,))
    news = cursor.fetchone()
    if not news:
        return jsonify({"error": "News not found"}), 404
    return jsonify(news)


@news_bp.route("/", methods=["POST"])
def add_news():
    """新增新聞 (管理後台使用)"""
    data = request.json
    db = get_db_connection()
    cursor = db.cursor()
    sql = """
        INSERT INTO news (title, subtitle, content, image_url)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (data["title"], data["subtitle"], data["content"], data.get("image_url", "")))
    db.commit()
    return jsonify({"message": "News added successfully", "id": cursor.lastrowid})


@news_bp.route("/<int:news_id>", methods=["DELETE"])
def delete_news(news_id):
    """刪除新聞 (管理後台使用)"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM news WHERE id = %s", (news_id,))
    db.commit()
    return jsonify({"message": "News deleted successfully"})
