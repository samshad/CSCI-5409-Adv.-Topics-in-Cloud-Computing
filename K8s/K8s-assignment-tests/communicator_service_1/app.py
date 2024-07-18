import os
import requests

from flask import Flask, request

app = Flask(__name__)

FOLDER_NAME = "/"


@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Endpoint to calculate based on the provided file path.

    Expects a JSON payload with a 'file' key containing the path to the file.

    Returns:
        dict: Response containing the status of the file and any error message.
    """
    try:
        if request.json.get("file") is None:
            return {
                "file": None,
                "error": "Invalid JSON input."
            }
    except KeyError:
        return {
            "file": None,
            "error": "Invalid JSON input."
        }

    file_path = FOLDER_NAME + request.json["file"]
    if not os.path.isfile(file_path):
        return {
            "file": file_path,
            "error": "File not found."
        }

    sum_url = "http://k8s-c2-dep2-service.default.svc.cluster.local/sum"
    response = requests.post(url=sum_url, json=request.json, headers={'Content-Type': 'application/json'})
    print(response)
    return response


@app.route("/store-file", methods=["POST"])
def store_file():
    """
    Endpoint to store the content to a file.

    Expects a JSON payload with 'file' and 'data' keys.
    The 'file' key should contain the path to the file.
    The 'data' key should contain the content to be written to the file.

    Returns:
        dict: Response containing the status of the file storage and any error message.
    """
    try:
        if request.json.get("file") is None:
            return {
                "file": None,
                "error": "Invalid JSON input."
            }
    except KeyError:
        return {
            "file": None,
            "error": "Invalid JSON input."
        }

    file_path = FOLDER_NAME + request.json["file"]
    try:
        with open(file_path, "w+") as csvfile:
            csvfile.write(request.json["data"].replace(" ", ""))
    except Exception as e:
        return {
            "file": None,
            "error": "Error while storing the file to the storage."
        }

    return {
        "file": file_path,
        "message": "Success."
    }


if __name__ == "__main__":
    app.json.sort_keys = False
    app.run(host="0.0.0.0", port=6000, debug=True)
