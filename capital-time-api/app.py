from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"  # Shared secret

capital_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
    "Tokyo": "Asia/Tokyo",
    "Delhi": "Asia/Kolkata",
    "Canberra": "Australia/Sydney"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    return decorator

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get('city')
    if city not in capital_timezones:
        return jsonify({"error": f"{city} not found in database"}), 404
    tz = pytz.timezone(capital_timezones[city])
    now = datetime.now(tz)
    offset = now.strftime('%z')
    formatted_offset = f"{offset[:3]}:{offset[3:]}"
    return jsonify({
        "city": city,
        "local_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": formatted_offset
    })

@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
