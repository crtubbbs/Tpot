from flask import Flask, request, jsonify
from logger import log_event
from rules import inspect_request

app = Flask(__name__)

@app.before_request
def inspect():
    inspect_request(request)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    log_event("LOGIN_ATTEMPT", request.remote_addr, username)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/admin", methods=["GET"])
def admin():
    log_event("ADMIN_PROBE", request.remote_addr)
    return "Forbidden", 403

@app.route("/wp-login.php", methods=["POST"])
def wordpress_probe():
    log_event("WP_PROBE", request.remote_addr)
    return "Not Found", 404

if __name__ == "__main__":
    print("🪤 Python Honeypot running on port 5000")
    app.run(host="0.0.0.0", port=5000)
