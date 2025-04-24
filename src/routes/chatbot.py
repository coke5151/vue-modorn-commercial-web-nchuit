import google.generativeai as genai
import requests
from flask import Blueprint, jsonify, request

from ..models.database import get_db_connection

chatbot_bp = Blueprint("chatbot", __name__)

# 設定 Google Gemini API Key
GOOGLE_API_KEY = "AIzaSyDGPaCu4qEfKdSEt6_F6RBCacrPAVuI_Dg"
SEARCH_API_KEY = "AIzaSyBdk9-rBAloADzHC1C4E9bRsAy6enoKaMQ"
SEARCH_ENGINE_ID = "4514dc2fb56214165"

# 設定 Gemini 模型
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# 商品推薦（假設你有 MySQL 資料庫）
def get_recommended_products():
    return [
        {"id": 101, "name": "MacBook Pro 16吋", "price": "NT$89,900"},
        {"id": 102, "name": "Sony WH-1000XM5 耳機", "price": "NT$12,900"},
        {"id": 103, "name": "iPhone 15 Pro Max", "price": "NT$45,900"},
    ]


# Google Custom Search API（RAG）
def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    response = requests.get(url).json()
    results = [item["snippet"] for item in response.get("items", [])]
    return "\n".join(results)


def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT id, name, price FROM products LIMIT 5"
    cursor.execute(sql)
    return cursor.fetchall()


# API 路由：處理 AI 聊天
@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    # 從資料庫查詢相關商品
    # 查詢商品
    related_products = get_products()

    prompt = f"""
    使用者問題: {user_message}

    請 **直接回答與購物相關的問題**，並根據資料庫中的商品資訊推薦正確的商品。
    如果問題與購物無關，請回覆：「這個問題我無法回答，請詢問客服。」

    ### **回答格式：**
    1. **簡要回答用戶問題**
    2. **提供商品推薦（包含名稱、編號、價格）**
    3. **所有推薦商品需來自資料庫，避免錯誤編號**
    4. **商品推薦的格式如下，讓前端可以正確顯示：**
    5. **如果問題與購物無關，請回覆：「這個問題我無法回答，請詢問客服。」**
    6. **對方是客戶不是賣家，不需要回答太專業的問題，請他重新輸入問題就好**
    ```json
    [
        {{"id": 1, "name": "Gaming Mouse 1", "price": 999}},
        {{"id": 2, "name": "Gaming Mouse 2", "price": 799}},
        {{"id": 3, "name": "Gaming Mouse Pro", "price": 1299}},
        {{"id": 4, "name": "Gaming Mouse X", "price": 899}},
        {{"id": 5, "name": "Mechanical Keyboard V1", "price": 1499}}
    ]
    商品列表:{related_products}
    """

    response = model.generate_content(prompt, generation_config={"max_output_tokens": 400})

    return jsonify({"type": "text", "data": response.text})
