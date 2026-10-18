import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Чтобы веб-панель могла отправлять запросы

CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"aim": False, "esp": True}

def save_config(data):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify(load_config())

@app.route('/api/toggle', methods=['POST'])
def toggle_feature():
    data = request.json
    feature = data.get("feature")
    state = data.get("state")
    
    config = load_config()
    config[feature] = state
    save_config(config)
    
    print(f"[BACKEND] Feature {feature} set to {state}")
    return jsonify({"success": True, "config": config})

if __name__ == '__main__':
    print("Vesta Backend running on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000)
