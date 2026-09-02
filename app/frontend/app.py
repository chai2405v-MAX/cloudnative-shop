from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
    <h1>CloudNative Shop</h1>
    <p>Frontend service is running.</p>
    <p>Product API: http://localhost:5001/products</p>
    <p>Order API: http://localhost:5002/orders</p>
    """

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)