from flask import Flask
import urllib.request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    products_response = urllib.request.urlopen(
        "http://product-api:5001/products"
    )
    products = json.loads(products_response.read().decode())

    orders_response = urllib.request.urlopen(
        "http://order-api:5002/orders"
    )
    orders = json.loads(orders_response.read().decode())

    return {
        "service": "CloudNative Shop Frontend",
        "products": products,
        "orders": orders
    }

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)