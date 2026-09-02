from flask import Flask

app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = [
        {
            "id": 101,
            "product": "Laptop",
            "quantity": 1,
            "status": "confirmed"
        }
    ]
    return orders

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)