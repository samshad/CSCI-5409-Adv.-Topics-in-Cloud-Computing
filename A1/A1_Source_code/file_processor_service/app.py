from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)


def check_csv_empty(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        first_row = next(reader, None)
        if first_row is None:
            return True
        else:
            return False


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    file_name = data.get('file')
    product = data.get('product')
    file_path = os.path.join('/data', file_name)

    if not os.path.exists(file_path):
        return jsonify({"file": file_name, "error": "File not found."})

    if check_csv_empty(file_path):
        return jsonify({"file": file_name, "error": "Input file not in CSV format."})

    try:
        total = 0
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product:
                    total += int(row['amount'])
        return jsonify({"file": file_name, "sum": total})
    except Exception as e:
        return jsonify({"file": file_name, "error": "Input file not in CSV format."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)