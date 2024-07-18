import csv
from flask import Flask, request

app = Flask(__name__)

FOLDER_NAME = "/"


@app.route("/sum", methods=["POST"])
def sum_products():
    """
    Endpoint to calculate the sum of products for a specified product from a CSV file.

    Expects a JSON payload with 'file' and 'product' keys.
    The 'file' key should contain the path to the CSV file.
    The 'product' key should contain the product name to sum values for.

    Returns:
        dict: Response containing the file path and the calculated sum, or an error message.
    """
    sum_total = 0
    file_path = FOLDER_NAME + request.json["file"]
    product_name = request.json["product"]

    with open(file_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if len(row) != 2:
                return {
                    "file": file_path,
                    "error": "Input file not in valid CSV format."
                }
            if row[0] == product_name:
                sum_total += int(row[1])

    return {
            "file": request.json["file"],
            "sum": sum
        }


if __name__ == "__main__":
    app.json.sort_keys = False
    app.run(host="0.0.0.0", port=7000)
