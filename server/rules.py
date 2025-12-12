from logger import log_event

SUSPICIOUS_PATHS = [
    "/admin",
    "/wp-login.php",
    "/phpmyadmin",
    "/.env"
]

def inspect_request(req):
    ip = req.remote_addr
    path = req.path
    user_agent = req.headers.get("User-Agent", "")

    if path in SUSPICIOUS_PATHS:
        log_event("SUSPICIOUS_PATH", ip, path)

    if "curl" in user_agent.lower() or "python" in user_agent.lower():
        log_event("AUTOMATION_TOOL", ip, user_agent)
