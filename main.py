from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV file
try:
    df = pd.read_csv("data/results.csv", dtype={"RollNo": str})
except FileNotFoundError:
    df = pd.DataFrame(columns=["RollNo", "Name", "Status", "Marks", "Grade", "SchoolName", "SchoolCode"])

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Gazette API is running. Use /api/result?roll=<ROLL_NO>"
    })

@app.route("/api/result")
def get_result():
    roll = request.args.get("roll")
    if not roll:
        return jsonify({"status": "error", "message": "Roll number required"}), 400

    # Search for roll number
    row = df[df["RollNo"] == roll].to_dict(orient="records")
    if row:
        return jsonify({"status": "success", "data": row[0]})
    else:
        return jsonify({"status": "error", "message": "Roll number not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
