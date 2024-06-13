from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
file_processor_url = "http://file-processor:7000/calculate"


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'file' not in data or 'product' not in data\
            or not data.get('file') or not data.get('product'):
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join('/data', data.get('file'))

    if not os.path.exists(file_path):
        return jsonify({"file": data.get('file'), "error": "File not found."})

    response = requests.post(file_processor_url, json=data)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
