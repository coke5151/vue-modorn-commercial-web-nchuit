from flask import Blueprint, jsonify
from models.product import get_all_products

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify(products)
