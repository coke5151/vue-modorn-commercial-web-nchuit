from flask import Blueprint, request, jsonify
from models.database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint('order', __name__)

@orders_bp.route("/place_order", methods=["POST"])
def place_order():
    data = request.json
    user_id = data.get("user_id")
    items = data.get("items", [])
    total = data.get("total")
    name = data.get("name")
    address = data.get("address")
    phone = data.get("phone")
    payment = data.get("payment")
    if not (user_id and items and total and name and address and phone and payment):
        return jsonify({"error": "缺少必要參數"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 插入訂單
        cursor.execute("INSERT INTO orders (user_id, total) VALUES (%s, %s)", (user_id, total))
        order_id = cursor.lastrowid  # 取得最新的訂單 ID

        # 插入訂單商品
        for item in items:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                (order_id, item["id"], item["quantity"], item["price"])
            )

            # 更新庫存
            cursor.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (item["quantity"], item["id"])
            )

        # 插入地址
        cursor.execute(
            "INSERT INTO addresses (user_id, name, phone, address) VALUES (%s, %s, %s, %s)",
            (user_id, name, phone, address)
        )

        conn.commit()
        return jsonify({"message": "訂單已成功建立", "order_id": order_id})

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

@orders_bp.route("/orders", methods=["GET"])
@jwt_required()
def get_user_orders():
    user_id = get_jwt_identity()  # 取得當前登入的使用者 ID
    try:
        query = """
            SELECT o.id AS order_id, o.total, o.created_at,
                   p.id AS product_id, p.name AS product_name, 
                   p.image_url, oi.quantity, oi.price
            FROM orders o
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            WHERE o.user_id = %s
            ORDER BY o.created_at DESC;
        """

        # 建立資料庫連線
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        orders = cursor.fetchall()

        cursor.close()
        conn.close()

        # 轉換資料格式，按 `order_id` 分組
        orders_dict = {}
        for row in orders:
            order_id = row["order_id"]
            if order_id not in orders_dict:
                orders_dict[order_id] = {
                    "order_id": order_id,
                    "total": row["total"],
                    "created_at": row["created_at"],
                    "items": []
                }
            orders_dict[order_id]["items"].append({
                "product_id": row["product_id"],
                "name": row["product_name"],
                "image": row["image_url"],
                "quantity": row["quantity"],
                "price": row["price"],
            })

        return jsonify(list(orders_dict.values())), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
