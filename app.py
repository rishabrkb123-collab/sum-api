import os
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-KEY")
        if not key or key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated


def validate_numbers(body):
    """Returns (numbers, error_message). error_message is None on success."""
    if body is None:
        return None, "Request body is required"
    if "numbers" not in body:
        return None, "Missing required key: 'numbers'"
    numbers = body["numbers"]
    if not isinstance(numbers, list):
        return None, "'numbers' must be a list"
    for item in numbers:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return None, "All elements in 'numbers' must be numeric"
    return numbers, None


@app.route("/sum", methods=["POST"])
@require_api_key
def sum_numbers():
    body = request.get_json(silent=True)
    numbers, error = validate_numbers(body)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "result": sum(numbers),
        "count": len(numbers),
        "numbers": numbers,
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=port)
