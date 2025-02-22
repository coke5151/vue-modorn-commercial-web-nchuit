from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.product import product_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
