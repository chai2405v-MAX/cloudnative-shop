from flask import Flask

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 75000},
        {"id": 2, "name": "Phone", "price": 40000},
        {"id": 3, "name": "Headset", "price": 5000},
    ]
    return products
@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


