from flask import Blueprint, request, jsonify
from models.database import get_db_connection

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
                (order_id, item["product_id"], item["quantity"], item["price"])
            )

            # 更新庫存
            cursor.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (item["quantity"], item["product_id"])
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