from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .routes.auth import auth_bp
from .routes.chatbot import chatbot_bp
from .routes.news import news_bp
from .routes.orders import orders_bp
from .routes.product import product_bp
from .routes.user import user_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["JWT_SECRET_KEY"] = "your_secret_key"
app.config["JWT_IDENTITY_CLAIM"] = "sub"

jwt = JWTManager(app)  # 啟動 JWT

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(orders_bp, url_prefix="/api")
app.register_blueprint(product_bp, url_prefix="/api")
app.register_blueprint(news_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")
app.register_blueprint(chatbot_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
