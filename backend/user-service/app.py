from flask import Flask, jsonify

# Create the Flask application for the User Service.
app = Flask(__name__)


@app.get("/health")
def health_check():
    """Report that the service is running."""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    # Keep the development server available only on this computer.
    app.run(host="127.0.0.1", port=5001)
