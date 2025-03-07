from flask import Blueprint, request, jsonify
from models.database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint('order', __name__) # 建立 Blueprint 物件

@orders_bp.route("/place_order", methods=["POST"]) # 新增訂單
def place_order():
    data = request.json # 取得 POST 資料
    user_id = data.get("user_id") # 取得使用者 ID
    items = data.get("items", []) # 預設為空清單
    total = data.get("total")  # 新增 total 欄位
    name = data.get("name") # 新增 name 欄位
    city = data.get("city")  # 新增 city 和 
    district = data.get("district")  # district 欄位
    address = data.get("address") # 新增 address 欄位
    address = city + dictirct + address  # 合併地址
    phone = data.get("phone") # 新增 phone 欄位
    payment = data.get("payment")  # 新增 payment 欄位
    if not (user_id and items and total and name and address and phone and payment): # 檢查是否有缺少參數
        return jsonify({"error": "缺少必要參數"}), 400 # 回應錯誤訊息

    conn = get_db_connection() # 建立資料庫連線
    cursor = conn.cursor() # 建立游標

    try:
        # 插入訂單
        cursor.execute("INSERT INTO orders (user_id, total) VALUES (%s, %s)", (user_id, total)) # 插入訂單
        order_id = cursor.lastrowid  # 取得最新的訂單 ID

        # 插入訂單商品
        for item in items: # 逐一處理訂單商品
            cursor.execute( # 插入訂單商品
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)", 
                (order_id, item["id"], item["quantity"], item["price"])
            )

            # 更新庫存
            cursor.execute( # 更新庫存
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (item["quantity"], item["id"])
            )

        # 插入地址
        cursor.execute( # 插入地址
            "INSERT INTO addresses (user_id, name, phone, address) VALUES (%s, %s, %s, %s)",
            (user_id, name, phone, address)
        )

        conn.commit() # 提交交易
        return jsonify({"message": "訂單已成功建立", "order_id": order_id})

    except Exception as e: # 處理例外
        conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally: # 確保最後一定會執行
        cursor.close() # 關閉游標
        conn.close() # 關閉資料庫連線

@orders_bp.route("/orders", methods=["GET"]) # 取得使用者訂單
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
